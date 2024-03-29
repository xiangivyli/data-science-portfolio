from airflow.decorators import dag, task
from datetime import datetime
from airflow.operators.python import PythonOperator
from airflow.models import DAG
from google.cloud import storage
import glob
import os

def upload_files_to_gcs(bucket_name, src_directory, dst_directory, gcp_conn_id):
    """Uploads files from the local filesystem to GCS."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    
    for local_file in glob.glob(f'{src_directory}/**/*.csv', recursive=True):
        remote_path = os.path.join(dst_directory, os.path.relpath(local_file, start=src_directory))
        blob = bucket.blob(remote_path)
        blob.upload_from_filename(local_file)
        print(f"Uploaded {local_file} to {remote_path}.")

default_args = {
    'start_date': datetime(2024, 3, 29),
}

with DAG('csv_to_gcs', default_args=default_args, schedule_interval=None, catchup=False, tags=['step1_csv_to_gcs']) as dag:
    
    upload_task = PythonOperator(
        task_id='upload_all_csv_to_gcs',
        python_callable=upload_files_to_gcs,
        op_kwargs={
            'bucket_name': 'de-zoomcamp-xiangivyli',
            'src_directory': '/usr/local/airflow/include/dataset',
            'dst_directory': 'final_project/raw/',
            'gcp_conn_id': 'gcp', 
        }
    )
