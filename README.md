# Data Science Projects Portfolio

This portfolio holds the below projects. 

Each project has a **folder** in this repository or **another repository** (for easy execution) for data, codes, and key takeaways. 
Some projects may cover multiple technical aspects, like data dashboarding containing the data engineering process.
# Table of Contents

## Part A Data Engineering

### [Job Postings on Linkedin](https://github.com/xiangivyli/data-science-portfolio/tree/main/part_a_job_posting_linkedin_pipeline)

Tools:
 - Python with Jupyter Notebook
 - Data Transformation: dbt
 - Data Loading: Airflow (Astro Cli)
 - Data Visualisation: Power BI
 - Data Quality Testing: Soda
 - Data Lake: Google Cloud Storage
 - Data Warehouse: BigQuery
 - Data Orchestration: Airflow

Objectives:
   - extract raw data from Kaggle, and process data for a read-to-use dataset
   - reduce file size and identify schema by using parquet files
   - achieve automation and monitorization with Airflow and dbt
   - visualize data for insights with Power BI

### [PM2.5-Monitoring](https://github.com/xiangivyli/pm25_monitoring)

Tools:
 - Data Extraction, Transformation, Validation: API, Python
 - Data Orchestration: **Airflow**
 - Database: **DuckDB**
 - Data Reporting： **Streamlit**
 - Containerization: **Docker Compose**

Objectives:
   - Ingest pm2.5 data into DuckDB daily
   - Transformation is triggered by data ingestion in Airflow
   - Streamlit container keeps running and monitors the pm2.5 data in real-time 

### [Data Platform Design for Healthcare Research (Database)](https://xiangivyli.com/blog/data-platform-design-for-healthcare-research-mysql/)
 
Tool: MySQL
 
Objectives:
   - identify how diseases begin and progress
   - integration of genetics and healthcare data
   - research-ready, well-curated and well-documented data

### [Nomalisation (SQL Server)](https://xiangivyli.com/blog/normalisation-for-professors-in-organisations-with-sql-server/)

Tool: SQL Server

Objectives:
  - Split a table into a fact table and dimension tables
  - Set datatype, primary key, foreign key and referential integrity

## Part B Exploratory Data Analysis and Data Modelling

### [ESG analysis for Pfizer (Exploratory Data Analysis and Linear Regression)](https://xiangivyli.com/blog/esg-pfizer/)

Tool: Python

Objectives:
  - identify Pfizer company's position in the pharmaceutical industry
  - visualise the development of Pfizer from 2016 to 2018
  - linear regression between ESG score and total assets
 
### [BT Customer Churn Prediction (Python and Power BI)](https://xiangivyli.com/blog/bt-customer-churn-prediction/)
 
Tool: Python and Power BI

Objectives:
   - build a logistic regression model 
   - identify which feature will influence customer churn

### [Revenue increase strategy analysis for Google merchandise store (Business Intelligence)](https://xiangivyli.com/blog/revenue-google-store/)

Tool: Google Analytics

Objectives:
  - map the persona of customers
  - identify the performance of products
  - identify the pattern of activity
  - the funnel diagrams shows the buyer's journey

## Part C Data Visualization and Dashboarding

### [Lloyds Bank Customer Profiling (Business Intelligence)](https://github.com/xiangivyli/data-science-portfolio/tree/main/part_c_lloyds_bank_customer_profiling)
 
Tool: Power BI

Objectives:
  - map the persona of customers 
  - analysis the features of customers based on the loan status variable

### [Education-Focused Analysis (Power BI and Python)](https://xiangivyli.com/blog/education-focused-analysis-assessment-types-final-results)

Tool: Python and Power BI

Objectives:
  - Prepare a cleansed dataset for analysis
  - A logical story to explain why the mix and weighting of assessment types changed the final result

### [A self-service platform for GDP, Life Satisfaction and Education Level](https://xiangivyli.com/blog/an-information-retrieval-platform-for-gdp-satisfaction-education/)

Tool: Tableau

Objectives:
  - Provide users a platform to retrieve information about **GDP**, **Life Satisfaction**, and **Education Level** for countries in different year
  - Give a general idea about this information for regions
  - Check the relationship between **education level** and **GDP per capita**
 
