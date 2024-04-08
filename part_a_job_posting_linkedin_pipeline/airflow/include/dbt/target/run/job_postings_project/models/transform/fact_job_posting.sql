
  
    

    create or replace table `cedar-style-412618`.`job_postings_project`.`fact_job_posting`
      
    
    

    OPTIONS()
    as (
      with job_posting as (
    select 
        job_id,
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

    from `cedar-style-412618`.`job_postings_project`.`job_postings`
    where company_id IS NOT NULL
),

company_info as (
    select *
    from `cedar-style-412618`.`job_postings_project`.`dim_company`
),

industry as (
    select job_id,
           STRING_AGG(industry_name, ', ') AS industry
    from `cedar-style-412618`.`job_postings_project`.`dim_industry`
    group by job_id
),

skills as (
    select job_id,
           STRING_AGG(skill_name, ', ') AS skills_required
    from `cedar-style-412618`.`job_postings_project`.`dim_skill`
    group by job_id
)

SELECT job_posting.*,
       skills.skills_required,
       company_info.name,
       company_info.company_size,
       company_info.country,
       company_info.city,
       company_info.employee_count,
       company_info.follower_count,
       industry.industry
FROM job_posting 
LEFT JOIN company_info
ON job_posting.company_id = company_info.company_id
LEFT JOIN industry
ON job_posting.job_id = industry.job_id
LEFT JOIN skills
ON job_posting.job_id = skills.job_id
    );
  