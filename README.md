# Global Health, Economy & Governance Dynamics  
## A Visual Exploration of Long-Term Development Patterns, 1960–2024

## Project Overview

This project explores how **economic growth**, **governance quality**, **corruption**, and **global crises** relate to long-term health outcomes across countries.

Using interactive Tableau dashboards, the project investigates whether wealth consistently translates into longer life expectancy, whether democratic and low-corruption institutions improve health outcomes, how regions have converged or diverged over time, and how major disruptions such as HIV/AIDS and COVID-19 affected global development.

The project began with a broad global development analysis in **Project 1** and was extended in **Project 2** using more advanced Tableau features such as:

- Parameter controls
- Table calculations
- Pages shelf animation
- Cross-filtering dashboards
- FIXED and INCLUDE Level of Detail expressions
- Interactive hypothesis testing

---

## Research Motivation

Global development is often simplified into one dominant story: richer countries live longer, democracies govern better, and corruption harms public welfare.

This project shows that the real pattern is more complicated.

Economic growth matters, but its effect on life expectancy weakens after countries reach middle- or high-income status. Democratic institutions are often associated with better health outcomes, but low corruption appears to be a more consistent predictor than elections alone. COVID-19 also challenged expectations by causing some of the sharpest life expectancy declines in wealthier and more urbanized countries.

The goal of this project is not only to present numbers, but to make complex global patterns visible, explorable, and interpretable through data visualization.

---

## Core Research Questions

### Project 1 Questions

1. Has economic growth consistently translated to longer lives?
2. Do democratic institutions improve health outcomes at similar income levels?
3. Are world regions converging or diverging in development?
4. Which countries achieved the greatest life expectancy gains, and what do they share?
5. How did major crises such as COVID-19 and HIV/AIDS affect different country groups?

### Project 2 Extension Questions

6. Does corruption kill? Do less corrupt countries achieve better health outcomes at every income level?
7. Which countries climbed the income ladder, and how has income class mobility related to health gains since 1987?
8. How did COVID-19 affect different regions and income groups? Which countries were hit hardest and which recovered fastest?

---

## Datasets Used

This project combines two major datasets.

### Dataset A: Health and Economic Indicators

Dataset A combines data from **Gapminder** and the **World Bank World Development Indicators**.

It includes country-year level information for approximately **236 countries** from **1960 to 2024**.

Key variables include:

- Country name
- ISO country code
- Year
- Life expectancy
- Male life expectancy
- Female life expectancy
- GDP per capita
- Population
- Region
- Income group
- Historical World Bank income class

This dataset is used to analyze long-term trends in health, wealth, population, regional development, and income mobility.

### Dataset B: Governance Indicators

Dataset B comes from the **Varieties of Democracy Project, V-Dem v16**.

It includes governance indicators for approximately **182 countries**.

Key variables include:

- Electoral Democracy Index
- Liberal Democracy Index
- Political Corruption Index
- Country name
- ISO country code
- Year

The governance data is used to analyze whether democracy, liberal institutions, and corruption are associated with better health outcomes.

---

## Data Integration

The two datasets were connected in Tableau using a relationship on:

```text
iso_code + year
```

A Tableau relationship was used instead of a physical join to preserve each dataset’s level of detail and avoid measure duplication.

This allowed the project to combine health, economic, and governance indicators while maintaining clean aggregation behavior in Tableau.

---

## Tools and Technologies

| Tool | Purpose |
|---|---|
| Tableau Prep | Data cleaning and preparation |
| Tableau Desktop | Dashboard building and visual analysis |
| Gapminder | Life expectancy, GDP, population |
| World Bank WDI | Income groups and economic indicators |
| V-Dem | Democracy and corruption indicators |
| Excel / CSV | Intermediate data storage |
| Tableau Calculated Fields | Derived metrics and analysis logic |
| Tableau Parameters | Interactive threshold testing |
| Tableau LOD Expressions | Fixed country-level calculations |
| Tableau Table Calculations | Year-over-year changes and percent totals |

---

## Key Visualizations

### 1. Life Expectancy by Country Map

This choropleth map shows global life expectancy by country for a selected year.

**Purpose:**  
To provide a geographic overview of health outcomes across the world.

**Variables:**

- Country
- Year
- Life expectancy
- GDP per capita in tooltip

