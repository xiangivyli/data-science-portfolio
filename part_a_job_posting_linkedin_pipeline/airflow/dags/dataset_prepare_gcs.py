import os
from airflow.decorators import dag, task
from datetime import datetime
from airflow.utils.dates import days_ago


from airflow.operators.empty import EmptyOperator
from airflow.providers.google.cloud.hooks.gcs import GCSHook
from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator
from airflow.operators.python import PythonOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

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

# Define my DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
}      
@dag(
    'data_parquet_gcs',
    default_args=default_args,
    description='A DAG to upload raw and parquet files to gcs with pyspark',
    schedule_interval=None,
    catchup=False,
    tags=['parquet_spark_gcs']
)

def upload_raw_to_gcs():    
    upload_raw_tasks = []
    
    for raw_file_path, table in zip(csv_files, table_names):
        task_id = f"upload_raw_{table}_to_gcs"

        dst_raw_path = f"{gcs_raw_folder}/{table}.csv"

        upload_raw_to_gcs = LocalFilesystemToGCSOperator(
            task_id=task_id,
            src=raw_file_path,
            dst=dst_raw_path,
            bucket=bucket,
            gcp_conn_id='gcp',
            mime_type='text/csv',
        )
        upload_raw_tasks.append(upload_raw_to_gcs)

upload_raw_to_gcs()
