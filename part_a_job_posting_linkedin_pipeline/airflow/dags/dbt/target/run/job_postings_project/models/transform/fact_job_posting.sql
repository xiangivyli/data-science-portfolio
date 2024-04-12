
  
    

    create or replace table `cedar-style-412618`.`job_postings_project`.`fact_job_posting`
      
    
    

    OPTIONS()
    as (
      with job_posting as (
    select *
    from `cedar-style-412618`.`job_postings_project`.`job_postings`
)

select job_id,
        company_id,
        title,
        max_salary,
        med_salary,
        min_salary,
        pay_period,
        formatted_work_type,
        location,
        applies,
        remote_allowed,
        application_type,
        expiry,
        formatted_experience_level,
        listed_time
from job_posting
where company_id IS NOT NULL
    );
  