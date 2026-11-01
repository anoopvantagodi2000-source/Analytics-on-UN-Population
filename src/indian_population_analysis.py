import csv
from matplotlib import pyplot as plt
CSV_PATH = "resources/population.csv"


def compute_indian_population(path : str):
    population_of_india = {}
    with open(path,'r',encoding="utf-8") as population_csv:
        populations = csv.DictReader(population_csv)
        for population in populations:
            country = population.get("Country Name")
            year = population.get("Year")
            value = population.get("Value")
            if not country or not year or not value:
                continue
            population_of_india[year] = int(value)
    return  population_of_india


def plot_indian_population(data:dict[str,int]):
    sorted_data = sorted(data.items(),key= lambda items:items[1])
    years = [year for year,_ in sorted_data]
    population_values = [population for _,population in sorted_data]

    plt.figure(figsize=(15,15))
    plt.bar(years,population_values)
    plt.title("India Population")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.xticks(rotation=45)
    plt.ticklabel_format(axis="y",style="plain")
    plt.tight_layout()
    plt.show()

def main():
    data = compute_indian_population(CSV_PATH)
    plot_indian_population(data)

if __name__ == "__main__":
    main()
