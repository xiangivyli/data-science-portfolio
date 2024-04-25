# Job Posting on Linkedin DataSet Pipeline

# Table of Contents
1. [Chapter 1 - Project Overview](#ch1)
2. [Chapter 2 - Data Extraction](#ch2)
3. [Chapter 3 - Data Preparation with Airflow](#ch3)
4. [Chapter 4 - Data Quality Check](#ch4)
5. [Chapter 5 - Data Transformation with dbt](#ch5)
6. [Chapter 6 - Data Visualisation](#ch6)
7. [Chapter 7 - Future Work](#ch7)



<a id = "ch1"></a>
## Chapter 1 Project Overview

The project is inspired by my interest: I would like to understand the job market, the whole process includes 

Data Source: [LinkedIn Job Postings - 2023](https://www.kaggle.com/datasets/arshkon/linkedin-job-postings/data)

>This dataset contains a nearly comprehensive record of 33,000+ job postings listed over the course of 2 days, months apart. Each individual posting contains 27 valuable attributes, including the title, job description, salary, location, application URL, and work-types (remote, contract, etc), in addition to separate files containing the benefits, skills, and industries associated with each posting.

The workflow is:

 0. Download csv data from Kaggle public dataset with opendatasets and Prepare dataset summary table for review (size, number of records)
 1. Upload raw data to Google Cloud Storage with **Airflow**
 2. Define schema and repartition to parquet file with **PySpark** and **Airflow**
 3. Upload parquet data to Google Cloud Storage with **Airflow**
 4. Create tables in **BigQuery**
 5. Transform and aggregate data with **dbt**
 6. Visualise data with **PowerBI**

#### Infrastructure
Used Techniques are:
 - Data Extraction: Python with [Jupyter notebook](https://jupyter.org/)
 - Data Transformation: [dbt](https://www.getdbt.com/product/what-is-dbt)
 - Data Loading: Airflow ([Astro Cli](https://docs.astronomer.io/astro/cli/overview))
 - Data Visualisation: [Power BI](https://www.microsoft.com/en-us/power-platform/products/power-bi)
 - Data Quality Testing: [Great Expectations](https://greatexpectations.io/)

 - Data Lake: [Google Cloud Storage](https://cloud.google.com/storage?hl=en)
 - Data Warehouse: [BigQuery](https://cloud.google.com/bigquery/docs/introduction)

 - Containerization: Astro Cli (Docker Compose)
 - Data Orchestration: [Airflow](https://airflow.apache.org/)


The work flow is shown below:
<p align = "center">
  <img src="./image/technology_summary.png">
  </p>


<a id = "ch2"></a>
 ## Chapter 2 Data Extraction
 
 With a jupyter notebook named [0_download_explore_data.ipynb](./0_download_explore_data.ipynb), I downloaded the raw data to my Airflow dataset (it is ignored in .gitignore considering space).

 The strucuture is <p align = "center">
  <img src="./image/1_tree.png">
  </p>
 The size information is <p align = "center">
  <img src="./image/2_size.png">
  </p>
 The number of records information is <p align = "center">
  <img src="./image/3_records.png">
  </p>

I also use Power BI to draw the relationship among these tables, the data modelling is <p align = "center">
  <img src="./image/4_data_modelling.png">
  </p>

<a id = "ch3"></a>
# Chapter 3 Data Preparation with Airflow

Airflow controls the whole process for data preparation, it includes:
1. Backup **raw** files in **Google Cloud Storage** with [GCSHook](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/hooks/gcs/index.html) and [PythonOperator](https://airflow.apache.org/docs/apache-airflow/stable/howto/operator/python.html)
2. Repartition and convert raw to **parquet files** with [SparkSubmitOperator](https://registry.astronomer.io/providers/apache-airflow-providers-apache-spark/versions/4.7.1/modules/SparkSubmitHook) and a [python script](./airflow/include/spark_repartition_parquet.py) file
3. Upload **parquet** files to **Google Cloud Storage** with GCSHook and PythonOperator
4. Create an **empty dataset** in **BigQuery** with [BigQueryCreateEmptyDatasetOperator](https://registry.astronomer.io/providers/google/versions/latest/modules/bigquerycreateemptydatasetoperator)
5. Import **parquet data from Google Cloud Storage to BigQuery** with [astro-sdk-python](https://docs.astronomer.io/learn/astro-python-sdk-etl)

The dag file is [in the airflow/dags subfolder](./airflow/dags/data_ingest_gcs.py), the spark script is [in the airflow/include subfolder](./airflow/include/spark_repartition_parquet.py)

The Graph is <p align = "center">
  <img src="./image/5_data_preparation.png">
  </p>

<a id = "ch4"></a>
# Chapter 4 Data Quality Check with Great Expectation

## Pre-requisites
`requirements.txt` file: `airflow-provider-great-expectations==0.2.7`
`packages.txt` file: `libgeos-c1v5`

## Run test in DAG

Use `airflow-provider-great-expectations` package in Airflow.

Add `json` file corresponding to each table in `include/gx/expectations` folder to list desired checks

The test focus before transformation are the correct total account, the schema

And the check passed as shown below


<a id = "ch5"></a>
# Chapter 5 Data Transformation with dbt

Purposes are:
dim_company model:
  - **employee_count** removes duplicate records for same `company_id`
  - join **employee_count** to **company**: add `employee_count` and `follower_count` information

dim_skill model:
  - join **skills_name** to **job_skills**: replace `skill_abr` with full name

dim_industry model:
  - join **industry** to **job_industry**: replace `industry_id` with full name

fact_job_posting model:
 - keep **job_postings** columns that need in the data visualisation

aggre_job_posting_model:
 - put company_info, industry and skills to the fact table **job_postings**

The method is to use [cosmos](https://www.astronomer.io/cosmos/) combine dbt in the airflow, the dags are connected by dataset, once the upstream dag (i.e., load data in the bigquery), the updated dataset triggers this dag.

The dag dependencies is <p align = "center">
  <img src="./image/7_dag_dependencies.png">
  </p>

The dataset trigger label is <p align = "center">
  <img src="./image/7_dataset_trigger.png">
  </p>


The lineage graph is <p align = "center">
  <img src="./image/7_dag2_dbt_transform_bigquery.png">
  </p>



<a id = "ch6"></a>
# Chapter 6 Data Visualisation

Before the data visualisation even before the data engineering project, I want to answer several questions:
1. Which industry has more job openings
2. How about the salary range
3. Which city has more opportunities

Considering the dataset mainly covered the US job market, it is meaningful to find some trends.

The data visualisation can answer my questions well:
1. Healthcare and IT are still popular
2. Around 200K dollars
3. New York is attractive
   
<p align = "center">
  <img src="./image/8_data_viz.png">
  </p>

<a id = "ch7"></a>
# Chapter 7 Future Work

1. Write test functions
3. Add Terraform 


