with job_skills as (
    select *
    from {{ source('job_postings_project', 'job_skills') }}
),

skills_name as (
    select *
    from {{ source('job_postings_project', 'skills') }}

)

select job_skills.job_id,
       STRING_AGG(skills_name.skill_name, ', ') AS skills_required
from job_skills
left join skills_name 
on job_skills.skill_abr = skills_name.skill_abr
group by job_skills.job_id