**Main Finding:**  
The map reveals strong global improvement from 1960 to 2024, but also persistent regional inequality. Sub-Saharan Africa remains lighter than Europe, East Asia, and the Americas, indicating lower average life expectancy.

---

### 2. Life Expectancy by Region and Income Group

This grouped bar chart compares average life expectancy across world regions and income groups.

**Purpose:**  
To test whether regions are converging or diverging in health outcomes.

**Variables:**

- Region
- Income group
- Life expectancy
- Year

**Main Finding:**  
Higher-income groups generally have higher life expectancy within each region. However, the gap between income groups narrows over time, showing partial convergence in global health outcomes.

---

### 3. Male and Female Life Expectancy Trends

This line chart tracks male and female life expectancy from 1960 to 2024 across major world regions.

**Purpose:**  
To examine long-term health progress, gender gaps, and crisis effects.

**Variables:**

- Year
- Male life expectancy
- Female life expectancy
- Region

**Main Finding:**  
Women consistently outlive men across all regions. The chart also shows visible disruptions from HIV/AIDS in Africa and COVID-19 globally.

---

### 4. Top and Bottom Life Expectancy Gains

This table ranks countries by life expectancy percentage gain from 1960 to 2024.

**Purpose:**  
To identify which countries improved most and least over six decades.

**Main Finding:**  
Countries with the largest gains, such as China, Oman, Maldives, and Timor-Leste, started from very low life expectancy levels in 1960. Their improvement was not tied to one single governance model. Instead, the strongest shared pattern was low starting point and rapid development.

---

### 5. GDP per Capita vs Life Expectancy Bubble Chart

This Gapminder-inspired scatter plot shows the relationship between GDP per capita and life expectancy.

**Purpose:**  
To test whether economic growth buys longer lives.

**Variables:**

- GDP per capita
- Life expectancy
- Population
- Region
- Country

**Main Finding:**  
The relationship between GDP and life expectancy is strongly positive but nonlinear. Income gains produce large health improvements at low income levels, but after a certain point, additional wealth produces smaller gains. This is consistent with the Preston Curve idea of diminishing returns.

---

### 6. Democracy, Governance, and Health Heatmap

This heatmap compares top life expectancy countries with democracy, liberal democracy, and corruption indicators.

**Purpose:**  
To examine whether democratic institutions are associated with better health outcomes.

**Variables:**

- Life expectancy
- Electoral Democracy Index
- Liberal Democracy Index
- Political Corruption Index
- Region
- Year

**Main Finding:**  
Many high-life-expectancy countries have strong democracy scores, but some exceptions, such as Singapore and Hong Kong, show that democracy alone does not explain health outcomes. Low corruption appears to be a more consistent pattern among high-performing countries.

---

## Project 2 Extensions

### 7. COVID Impact Map

This animated map shows year-over-year life expectancy change by country.

**Purpose:**  
To visualize the geographic spread and recovery pattern of COVID-19’s impact on life expectancy.

**Tableau Feature Used:**

```text
Pages shelf animation
```

**Calculation:**

```text
AVG([Life Expectancy]) - LOOKUP(AVG([Life Expectancy]), -1)
```

**Main Finding:**  
From 2019 to 2020, many countries shifted sharply into negative life expectancy change. The Americas, Europe, and Central Asia showed some of the strongest declines. Recovery began unevenly across regions after 2021.

---

### 8. Corruption and Life Expectancy by Income Group

This grouped bar chart compares average life expectancy between high-corruption and low-corruption countries within income groups.

**Purpose:**  
To test whether less corrupt countries achieve better health outcomes at every income level.

**Tableau Feature Used:**

```text
Parameter control
```

**Corruption Classification Logic:**

```text
IF [V2X Corr] <= [Corruption Threshold]
THEN "Low Corruption"
ELSE "High Corruption"
END
```

**Main Finding:**  
The relationship between corruption and health is not simple. At stricter corruption thresholds, cleaner governments tend to show better health outcomes. But at moderate or lenient thresholds, the pattern changes, especially among poorer countries. This suggests that income level, disease burden, geography, aid, and state capacity may mediate the corruption-health relationship.

---

### 9. Corruption and Life Expectancy Scatter Plot

This scatter plot shows individual countries using corruption on the x-axis and life expectancy on the y-axis.

**Purpose:**  
To reveal country-level variation hidden by group averages.

**Variables:**

- Political corruption
- Life expectancy
- Income group
- Region
- Population

