from airflow import DAG
from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime

# Define your DAG
with DAG(
    'data_parquet_gcs',
    start_date=datetime(2024, 3, 30),
    schedule_interval=None,
    catchup=False,
    tags=['raw_parquet_gcs'],
) as dag:

    # Define the Spark job submission task (repartition parquet locally)
    repartition_parquet = SparkSubmitOperator(
        task_id='repartition_parquet',
        application='/usr/local/airflow/include/test_spark_local.py', 
        conn_id='spark_default',
        total_executor_cores='1',
        executor_memory='2g',
        num_executors='1',
        driver_memory='2g',
        verbose=False,
        env_vars={'PATH': '/bin:/usr/bin:/usr/local/bin'}
    )

    # Create a task to upload the files to GCS
    upload_task = LocalFilesystemToGCSOperator(
        task_id='upload_raw_job_posting_to_gcs',
        src='/usr/local/airflow/include/dataset/parquet/job_postings/*.parquet',
        dst='final_project/parquet/job_postings/',
        bucket='de-zoomcamp-xiangivyli',
        gcp_conn_id='gcp',
        mime_type='text/csv',
        )
    
    # Set dependencies: the Spark job should run after all upload tasks are complete
    repartition_parquet >> upload_task
