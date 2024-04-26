with job_industry as (
    select *
    from {{ source('job_postings_project', 'job_industries') }}
),

industry as (
    select CAST (industry_id AS STRING) AS industry_id,
           industry_name
    from {{ source('job_postings_project', 'industries') }}

)

select job_industry.job_id,
       STRING_AGG(industry.industry_name, ', ') AS industry
from job_industry
left join industry
on job_industry.industry_id = industry.industry_id
group by job_industry.job_id
