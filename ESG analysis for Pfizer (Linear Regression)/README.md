<img src="./Images/Pfizer.jpg" align = "left" width = "500"/>
Pfizer is one of the biggest multinational biopharmaceutical companies and medicine suppliers with a robust research capacity (MarketLine, 2021). Its revenue dramatically increased to over 24 billion U.S dollars with the Covid-19 vaccine in the Third Quarter of 2021(Statista, 2021). 

<img src="./Images/ESG.jpg" align = "right" width = "500"/>
Environmental, social and governance (ESG) score in today’s markets evaluates the sustainable effort of companies, representing the deduction of footprint and organising eco-friendly activities, maintaining the relationship with humans, and testing the transparency of management structure. 

# Table of Contents
1. [Chapter 1 - Project Overview](#ch1)
1. [Chapter 2 - Data Gathering](#ch2)
1. [Chapter 3 - Biopharmaceutical Industry](#ch3)
1. [Chapter 4 - Development of Pfizer](#ch4)
1. [Chapter 5 - Relationship between total asset and ESG score](#ch5)
1. [Chapter 6 - Discussion](#ch6)

1. [References](#ch90)

<a id = "ch1"></a>
## Chapter 1 Project Overview
### Objects

This empirical analysis has two objectives.

- It attempts to identify Pfizer company’s position in the pharmaceutical industry and then visualise the trend of business aspects in Pfizer from 2016 to 2018. 

- Given that the ESG scores have triggered a wider concern of the company's corporate social responsibility. The analysis applied linear regression to disclose the relationship between total assets and ESG scores.

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
## Chapter 2 Data Gathering
### Import data
```
# Importing all libraries that I will use in the project
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
<img src="https://github.com/xiangivyli/Data-Science-Porfolio/blob/main/ESG%20analysis%20for%20Pfizer%20(Linear%20Regression)/Images/data.gathering.df.count.png" align = "left" width = "500"/>

```
# Checking the number of variables
df.shape[1]

#Checking how many industries are involved
len(df["SIC Code"}.unique())
```

Data covers 326 industries. The data includes 4518 rows and 20 variables. Most are quantitative results and collect financial information like total assets, return on assets, and so on; it also includes behaviour scores from external institutions like environmental disclosure score, social disclosure score and governance disclosure score.

[Dictionary](https://github.com/xiangivyli/Data-Science-Porfolio/blob/main/ESG%20analysis%20for%20Pfizer%20(Linear%20Regression)/Data/Dictionary.csv) in [Data](https://github.com/xiangivyli/Data-Science-Porfolio/blob/main/ESG%20analysis%20for%20Pfizer%20(Linear%20Regression)/Data/SP1500_Raw%20Dataset_Data%20Analytics%20in%20Business%20Assignment_2021.csv) explains the variables’ definitions.

<a id = "ch3"></a>
## Chapter 3 Biopharmaceutical Company
The chapter is to achieve the first objective - identify Pfizer's position in the pharmaceutical industry.

1. Using SIC Code of 2834 or 2836 to narrow down the range of companies (SIC Code 2843 - Pharmaceutical, SIC Code 2836 Biological Products).
2. Identify the analysis variables
    - name
    - year
    - country or territory of domicile
    - total assets
    - the number of employees
    - return in assets
    - R&D expense adjusted
    - environmental score
    - Tobin's Q ratio
    - return on assets
3. Drop NaN values to guarantee the rationality of results and figures
4. Calculate mean, median, maximum and minimum values 
5. Visulalise these metrics for comparison

Table 1 shows the descriptive statistics of biopharmaceutical companies with chosen variables and puts Pfizer's data aside to locate its performance level. There are 21 biopharmaceutical companies, like AbbVie, Amgen, and so on. Two companies are in Ireleand (Endo Internation PLC and Perrigo Co PLC), and the headquarters of 19 companies are in America.

Pfizer is an American corporation, and its headquarter locates in the U.S. as well. Pfizer is generally higher than the average level except for Tobin's Q ratio evaluation; the median value of the cohort is 7.33, while Pfizer only scored 1.94. The data of Pfizer is near teh maximum value in employees and total assets aspects.

<image src="https://github.com/xiangivyli/Data-Science-Porfolio/blob/main/ESG%20analysis%20for%20Pfizer%20(Linear%20Regression)/Images/biopharmaceutical.industry.landscape.table.png" align = "center"/>




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


