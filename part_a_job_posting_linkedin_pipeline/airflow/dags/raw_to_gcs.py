from airflow.decorators import dag, task
from datetime import datetime

from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator

from pathlib import Path
import glob


@dag(
    start_date=datetime(2024, 3, 29),
    schedule=None,
    catchup=False,
    tags=['step1_csv_to_gcs'],
)

def csv_to_gcs():
    #list all CSV files
    csv_files = glob.glob('/usr/local/airflow/include/dataset/**/*.csv', recursive=True)
    

    for file_path in csv_files:
        # generate unique task id
        task_id=f'upload_{Path(file_path).stem}_to_gcs'

        #construct the destunation path in GCS
        dst_path = 'final_project/raw/' + Path(file_path).name

        #create a task to upload the files to GCS
        upload_to_gcs = LocalFilesystemToGCSOperator(
            task_id=task_id,
            src=file_path,
            dst=dst_path,
            bucket='de-zoomcamp-xiangivyli',
            gcp_conn_id='gcp',
            mime_type='text/csv',)
   
dag_instance = csv_to_gcs()