import os
from pathlib import Path

from airflow.decorators import dag
from datetime import datetime
from airflow.utils.dates import days_ago
from airflow.datasets import Dataset

from cosmos import DbtDag, ProjectConfig, ProfileConfig, ExecutionConfig


from airflow.models.baseoperator import chain

job_postings_dataset = Dataset("job_postings_dataset")

companies_dataset = Dataset("companies_dataset") 
salaries_dataset = Dataset("salaries_dataset")

                              
job_skills_dataset = Dataset("job_skills_dataset")
skills_dataset = Dataset("skills_dataset")

profile_config = ProfileConfig(
    profile_name="job_postings_project",
    target_name="dev",
    profiles_yml_filepath=Path('/usr/local/airflow/dags/dbt/profiles.yml')
)

my_cosmos_dag = DbtDag(
    project_config=ProjectConfig(
        dbt_project_path='/usr/local/airflow/dags/dbt/'
    ),
    profile_config=profile_config,
    execution_config=ExecutionConfig(
        dbt_executable_path=f"{os.environ['AIRFLOW_HOME']}/dbt_venv/bin/dbt",
),

    # dag settings
    start_date=days_ago(1),
    schedule=(job_postings_dataset | (companies_dataset) & (salaries_dataset) 
              | (job_skills_dataset) & (skills_dataset)),
    catchup=False,
    dag_id="dbt_transform_in_bigquery",
    tags=["dbt_transform_data_in_bigquery"],
    default_args={"retries": 2},
)


