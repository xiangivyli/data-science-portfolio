import os
import glob
from pathlib import Path
from typing import List

from airflow.decorators import dag, task
from datetime import datetime
from airflow.utils.dates import days_ago

from airflow.providers.google.cloud.operators.bigquery import BigQueryCreateEmptyDatasetOperator
from airflow.operators.python import PythonOperator

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


@dag(
    start_date=days_ago(1),
    schedule=None,
    catchup=False,
    tags=["test"],
)
def test():
        
        input_folder_path = f'gs://{bucket}/{gcs_parquet_folder}pq_salaries/'


        aql.load_file(
            task_id='load_salaries_to_bigquery',
            input_file=File(
                path=input_folder_path,
                conn_id="google_cloud_default",
                filetype=FileType.PARQUET,
            ),
            output_table=Table(
                name='salaries',
                conn_id="google_cloud_default",
                metadata=Metadata(schema="job_postings_project"),
            ),
            use_native_support=False,
        )

test()

