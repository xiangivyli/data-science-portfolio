import os
import glob
from pathlib import Path
from typing import List

from airflow.decorators import dag, task
from datetime import datetime
from airflow.utils.dates import days_ago

from airflow.providers.google.cloud.operators.bigquery import BigQueryCreateEmptyDatasetOperator

from astro import sql as aql
from astro.files import File
from astro.sql.table import Table, Metadata
from astro.constants import FileType


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



def load_parquet_folders_to_bigquery(bucket: str, gcs_parquet_folder: str, table_names: List[str], conn_id: str = "google_cloud_default"):
    for table in table_names:
        # Construct the full path to the parquet folder for each table
        input_folder_path = f'gs://{bucket}/{gcs_parquet_folder}pq_{table}/'
        
        # Define the task to load data from GCS to BigQuery
        load_task = aql.load_file(
            task_id=f'load_{table}_to_bigquery',
            input_file=File(
                path=input_folder_path,
                conn_id=conn_id,
                filetype=FileType.PARQUET
            ),
            output_table=Table(
                name=table,
                conn_id=conn_id,
                metadata=Metadata(schema='test'), 
            ),
            use_native_support=False, 
        )

@dag(
    start_date=days_ago(1),
    schedule=None,
    catchup=False,
    tags=["test"],
)
def test():

    load_parquet_to_bigquery_task = load_parquet_folders_to_bigquery(
        bucket=bucket, 
        gcs_parquet_folder=gcs_parquet_folder,
        table_names=table_names,  
    )

test()

