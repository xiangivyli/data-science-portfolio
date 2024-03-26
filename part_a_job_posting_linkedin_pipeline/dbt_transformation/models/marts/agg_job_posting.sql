{{
    config(
        materialized='table'
    )
}}


with job_posting as (
    select *
    from {{ ref('stg_fact__job_postings') }}
),

company_info as (
    select *
    from {{ ref('company_info') }}
),

industry as (
    select job_id,
           STRING_AGG(industry_name, ', ') AS industry
    from {{ ref('industry_info') }}
    group by job_id
),

skills as (
    select job_id,
           STRING_AGG(skill_name, ', ') AS skills_required
    from {{ ref('skills_info') }}
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