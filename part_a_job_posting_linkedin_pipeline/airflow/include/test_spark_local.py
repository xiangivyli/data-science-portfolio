import pyspark
from pyspark.sql import SparkSession
from pyspark.conf import SparkConf
from pyspark.context import SparkContext

from pyspark.sql.types import StructType, StructField, IntegerType, FloatType, StringType, TimestampType, DoubleType, LongType
from pyspark.sql.functions import col, from_unixtime, floor

def repartition_parquet_convert(input_path, output_path):
    """
    Read a CSV file from `input_path`, repartition then convert it to parquet file, and store it in GCS
    """

    # First, stop the existing Spark session if it's running
    if 'spark' in locals():
        spark.stop()


    # Create or get a Spark session
    spark = SparkSession.builder \
        .master("local[*]") \
        .appName("repartition_spark") \
        .getOrCreate()

    # Repartition and save it to parquet file in gcs
    # 1. define the schema
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
    # 2. read the dataset from the given path
    df_posting = spark.read \
        .option("header", "true") \
        .option("escape", "\"") \
        .option("multiline", "true") \
        .schema(job_postings_schema) \
        .csv(input_path)

     # 3. Define a list of your timestamp columns
    timestamp_columns = ["original_listed_time", "expiry", "closed_time", "listed_time"]

    # Convert from Unix time in milliseconds to a proper timestamp
    # Loop through the list and apply the transformation to each column
    for column_name in timestamp_columns:
        df_posting = df_posting.withColumn(
            column_name,
            (col(column_name) / 1000).cast("timestamp"))
        
    df_posting.repartition(10).write.parquet(output_path, mode="overwrite")
    
    # Stop the Spark session
    spark.stop()


if __name__ == "__main__":
    input_dataset_path ="/usr/local/airflow/include/dataset/raw/job_postings.csv"
    output_dataset_path = "/usr/local/airflow/include/dataset/parquet/job_postings/"


    repartition_parquet_convert(input_dataset_path, output_dataset_path)