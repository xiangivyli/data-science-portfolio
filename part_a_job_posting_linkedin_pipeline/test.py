import os
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.empty import EmptyOperator
from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator
from airflow.operators.python import PythonOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime
import glob
from pathlib import Path

CURRENT_DIR = os.getcwd()

# Downloaded and Converted Datasets
dir_raw_data = f"{CURRENT_DIR}/airflow/include/dataset/2024-03-31/raw/linkedin-job-postings"
dir_parquet_data = f"{CURRENT_DIR}/airflow/include/dataset/2024-03-31/parquet/"

#List all CSV files and table names
csv_files = glob.glob(f"{dir_raw_data}/**/*.csv", recursive=True)
table_names = [Path(file_path).stem for file_path in csv_files]

# Google Cloud Storage
bucket = "de-zoomcamp-xiangivyli"
gcs_raw_folder = "final_project/2024-03-31/raw"
parquet_folder = "final_project/2024-03-31/parquet"


    # Get src path for each file
for raw_file_path, table in zip(csv_files, table_names):
    # Generated destination for each file
    dst_raw_path = f"{gcs_raw_folder}/{table}.csv"
    print(dst_raw_path)
    task_id=f"upload_{table}_csv_to_gcs"
    print(task_id)


