
# Gapminder Project: Reproducible workflow with Pixi

## Task description
This project uses the Gapminder dataset to explore global development indicators like life expectancy, GDP per capita, and population.

The workflow includes:
- Data preprocessing
- Analysis by continent
- Visualization of results

## Setup Instructions

### 1. **Create a reproducible research using cookiecutter**: 

Check the GitHub repo to install cookiecutter and create a project - https://github.com/bios259/cookie-for-reproducible-research

Here is the command to start the project using cookiecutter.
```bash
cookiecutter gh:bios259/cookie-for-reproducible-research
```
### 2. **Copy necessary from this repo**:
Copy the necessary files from this repo to making the project as Pixi and add the scripts and data.

Check the `pixi.toml` file for more details.

### 3. **Install Pixi packages and run the Pixi tasks**:

- Install pixi dependencies after copying the pixi.toml:

```bash
pixi install
```
- Preprocess the data:

```bash
pixi run preprocess
```

- Analyze the data:
```bash
pixi run analyze
```

- Visualize the results:
```bash
pixi run visualize
```

### 4. **Run with Docker**:

Build and run the Docker container:
```bash
docker build -t gapminder-project .
docker run -v $(pwd):/app -it gapminder-project
```

## Results
- **Cleaned Data**:
`data/processed/cleaned_gapminder.csv`

- **Summary Table**:
`results/tables/continent_summary.csv`

- **Figures**:
  - Life Expectancy: `results/figures/life_expectancy_over_time.png`
  - GDP per Capita: `results/figures/gdp_per_capita_distribution.png`
