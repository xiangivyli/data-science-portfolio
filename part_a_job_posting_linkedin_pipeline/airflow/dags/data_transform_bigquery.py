from airflow.decorators import dag
from datetime import datetime
from airflow.utils.dates import days_ago
from airflow.datasets import Dataset

from include.dbt.cosmos_config import DBT_PROJECT_CONFIG, DBT_CONFIG
from cosmos.airflow.task_group import DbtTaskGroup
from cosmos.constants import LoadMode
from cosmos.config import  RenderConfig

from airflow.models.baseoperator import chain

job_postings_dataset = Dataset("job_postings_dataset")

companies_dataset = Dataset("companies_dataset") 
salaries_dataset = Dataset("salaries_dataset")

                              
job_skills_dataset = Dataset("job_skills_dataset")
skills_dataset = Dataset("skills_dataset")



@dag(
    start_date=days_ago(1),
    schedule=(job_postings_dataset | (companies_dataset) & (salaries_dataset) 
              | (job_skills_dataset) & (skills_dataset)),
    catchup=False,
    tags=["dbt_transform_data_in_bigquery"],
)
def transform_data_in_bigquery():

    # task1 dbt transforms data
    transform = DbtTaskGroup(
        group_id='transform',
        project_config=DBT_PROJECT_CONFIG,
        profile_config=DBT_CONFIG,
        render_config=RenderConfig(
            load_method=LoadMode.DBT_LS,
            select=['path:models/transform']
        )
    )

    # task2 dbt report data prep
    report = DbtTaskGroup(
        group_id='report',
        project_config=DBT_PROJECT_CONFIG,
        profile_config=DBT_CONFIG,
        render_config=RenderConfig(
            load_method=LoadMode.DBT_LS,
            select=['path:models/report']
        )
    )
    chain(transform, report)  

transform_data_in_bigquery()

