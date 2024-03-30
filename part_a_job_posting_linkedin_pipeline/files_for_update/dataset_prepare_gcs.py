from airflow import DAG
from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime
import glob
from pathlib import Path

# Define your DAG
with DAG(
    'data_raw_parquet_gcs',
    start_date=datetime(2024, 3, 30),
    schedule_interval=None,
    catchup=False,
    tags=['raw_parquet_gcs'],
) as dag:

    # List all CSV files
    csv_files = glob.glob('/usr/local/airflow/include/dataset/**/*.csv', recursive=True)

    # Keep track of all the upload tasks
    upload_tasks = []
    
    # Iterate over each file and create a task for each one
    for file_path in csv_files:
        # Generate unique task_id
        task_id = f'upload_{Path(file_path).stem}_to_gcs'
        
        # Construct the destination path in GCS
        dst_path = f'final_project/raw/{Path(file_path).name}'

        # Create a task to upload the files to GCS
        upload_task = LocalFilesystemToGCSOperator(
            task_id=task_id,
            src=file_path,
            dst=dst_path,
            bucket='de-zoomcamp-xiangivyli',
            gcp_conn_id='gcp',
            mime_type='text/csv',
        )
        
        upload_tasks.append(upload_task)

    # Define the Spark job submission task
    submit_job = SparkSubmitOperator(
        task_id='submit_job',
        application='/include/pyspark_script.py', 
        conn_id='spark_default',
        total_executor_cores='1',
        executor_memory='2g',
        num_executors='1',
        driver_memory='2g',
        verbose=False
    )

    # Set dependencies: the Spark job should run after all upload tasks are complete
    for upload_task in upload_tasks:
        upload_tasks >> submit_job
