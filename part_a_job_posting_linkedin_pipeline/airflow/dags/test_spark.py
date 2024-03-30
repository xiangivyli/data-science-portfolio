from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime


# Define your DAG
with DAG(
    'test',
    start_date=datetime(2024, 3, 30),
    schedule_interval=None,
    catchup=False,
    tags=['test'],
) as dag:
    
    # Define the Spark job submission task
    submit_job=SparkSubmitOperator(
        task_id='submit_job',
        application='/usr/local/airflow/include/test_spark_local.py',
        conn_id='spark_default',
        total_executor_cores='1',
        executor_cores='1',
        executor_memory='2g',
        num_executors='1',
        driver_memory='2g',
        verbose=False,
        env_vars={'PATH': '/bin:/usr/bin:/usr/local/bin'}
    )
