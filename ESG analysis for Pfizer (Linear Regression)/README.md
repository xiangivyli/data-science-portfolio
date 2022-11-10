<img src="./Images/Pfizer.jpg" align = "left" width = "500" height = "300" />
Pfizer is one of the biggest multinational biopharmaceutical companies and medicine suppliers with a robust research capacity (MarketLine, 2021). Its revenue dramatically increased to over 24 billion U.S dollars with the Covid-19 vaccine in the Third Quarter of 2021(Statista, 2021). 

<img src="./Images/ESG.jpg" align = "right" width = "500" height = "400" />
Environmental, social and governance (ESG) score in today’s markets evaluates the sustainable effort of companies, representing the deduction of footprint and organising eco-friendly activities, maintaining the relationship with humans, and testing the transparency of management structure. 

# Table of Contents
1. [Chapter 1 - Project Overview](#ch1)
1. [Chapter 2 - Data Cleansing](#ch2)
1. [Chapter 3 - Descriptive Analysis](#ch3)
1. [Chapter 4 - Linear Regression](#ch4)
1. [Chapter 5 - Model Validation](#ch5)
1. [Chapter 5 - Discussion](#ch6)

1. [References](#ch90)

<a id = "ch1"></a>
## Project Overview
### Objects

This empirical analysis has two objectives.

Firstly, it attempts to identify Pfizer company’s position in the pharmaceutical industry and then visualise the trend of business aspects in Pfizer from 2016 to 2018. 

Secondly, given that the ESG scores (Environmental, Social, Governance Scores) have triggered a wider concern of the company's corporate social responsibility. The analysis applied linear regression to disclose the relationship between total assets and ESG scores.

### Brief

The process includes data cleansing, modelling, visualisation, and combining statistics to detect the rationality of the equation. 

The project shows that Pfizer has a strong foundation, including tremendous assets and sufficient employees; conversely, it is on a middle-level of the biopharmaceutical companies regarding return on assets and Tobin’s Q ratio, which means Pfizer needs to focus on arousing development potential. Moreover, the regression model indicates that the ESG score can efficiently promote total assets; the relationship is that total assets increase by e<sup>5.2366</sup> million U.S. dollars when environmental and governance disclosure scores increase by one unit. 

### Dataset

The dataset and corresponding dictionary can be found in the Data folder.
The dataset contains all S&P 1500 companies listed in the US stock market over three years 2016 - 2018.

### Features for each company:

- Ticker
- Name
- Year
- ISIN Number
- SIC Code
- GICS Industry
- Country or Territory of Domicile
- Number of Employees
- Total Assets
- R&D Expense
- R&D Expense Adjusted
- Operating Expenses R&D
- Cash and Cash Equivalients
- Environmental Disclosure Score
- Social Disclosure Score
- Social Disclosure Score
- Governance Disclosure Score
- Tobin's Q Ratio
- Return on Assets
- Return on Common Equity
- Gross Margin

<a id = "ch2"></a>
## Data Cleansing
### Import data
```
# Importing all livraries that I will use
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.formula.api import ols

# Creating a dataframe and importing data
df = pd.read_csv("./S&P1500_Raw Dataset_Data Analytics in Business Assignment_2021.csv")
df.count()
```

Data is the U.S. stock market S&P 1500 firms’ dataset from 2016 to 2018, covering 326 industries. The data includes 4518 rows and 20 variables.
[Dictionary](#Dictionary) in [Data](#Data) explains the variables’ definitions.

Three data frames
1. Biopharmaceutical companies: show the difference between Pfizer and other companies in the industry

2. Pfizer from 2016 to 2018: show the development trends

3. All data: establish a regression model (Total asset & ESG)


## Descriptive Analysis
- Count the number of companies
- Depict the locations of Pharmaceuticals in the world
- Find companies in Ireland
- Check the location of Pfizer 
- Compare total assets, employees, return on assets and Tobin's Q Ratio among Pharmaceuticals
- Describe the developing trend of Pfizer (assets, employees and so on)

## Predictive Analysis
- Lag ESG scores as the delayed impact 
- Delete outliers
- Log total assets
- Regression 
- Residual plot 
- Histogram plot
- Test multicollinearity


