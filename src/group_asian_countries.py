import csv
from datetime import datetime
from matplotlib import pyplot as plt

POPULATION_CSV = "resources/population.csv"

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

def compute_group_asean_population_by_year(path : str):
    asean_population_by_year = {}
    with open(path,'r',encoding="utf-8") as population_csv:
        populations = csv.DictReader(population_csv)
        for population in populations:
            country = population.get("Country Name")
            year_str = population.get("Year")
            value = population.get("Value")
            if not country or not year_str or not value:
                continue
            year = int(year_str)
            if country in southeast_asian_countries and 2004 <= year <=2014:
                if year not in asean_population_by_year:
                    asean_population_by_year[year] = {}
                asean_population_by_year[year][country] = int(value)

    return asean_population_by_year

def plot_group_by_year(data: dict[int, dict[str, int]]):

    sorted_data = sorted(data.items())
    years = [year for year, _ in sorted_data]

    shift = 0
    width = 0.15
    gap = 0.25

    positions = []
    labeled = set()

    plt.figure(figsize=(14, 6))

    for year in years:

        for j, (name, value) in enumerate(data[year].items()):

            label = name if name not in labeled else None

            plt.bar(
                shift + j * width,
                value,
                width=width,
                label=label
            )

            labeled.add(name)

        count = len(data[year])

        positions.append(shift + (count * width) / 2)

        shift += count * width + gap

    plt.xticks(positions, years)

    plt.title("Population by Year")
    plt.xlabel("Year")
    plt.ylabel("Population")

    plt.legend()
    plt.tight_layout()
    plt.show()


def main():
    data = compute_group_asean_population_by_year(POPULATION_CSV)
    plot_group_by_year(data)

if __name__ == "__main__":
  main()














