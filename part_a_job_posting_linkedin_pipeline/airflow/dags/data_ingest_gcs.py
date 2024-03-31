import os
import glob
from pathlib import Path

from airflow.decorators import dag, task
from datetime import datetime
from airflow.utils.dates import days_ago

from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator
from airflow.operators.empty import EmptyOperator

from airflow.models.baseoperator import chain
"""
Prepare all paths
"""
CURRENT_DIR = os.getcwd()

#Downloaded and Converted Datasets
local_raw = f"{CURRENT_DIR}/include/dataset/2024-03-31/raw/linkedin-job-postings/"
local_parquet = f"{CURRENT_DIR}/include/dataset/2024-03-31/parquet/"

#List all CSV files and table names
csv_files_path = glob.glob(f"{local_raw}/**/*.csv", recursive=True)
table_names = [Path(file_path).stem for file_path in csv_files_path]


# Google Cloud Storage
bucket = "de-zoomcamp-xiangivyli"
gcs_raw_folder = "final_project/2024-03-31/raw/"
parquet_folder = "final_project/2024-03-31/parquet/"


@dag(
    start_date=days_ago(1),
    schedule=None,
    catchup=False,
    tags=["raw_parquet_spark_gcs"],
)
def raw_parquet_to_gcs():
    upload_raw_tasks=[]

    for raw_file_path, table in zip(csv_files_path, table_names):
        task_id = f"upload_raw_{table}_to_gcs"

        dst_raw_path = f"{gcs_raw_folder}{table}.csv"
        upload_csv_to_gcs = LocalFilesystemToGCSOperator(
            task_id=f'upload_raw_{table}_to_gcs',
            src=raw_file_path,
            dst=dst_raw_path,
            bucket=bucket,
            gcp_conn_id="google_cloud_default",
            mime_type="text/csv",
        )

        upload_raw_tasks.append(upload_csv_to_gcs)

raw_parquet_to_gcs()

def repartition_parquet():
    