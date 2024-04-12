
  
    

    create or replace table `cedar-style-412618`.`job_postings_project`.`dim_skill`
      
    
    

    OPTIONS()
    as (
      with job_skills as (
    select *
    from `cedar-style-412618`.`job_postings_project`.`job_skills`
),

skills_name as (
    select *
    from `cedar-style-412618`.`job_postings_project`.`skills`

)

select job_skills.job_id,
       skills_name.skill_name
from job_skills
left join skills_name 
on job_skills.skill_abr = skills_name.skill_abr
    );
  