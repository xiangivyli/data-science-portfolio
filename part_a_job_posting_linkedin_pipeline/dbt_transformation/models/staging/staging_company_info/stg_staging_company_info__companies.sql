with 

source as (

    select * from {{ source('staging_company_info', 'companies') }}

),

renamed as (

    select
        company_id,
        name,
        description,
        company_size,
        state,
        country,
        city,
        zip_code,
        address,
        url

    from source

)

select * from renamed
