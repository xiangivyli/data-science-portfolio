
  
    

    create or replace table `cedar-style-412618`.`job_postings_project`.`dim_industry`
      
    
    

    OPTIONS()
    as (
      with job_industry as (
    select *
    from `cedar-style-412618`.`job_postings_project`.`job_industries`
),

industry as (
    select CAST (industry_id AS STRING) AS industry_id,
           industry_name
    from `cedar-style-412618`.`job_postings_project`.`industries`

)

select job_industry.job_id,
       industry.industry_name
from job_industry
left join industry
on job_industry.industry_id = industry.industry_id
    );
  