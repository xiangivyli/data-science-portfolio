with 

source as (

    select * from {{ source('company_info', 'companies') }}

),

renamed as (

    select
        company_id,
        name,
        company_size,
        country,
        city

    from source

)

select * from renamed
