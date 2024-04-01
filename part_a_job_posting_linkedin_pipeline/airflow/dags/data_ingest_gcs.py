import os
import glob
from pathlib import Path

from airflow.decorators import dag, task
from datetime import datetime
from airflow.utils.dates import days_ago

from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator
from airflow.providers.google.cloud.hooks.gcs import GCSHook
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.operators.python import PythonOperator
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
local_parquet_folders = glob.glob(f"{local_parquet}pq_{table_names}/")

# Google Cloud Storage
bucket = "de-zoomcamp-xiangivyli"
gcs_raw_folder = "final_project/2024-03-31/raw/"
gcs_parquet_folder = "final_project/2024-03-31/parquet/"

# Define a function to upload csv files
def upload_csv_to_gcs(bucket, local_folder, gcs_folder):
    gcs_hook = GCSHook(gcp_conn_id="google_cloud_default")
    local_folder_path = Path(local_folder)

    # Loop through all files in the directory and subdirectories
    for local_file in local_folder_path.rglob('*.csv'):
        if local_file.is_file():
            # Generate the relative path to maintain the directory structure
            relative_path = local_file.relative_to(local_folder_path)

            # Create the full GCS path for the file
            gcs_path = f"{gcs_folder}{relative_path}"

            # Upload the file
            gcs_hook.upload(bucket_name=bucket, 
                            object_name=gcs_path, 
                            filename=str(local_file))


# Define a function to upload parquet folders
def upload_directory_to_gcs(bucket, local_folder, gcs_folder):
    gcs_hook = GCSHook(gcp_conn_id="google_cloud_default")
    local_folder_path = Path(local_folder)

    # Loop through all files in the directory and subdirectories
    for local_file in local_folder_path.rglob('*.parquet'):
        if local_file.is_file():
            # Generate the relative path to maintain the directory structure
            relative_path = local_file.relative_to(local_folder_path)

            # Create the full GCS path for the file
            gcs_path = f"{gcs_folder}{relative_path}"

            # Upload the file
            gcs_hook.upload(bucket_name=bucket, 
                            object_name=gcs_path, 
                            filename=str(local_file))


@dag(
    start_date=days_ago(1),
    schedule=None,
    catchup=False,
    tags=["raw_parquet_spark_gcs"],
)
def raw_parquet_to_gcs():

    # task1 upload raw files to gcs for backup
    upload_raw_tasks=PythonOperator(
        task_id='upload_raw_to_gcs',
        python_callable=upload_csv_to_gcs,
        op_kwargs={'bucket': bucket,
                   'local_folder': local_raw,
                   'gcs_folder': gcs_raw_folder}
    )

    # task2 spark read and repartition to parquet files
    repartition_parquet = SparkSubmitOperator(
        task_id='repartition_parquet',
        application='/usr/local/airflow/include/spark_repartition_parquet.py', 
        conn_id='spark_default',
        total_executor_cores='1',
        executor_memory='2g',
        num_executors='1',
        driver_memory='2g',
        verbose=False,
        env_vars={'PATH': '/bin:/usr/bin:/usr/local/bin'}
    )

    # task3 upload parquet files in folder to gcs for usage
    upload_parquet_to_gcs_task = PythonOperator(
        task_id='upload_parquet_to_gcs',
        python_callable=upload_directory_to_gcs,
        op_kwargs={'bucket': bucket,
                   'local_folder': local_parquet,
                   'gcs_folder': gcs_parquet_folder}
    )

    chain(
        upload_raw_tasks,
        repartition_parquet,
        upload_parquet_to_gcs_task
    )

raw_parquet_to_gcs()
