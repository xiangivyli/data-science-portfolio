with 

source as (

    select * from {{ source('fact', 'job_postings') }}

),

renamed as (

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

    from source

)

select * 
from renamed
where company_id IS NOT NULL
