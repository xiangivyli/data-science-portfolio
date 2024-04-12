
  
    

    create or replace table `cedar-style-412618`.`job_postings_project`.`aggre_job_posting`
      
    
    

    OPTIONS()
    as (
      with job_posting as (
    select *
    from `cedar-style-412618`.`job_postings_project`.`fact_job_posting`
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
  