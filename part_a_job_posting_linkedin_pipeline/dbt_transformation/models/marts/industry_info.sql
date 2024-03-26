
with job_industry as (
    select *
    from {{ ref('stg_industry__job_industries') }}
),

industry as (
    select CAST (industry_id AS STRING) AS industry_id,
           industry_name
    from {{ ref('dim_industry') }}

)

select job_industry.job_id,
       industry.industry_name
from job_industry
left join industry
on job_industry.industry_id = industry.industry_id