with job_skills as (
    select *
    from {{ ref('stg_skills__job_skills') }}
),

skills_name as (
    select *
    from {{ ref('dim_skills') }}

)

select job_skills.job_id,
       skills_name.skill_name
from job_skills
left join skills_name 
on job_skills.skill_abr = skills_name.skill_abr