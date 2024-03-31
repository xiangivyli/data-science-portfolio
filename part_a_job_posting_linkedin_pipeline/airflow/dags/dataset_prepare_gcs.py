import os
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.empty import EmptyOperator
from airflow.providers.google.cloud.hooks.gcs import GCSHook
from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator
from airflow.operators.python import PythonOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime
import glob
from pathlib import Path
import logging


CURRENT_DIR = os.getcwd()

# Downloaded and Converted Datasets
dir_raw_data = f"{CURRENT_DIR}/airflow/include/dataset/2024-03-31/raw/linkedin-job-postings/"
dir_parquet_data = f"{CURRENT_DIR}/airflow/include/dataset/2024-03-31/parquet/"

#List all CSV files and table names
csv_files = glob.glob(f"{dir_raw_data}/**/*.csv", recursive=True)
table_names = [Path(file_path).stem for file_path in csv_files]

# Google Cloud Storage
bucket = "de-zoomcamp-xiangivyli"
gcs_raw_folder = "final_project/2024-03-31/raw/"
parquet_folder = "final_project/2024-03-31/parquet/"


def upload_raw_to_gcs(**kwargs):
    hook = GCSHook(gcp_conn_id="google_cloud_default")
    # Get src path for each file
    for raw_file_path, table in zip(csv_files, table_names):
        # Generated destination for each file
        dst_raw_path = f"{gcs_raw_folder}{table}.csv"

        logging.info(f"Uploading {raw_file_path} to {dst_raw_path} in bucket {bucket}")
        try:
            hook.upload(bucket_name=bucket, object_name=dst_raw_path, filename=raw_file_path)
            logging.info(f"Successfully uploaded {raw_file_path} to {dst_raw_path}")
        except Exception as e:
            logging.error(f"Failed to upload {raw_file_path} to {dst_raw_path}. Error: {e}")

# Define my DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
}      
with DAG(
    'data_parquet_gcs',
    default_args=default_args,
    description='A DAG to upload raw and parquet files to gcs with pyspark',
    schedule_interval=None,
    catchup=False,
    tags=['parquet_spark_gcs']
) as dag:
    start = EmptyOperator(task_id='start')
    end = EmptyOperator(task_id='end')
    
    # upload raw files to gcs
    upload_raw_to_gcs_task = PythonOperator(
        task_id="upload_raw_gcs",
        python_callable=upload_raw_to_gcs,
    )

    # Set dependencies: the Spark job should run after all upload tasks are complete
    start >> upload_raw_to_gcs_task >> end
