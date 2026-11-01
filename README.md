# UN Population Analytics

## Aim
To transform raw population data into meaningful visualizations using Python and Matplotlib.

This project analyzes country-wise population estimates and presents insights through different types of bar charts.

## Data Sources
- [Population Dataset – GitHub](https://github.com/datasets/population/blob/main/data/population.csv)
- [ASEAN Countries – Wikipedia](https://en.wikipedia.org/wiki/ASEAN)
- [SAARC Countries – Wikipedia](https://en.wikipedia.org/wiki/South_Asian_Association_for_Regional_Cooperation)

## Visualizations

The project generates the following charts:

1. **India Population Over the Years** – Bar chart showing India's population trends over the years.
2. **ASEAN Population in 2014** – Bar chart comparing the population of ASEAN countries in 2014.
3. **Total SAARC Population Over the Years** – Bar chart showing the combined population of SAARC countries for each year.
4. **ASEAN Population (2004–2014)** – Grouped bar chart comparing the population of ASEAN countries across different years.

## Project Structure

```text
.
├── output/
│   ├── India_population_over_years.png
│   ├── output4.png
│   ├── population_of_ASEAN_countries.png
│   └── total_population_of_SAARC_countries.png
├── requirements.txt
├── resources/
│   ├── asia.csv
│   └── population.csv
├── README.md
└── src/
    ├── asian_countries_population.py
    ├── group_asian_countries.py
    ├── indian_population_analysis.py
    └── saarc_countries_analysis.py
```

## Technologies Used
- Python
- Matplotlib
- CSV

## Installation and Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd un-population-analytics
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
```

### 3. Activate the virtual environment

**Linux / macOS**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the analysis

Run the required analysis scripts from the project root directory.

```bash
python src/indian_population_analysis.py
python src/asian_countries_population.py
python src/saarc_countries_analysis.py
python src/group_asian_countries.py
```

## Output

All generated charts are saved in the `output/` directory.

These visualizations help compare population trends across India, ASEAN, and SAARC countries.

## License

This project is developed for learning and data visualization practice.