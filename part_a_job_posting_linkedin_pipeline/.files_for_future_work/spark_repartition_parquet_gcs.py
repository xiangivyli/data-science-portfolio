import os

import pyspark
from pyspark.sql import SparkSession
from pyspark.conf import SparkConf
from pyspark.context import SparkContext

from pyspark.sql.types import StructType, StructField, IntegerType, FloatType, StringType, TimestampType, DoubleType, LongType
from pyspark.sql.functions import col, from_unixtime, floor

"""
Prepare all paths
"""
CURRENT_DIR = os.getcwd()

#Dowloaded and Converted Datasets
local_raw = f"{CURRENT_DIR}/include/dataset/2024-03-31/raw/linkedin-job-postings/"
local_parquet = "gs://de-zoomcamp-xiangivyli/final_project/2024-03-31/parquet/"

credentials_location = f"{CURRENT_DIR}/include/.gc/google_credential_spark.json"
jars_location = f"{CURRENT_DIR}/include/lib/gcs-connector-hadoop3-latest.jar"

def repartition_parquet_convert():
    """
    Read a CSV file from `input_path`, repartition then convert it to parquet file
    """

    # First, stop the existing Spark session if it's running
    if 'spark' in locals():
        spark.stop()


    conf = SparkConf() \
        .setMaster('local[*]') \
        .setAppName('RepartitionApp') \
        .set("spark.jars", jars_location) \
        .set("spark.hadoop.google.cloud.auth.service.account.enable", "true") \
        .set("spark.hadoop.google.cloud.auth.service.account.json.keyfile", credentials_location)

    sc = SparkContext(conf=conf)

    hadoop_conf = sc._jsc.hadoopConfiguration()

    hadoop_conf.set("fs.AbstractFileSystem.gs.impl",  "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFS")
    hadoop_conf.set("fs.gs.impl", "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem")
    hadoop_conf.set("fs.gs.auth.service.account.json.keyfile", credentials_location)
    hadoop_conf.set("fs.gs.auth.service.account.enable", "true")
    
    # Create or get a Spark session
    spark = SparkSession.builder \
        .config(conf=sc.getConf()) \
        .getOrCreate()

    # Repartition and save it to parquet file in gcs
    # 1. job_postings.csv
    job_postings_schema = StructType([
        StructField("job_id", StringType(), True),
        StructField("company_id", StringType(), True),
        StructField("title", StringType(), True),
        StructField("description", StringType(), True),
        StructField("max_salary", FloatType(), True),
        StructField("med_salary", FloatType(), True),
        StructField("min_salary", FloatType(), True),
        StructField("pay_period", StringType(), True),
        StructField("formatted_work_type", StringType(), True),
        StructField("location", StringType(), True),
        StructField("applies", IntegerType(), True),
        StructField("original_listed_time", LongType(), True),
        StructField("remote_allowed", StringType(), True),
        StructField("views", IntegerType(), True),
        StructField("job_posting_url", StringType(), True),
        StructField("application_url", StringType(), True),
        StructField("application_type", StringType(), True),
        StructField("expiry", LongType(), True),
        StructField("closed_time", LongType(), True),
        StructField("formatted_experience_level", StringType(), True),
        StructField("skills_desc", StringType(), True),
        StructField("listed_time", LongType(), True),
        StructField("posting_domain", StringType(), True),
        StructField("sponsored", IntegerType(), True),
        StructField("work_type", StringType(), True),
        StructField("currency", StringType(), True),
        StructField("compensation_type", StringType(), True),
        StructField("scraped", IntegerType(), True)
    ])
    # read the dataset from the given path
    df_posting = spark.read \
        .option("header", "true") \
        .option("escape", "\"") \
        .option("multiline", "true") \
        .schema(job_postings_schema) \
        .csv(f"{local_raw}job_postings.csv")

     # Define a list of your timestamp columns
    timestamp_columns = ["original_listed_time", "expiry", "closed_time", "listed_time"]

    # Convert from Unix time in milliseconds to a proper timestamp
    # Loop through the list and apply the transformation to each column
    for column_name in timestamp_columns:
        df_posting = df_posting.withColumn(
            column_name,
            (col(column_name) / 1000).cast("timestamp"))
        
    df_posting.repartition(10).write.parquet(f"{local_parquet}pq_job_postings/", mode="overwrite")


    # 2. company_details/companies.csv
    companies_schema=StructType([
        StructField("company_id", StringType(), True), 
        StructField("name", StringType(), True),
        StructField("description", StringType(), True),
        StructField("company_size", IntegerType(), True),  
        StructField("state", StringType(), True),
        StructField("country", StringType(), True),
        StructField("city", StringType(), True),
        StructField("zip_code", StringType(), True), 
        StructField("address", StringType(), True),
        StructField("url", StringType(), True)
    ]) 
    
    df_companies = spark.read \
        .option("header", "true") \
        .schema(companies_schema) \
        .option("escape", "\"") \
        .option("multiline", "true") \
        .csv(f"{local_raw}company_details/companies.csv")
    
    df_companies.repartition(5).write.parquet(f"{local_parquet}pq_companies/", mode="overwrite")
    
    # 3. company_details/company_industries.csv
    company_industry_schema=StructType([
        StructField("company_id", StringType(), True), 
        StructField("industry", StringType(), True)
    ])


    df_company_industry = spark.read \
        .option("header", "true") \
        .schema(company_industry_schema) \
        .csv(f"{local_raw}company_details/company_industries.csv") 
    
    df_company_industry.repartition(2).write.parquet(f"{local_parquet}pq_company_industries/", mode="overwrite")
    
    # 4. company_details/employee_counts.csv
    employee_schema=StructType([
        StructField("company_id", StringType(), True),
        StructField("employee_count", IntegerType(), True),
        StructField("follower_count", IntegerType(), True),
        StructField("time_recorded", DoubleType(), True)
    ])

    df_employee_counts = spark.read \
        .schema(employee_schema) \
        .csv(f"{local_raw}company_details/employee_counts.csv", header=True)
    
    # Floor the 'time_recorded' column to remove decimal part, then cast to long
    df_employee_counts = df_employee_counts.withColumn(
        "time_recorded",
        floor(col("time_recorded")).cast("long")
    )

    # Now convert from Unix time in seconds to a proper timestamp
    df_employee_counts = df_employee_counts.withColumn(
        "time_recorded",
        from_unixtime(col("time_recorded")).cast("timestamp")
    )
    
    df_employee_counts.repartition(5).write.parquet(f"{local_parquet}pq_employee/", mode="overwrite")
    
    # 5. company_details/company_specialities.csv
    company_specialities_schema=StructType([
        StructField("company_id", StringType(), True),
        StructField("speciality", StringType(), True)
    ])

    df_company_specialities = spark.read \
        .schema(company_specialities_schema) \
        .csv(f"{local_raw}company_details/company_specialities.csv", header=True)
    
    df_company_specialities.repartition(5).write.parquet(f"{local_parquet}pq_company_specialities/", mode="overwrite")
    
    # 6. job_details/job_industries.csv
    df_job_industries = spark.read \
        .csv(f"{local_raw}job_details/job_industries.csv", header=True)
    
    df_job_industries.repartition(5).write.parquet(f"{local_parquet}pq_job_industries/", mode="overwrite")

    # 7. job_details/job_skills.csv
    df_job_skills = spark.read \
        .csv(f"{local_raw}job_details/job_skills.csv", header=True)

    df_job_skills.repartition(5).write.parquet(f"{local_parquet}pq_job_skills/", mode="overwrite")

    # 8. job_details/salaries.csv
    salary_schema = StructType([
        StructField("salary_id", StringType(), True),
        StructField("job_id", StringType(), True),
        StructField("max_salary", FloatType(), True),
        StructField("med_salary", FloatType(), True),
        StructField("min_salary", FloatType(), True),
        StructField("pay_period", StringType(), True),
        StructField("currency", StringType(), True),
        StructField("compensation_type", StringType(), True)
    ])


    df_salaries = spark.read \
        .schema(salary_schema) \
        .csv(f"{local_raw}job_details/salaries.csv", header=True)
    
    df_salaries.repartition(5).write.parquet(f"{local_parquet}pq_salaries/", mode="overwrite")

    # 9. job_details/benefits.csv
    benefit_schema = StructType([
        StructField("job_id", StringType(), True),
        StructField("inferred", StringType(), True),
        StructField("type", StringType(), True)
    ])    


    df_benefit = spark.read \
        .schema(benefit_schema) \
        .csv(f"{local_raw}job_details/benefits.csv", header=True)
    
    df_benefit.repartition(5).write.parquet(f"{local_parquet}pq_benefits/", mode="overwrite")

    # 10. map/industries.csv
    industry_schema = StructType([
        StructField("industry_id", StringType(), True),
        StructField("industry_name", StringType(), True)
    ])


    df_industry = spark.read \
        .schema(industry_schema) \
        .csv(f"{local_raw}maps/industries.csv", header=True)
    
    df_industry.write.parquet(f"{local_parquet}pq_industries/", mode="overwrite")

    # 11. maps/skills.csv
    skills_schema = StructType([
        StructField("skill_abr", StringType(), True),
        StructField("skill_name", StringType(), True)
    ])


    df_skills = spark.read \
        .schema(skills_schema) \
        .csv(f"{local_raw}maps/skills.csv", header=True)
    
    df_skills.write.parquet(f"{local_parquet}pq_skills/", mode="overwrite")

    # Stop the Spark session
    spark.stop()



repartition_parquet_convert()