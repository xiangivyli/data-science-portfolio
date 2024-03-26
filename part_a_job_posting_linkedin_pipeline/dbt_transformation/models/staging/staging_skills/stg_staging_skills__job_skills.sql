with 

source as (

    select * from {{ source('staging_skills', 'job_skills') }}

),

renamed as (

    select
        job_id,
        skill_abr

    from source

)

select * from renamed
