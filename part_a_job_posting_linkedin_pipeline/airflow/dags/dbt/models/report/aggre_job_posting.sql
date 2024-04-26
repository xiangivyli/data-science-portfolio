with job_posting as (
    select *
    from {{ ref('fact_job_posting') }}
),

company_info as (
    select *
    from {{ ref('dim_company') }}
),

industry as (
    select job_id,
           industry
    from {{ ref('dim_industry') }}
),

skills as (
    select job_id,
           skills_required
    from {{ ref('dim_skill') }}
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