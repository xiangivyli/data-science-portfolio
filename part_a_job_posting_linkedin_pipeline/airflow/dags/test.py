from airflow.decorators import dag, task
from datetime import datetime
from airflow.utils.dates import days_ago

from airflow.providers.google.cloud.operators.bigquery import BigQueryCreateEmpytyDataSetOperator

"""
Prepare all paths
"""

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

    create_dataset = BigQueryCreateEmpytyDataSetOperator(
        task_id="test",
        dataset_id="test",
        gcp_conn_id="gcp",
    )
test()