**Main Finding:**  
The overall relationship is negative: countries with higher corruption tend to have lower life expectancy. However, there is wide variation within income groups. Some moderately corrupt upper-middle-income countries still achieve relatively high life expectancy, while poor and highly corrupt countries often face compounding disadvantages.

---

### 10. COVID Dip Heatmap

This heatmap shows year-over-year life expectancy changes by region from 2015 to 2024.

**Purpose:**  
To compare regional pandemic impact and recovery timing.

**Main Finding:**  
Before COVID-19, most regions showed steady improvement. In 2020, all regions experienced declines, with the Americas and Europe among the hardest hit. Recovery patterns differed: some regions rebounded quickly, while others lagged.

---

### 11. Income Mobility Stacked Area Chart

This stacked area chart shows how the share of countries in each World Bank income class changed from 1987 to 2024.

**Purpose:**  
To examine global income class mobility over time.

**Tableau Feature Used:**

```text
Percent of Total table calculation
```

**Main Finding:**  
The share of low-income countries fell from about 30% in 1987 to about 12% in 2024. The share of high-income countries increased substantially. However, crises such as the 1997 Asian Financial Crisis and the 2008 Global Financial Crisis temporarily disrupted upward mobility.

---

### 12. COVID-19 Impact Rankings Table

This ranked table identifies the countries with the largest life expectancy decline from 2019 to 2020.

**Purpose:**  
To quantify which countries were hit hardest by COVID-19.

**Key Fields:**

- Country
- Region
- Income group
- Life expectancy in 2019
- Life expectancy in 2020
- Life expectancy in 2022
- COVID drop
- Recovery

**Main Finding:**  
The hardest-hit countries were not necessarily the poorest. Armenia, Ecuador, Bolivia, and Andorra experienced some of the steepest declines. Upper-middle-income countries and countries in Europe and the Americas were disproportionately represented among the hardest hit.

---

## Main Findings

### 1. Economic growth improves health, but with diminishing returns

GDP per capita is strongly associated with life expectancy, especially at low income levels. However, after countries reach middle- or high-income status, additional GDP produces smaller gains.

### 2. Democracy matters, but it is not the whole story

Many democratic countries achieve strong health outcomes, but wealthy non-democracies can also perform well. This suggests that governance effectiveness, state capacity, and institutional quality matter alongside electoral democracy.

### 3. Low corruption is a more consistent signal than democracy alone

Among high-life-expectancy countries, low corruption appears more consistent than high democracy scores. This suggests that corruption may affect public health through government effectiveness, service delivery, and institutional trust.

### 4. The largest life expectancy gains came from countries that started poorest

Countries such as China, Oman, Maldives, and Timor-Leste improved dramatically because they began from very low life expectancy levels in 1960. Their progress reflects catch-up growth and major improvements in public health, infrastructure, and economic development.

### 5. COVID-19 hit wealthier and more urbanized countries sharply

The COVID analysis revealed a counterintuitive result: many of the largest life expectancy drops occurred in upper-middle-income and high-income countries, especially in Europe and the Americas.

### 6. Global income mobility improved substantially

From 1987 to 2024, the share of low-income countries declined sharply, while the share of high-income countries increased. This indicates substantial global economic mobility, although financial crises temporarily slowed or reversed progress.

---

## Dashboard Design Principles

This project follows several major visualization design principles.

### Shneiderman’s Information-Seeking Mantra

```text
Overview first, zoom and filter, then details on demand
```

The dashboards provide:

- Global overview through maps
- Zooming through filters and parameters
- Details through tooltips and country-level tables

### Munzner’s Nested Model

The project applies Munzner’s visualization framework across four levels:

1. Domain problem: global development, health, governance, crisis impact
2. Data abstraction: country-year tabular data
3. Visual encoding: maps, bars, lines, scatter plots, heatmaps, tables
4. Algorithm/design choices: filters, parameters, LODs, table calculations, dashboards

### Channel Effectiveness

The project uses strong visual channels for quantitative comparison:

- Position for GDP and life expectancy
- Length for grouped bar charts
- Color luminance for choropleth maps and heatmaps
- Area for population in bubble charts
- Line position for temporal trends

---

## Repository Structure

A recommended repository structure is shown below.

```text
global-health-economy-governance/
│
├── README.md
│
├── data/
│   ├── raw/
│   │   ├── gapminder_life_expectancy.csv
│   │   ├── world_bank_indicators.csv
│   │   └── vdem_governance.csv
│   │
│   ├── processed/
│   │   ├── dataset_a_health_economy.csv
│   │   ├── dataset_b_governance.csv
│   │   └── tableau_ready_data.csv
│
├── tableau/
│   ├── project_1_workbook.twbx
│   ├── project_2_workbook.twbx
│   └── tableau_prep_flow.tflx
│
├── reports/
│   ├── project_1_report.pdf
│   └── project_2_report.pdf
│
├── images/
│   ├── project_1_dashboard.png
│   ├── project_2_dashboard.png
│   ├── covid_map.png
│   ├── corruption_bar_chart.png
│   ├── income_mobility_area_chart.png
│   └── covid_rankings_table.png
│
└── docs/
    ├── variable_dictionary.md
    └── methodology_notes.md
```

---

## How to Use This Project

### 1. Open the Tableau Workbook

Open the packaged Tableau workbook:

```text
tableau/project_2_workbook.twbx
```

The packaged workbook should include the data extract needed to view the dashboard.

### 2. Explore Project 1 Dashboard

Use the Project 1 dashboard to explore:

- Life expectancy by country
- GDP per capita vs life expectancy
- Democracy and governance comparisons
- Top and bottom life expectancy gainers

### 3. Explore Project 2 Dashboard

Use the Project 2 dashboard to explore:

- COVID life expectancy impact
- Corruption and health by income group
- Income class mobility
- Hardest-hit COVID countries

### 4. Use the Filters and Parameters

Important interactive controls include:

- Year filter
- Region filter
- Country filter
- Corruption threshold parameter
- Map cross-filtering
- Pages shelf animation for COVID analysis

---

## Key Tableau Calculations

### Year-over-Year Life Expectancy Change

```text
AVG([Life Expectancy]) - LOOKUP(AVG([Life Expectancy]), -1)
```

Used for COVID impact maps and heatmaps.

### Corruption Level Classification

```text
IF [V2X Corr] <= [Corruption Threshold]
THEN "Low Corruption"
ELSE "High Corruption"
END
```

Used to classify countries based on a user-adjustable corruption threshold.

### COVID Drop

```text
[Life Exp 2020] - [Life Exp 2019]
```

Used to quantify the decline in life expectancy during the first pandemic year.

### COVID Recovery

```text
[Life Exp 2022] - [Life Exp 2020]
```

Used to measure post-2020 recovery.

### Income Class Share

```text
Percent of Total
```

Used in the stacked area chart to show the share of countries in each income class over time.

---

## Limitations

This project has several important limitations.

1. The analysis is observational and does not prove causality.
2. Country-level analysis can hide within-country inequality.
3. Some small countries and territories have missing governance data.
4. V-Dem indicators involve expert-coded judgment.
5. GDP and life expectancy data come from multiple sources, which may introduce methodological differences.
6. Historical income class data is only available from 1987 onward.
7. COVID-era life expectancy changes may be affected by reporting differences across countries.

---

## Future Work

Future versions of this project could extend the analysis by:

- Adding healthcare spending per capita
- Adding education indicators
- Comparing inequality using Gini index
- Modeling the relationship statistically using regression
- Separating democracies, autocracies, and hybrid regimes
- Studying regional case studies in more depth
- Building a Python or Dash version of the dashboard
- Adding uncertainty intervals where data quality varies
- Including subnational data for large countries

---

## Project Contributors

### Tambudzai Charumbira

Contributed to data collection, Gapminder and World Bank preparation, Tableau Prep workflow, and dashboard development.

### Sayan Patra

Contributed to governance data integration, visual analysis, Tableau dashboard development, interpretation, and project reporting.

---

## Course Context

This project was completed for:

```text
DATS 6401: Visualization of Complex Data
Master of Science in Data Science
George Washington University
Spring 2026
```

---

## Conclusion

This project shows that global health progress is shaped by a combination of wealth, governance, corruption, regional context, and crisis exposure.

Economic growth improves life expectancy, but only up to a point. Democracy is associated with better health outcomes, but low corruption and institutional effectiveness appear especially important. The countries that improved most were often those that started poorest, while COVID-19 revealed that wealth alone does not guarantee resilience.

Through interactive visual analytics, the project turns decades of global development data into a structured visual story about progress, inequality, governance, and vulnerability.
