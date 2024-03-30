from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
import glob
from pathlib import Path

# Define your DAG
with DAG(
    'test',
    start_date=datetime(2024, 3, 30),
    schedule_interval=None,
    catchup=False,
    tags=['test'],
) as dag:

    # Define the Spark job submission task
    submit_job = BashOperator(
        task_id='submit_job',
        bash_command="python /home/xiangivyli/data-science-portfolio/part_a_job_posting_linkedin_pipeline/airflow/include/pyspark_script.py",
        dag=dag,
        env={'PATH': '/bin:/usr/bin:/usr/local/bin'}
    )
