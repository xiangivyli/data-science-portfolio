import os
import glob
from pathlib import Path

from airflow import Dataset
from airflow.decorators import dag, task_group
from airflow.utils.dates import days_ago

from airflow.operators.empty import EmptyOperator
from airflow.providers.google.cloud.hooks.gcs import GCSHook
from airflow.providers.google.cloud.operators.bigquery import BigQueryCreateEmptyDatasetOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.operators.python import PythonOperator

from astro import sql as aql
from astro.files import File
from astro.sql.table import Table, Metadata
from astro.constants import FileType

from airflow.providers.common.sql.operators.sql import (
    SQLColumnCheckOperator,
    SQLTableCheckOperator,
    SQLCheckOperator,
)

from airflow.models.baseoperator import chain
"""
Prepare all paths
"""
CURRENT_DIR = os.getcwd()

DB_CONN = "google_cloud_default"

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
    default_args={"conn_id": DB_CONN},
)
def raw_parquet_to_gcs_bigquery():

    start = EmptyOperator(task_id="start")
    end = EmptyOperator(task_id="end")

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

    # task4 create an empty dataset in Bigquery
    create_dataset_tasks = BigQueryCreateEmptyDatasetOperator(
        task_id="create_dataset_bigquery",
        dataset_id="job_postings_project",
        gcp_conn_id="google_cloud_default",
    )

    # task5 import data from gcs to bigquery
    @task_group(group_id="import_tables")
    def import_data_gcs_to_bigquery_tasks():
    
        import_data_gcs_to_bigquery_tasks = []

        for table in table_names:
            dataset = Dataset(f"{table}_dataset")

            input_folder_path = f'gs://{bucket}/{gcs_parquet_folder}pq_{table}/'

            task = aql.load_file(
                task_id=f'load_{table}_to_bigquery',
                input_file=File(
                    path=input_folder_path,
                    conn_id="google_cloud_default",
                    filetype=FileType.PARQUET,
                ),
                output_table=Table(
                    name=table,
                    conn_id="google_cloud_default",
                    metadata=Metadata(schema="job_postings_project"),
                ),
                use_native_support=False,
                outlets=[dataset]
            )

            import_data_gcs_to_bigquery_tasks.append(task)

    # task6 make sure the records keep the same with raw file
    @task_group(group_id="tables_check")
    def number_of_records_check():
        
        number_of_records_check = []

        count_dic = {
            "job_postings" : 33246,
            "skills" : 35,
            "industries" : 229,
            "employee_counts" : 14275,
            "companies" : 11361,
            "company_specialities" : 78405,
            "company_industries" : 12601,
            "job_industries" : 44091,
            "job_skills":56591,
            "benefits":29325,
            "salaries": 13352
        }

        for table, expected_count in count_dic.items():
            check_statement = f"COUNT(*) == {expected_count}"
            task = SQLTableCheckOperator(
                task_id=f'{table}_table_check_bigquery',
                table=table,
                checks={
                    "my_row_count_check": {"check_statement": check_statement}
                }
            )

            number_of_records_check.append(task)


    chain(
        start,
        upload_raw_tasks,
        repartition_parquet,
        upload_parquet_to_gcs_task,
        create_dataset_tasks,
        import_data_gcs_to_bigquery_tasks(),
        number_of_records_check(),
        end,
    )
    

raw_parquet_to_gcs_bigquery()

