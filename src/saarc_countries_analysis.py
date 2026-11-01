import csv
from collections import defaultdict
from matplotlib import pyplot as plt

POPULATION_CSV = "resources/population.csv"

saarc_countries = {
    "Afghanistan",
    "Bangladesh",
    "Bhutan",
    "India",
    "Maldives",
    "Nepal",
    "Pakistan",
    "Sri Lanka"
}
def compute_saarc_countries_population(path:str):
    saarc_population = defaultdict(int)
    with open(path,'r',encoding="utf-8") as countries_csv:
        countries = csv.DictReader(countries_csv)
        for country in countries:
            extracted_country = country.get("Country Name")
            extracted_year = country.get("Year")
            population = country.get("Value")
            if not extracted_country or not extracted_year or not population:
                continue
            if extracted_country in saarc_countries:
                saarc_population[extracted_year] += int(population)

    return saarc_population


def plot(data:dict[str,int]):
    sorted_data = sorted(data.items())
    year = [year for year,_ in sorted_data]
    population = [population for _,population in sorted_data]
    plt.figure(figsize = (15,10))
    plt.bar(year,population)
    plt.xlabel("Year")
    plt.ylabel("SARRC Population ")
    plt.title("SARRC Population in each Year")
    plt.xticks(rotation=45)
    plt.savefig("output/total_population_of_SAARC_countries.png")

    plt.show()



def main():
    data = compute_saarc_countries_population(POPULATION_CSV)
    plot(data)

if __name__ == "__main__":
    main()
