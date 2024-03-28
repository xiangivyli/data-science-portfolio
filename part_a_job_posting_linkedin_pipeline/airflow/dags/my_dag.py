from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

with DAG("my_dag", start_date=datetime(2024, 3, 31),
         schedule_interval="@daily", catchup=False) as dag:
