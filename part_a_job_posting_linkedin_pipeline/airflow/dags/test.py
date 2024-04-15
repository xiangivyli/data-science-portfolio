from pathlib import Path

from airflow.decorators import dag
from airflow.utils.dates import days_ago
from airflow.datasets import Dataset

from cosmos.airflow.task_group import DbtTaskGroup
from cosmos.config import ExecutionConfig, ProfileConfig, ProjectConfig, RenderConfig
from cosmos.constants import ExecutionMode, LoadMode

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


@dag(start_date=days_ago(1), 
    schedule=(job_postings_dataset | (companies_dataset) & (salaries_dataset) 
              | (job_skills_dataset) & (skills_dataset)),
    catchup=False,
    dag_id="test",
    tags=["dbt_transform_data_in_bigquery"]
)
def test():

    transform = DbtTaskGroup(
        group_id="transform",
        project_config=ProjectConfig(
            dbt_project_path='/usr/local/airflow/dags/dbt/'
        ),
        profile_config=profile_config,
        execution_config=ExecutionConfig(
            execution_mode=ExecutionMode.VIRTUALENV,
        ),
        render_config=RenderConfig(
            load_method=LoadMode.DBT_LS,
            select=["path:models/transform"]),
        operator_args={
            "install_deps": True,
        },
    )
test()
