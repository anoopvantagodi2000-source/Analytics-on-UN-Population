import csv
from matplotlib import pyplot as plt

POPULATION_CSV = "resources/population.csv"
ASIAN_COUNTRIES_CSV = "resources/asia.csv"

southeast_asian_countries = {
    "Brunei",
    "Cambodia",
    "Indonesia",
    "Laos",
    "Malaysia",
    "Myanmar",
    "Philippines",
    "Singapore",
    "Thailand",
    "Timor-Leste",
    "Vietnam"
}


def compute_southeast_countries_population(path:str,year:str):
    southeast_population = {}
    with open(path,'r',encoding="utf-8") as countries_csv:
        countries = csv.DictReader(countries_csv)
        for country in countries:
            extracted_country = country.get("Country Name")
            extracted_year = country.get("Year")
            population = country.get("Value")
            if not extracted_country or not extracted_year or not population:
                continue
            if extracted_country in southeast_asian_countries and extracted_year == year:
                southeast_population[extracted_country] = int(population)

    return southeast_population


def plot(data:dict[str,int]):
    sorted_data = sorted(data.items(),key= lambda items:items[1])
    countries = [country for country,_ in sorted_data]
    countries_population = [population for _,population in sorted_data]
    plt.figure(figsize = (12,10))
    plt.bar(countries,countries_population)
    plt.xlabel("South East Countries")
    plt.ylabel("Population")
    plt.title("South East population in Year 2014")
    plt.xticks(rotation=45)
    plt.show()

def main():
    data = compute_southeast_countries_population(POPULATION_CSV,"2014")
    plot(data)

if __name__ == "__main__":
    main()




