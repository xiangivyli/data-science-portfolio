from airflow import DAG 
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime

with DAG('sppark_submit_job',
        start_date=datetime(2024, 3, 29),
        schedule_interval='@daily') as dag:
    
    submit_job = SparkSubmitOperator(
        task_id='submit_job',
        application='/include/pyspark_script.py', #/path/to/my/pyspark_script.py
        conn_id='spark_default',
        total_executor_cores='1',
        executor_memory='2g',
        num_executors='1',
        driver_memory='2g',
        verbose=False
    )
