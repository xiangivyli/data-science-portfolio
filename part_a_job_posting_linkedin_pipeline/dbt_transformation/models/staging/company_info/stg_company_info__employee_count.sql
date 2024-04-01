with 

source as (

    select * from {{ source('company_info', 'employee_counts') }}

),

renamed as (

    select
        company_id,
        employee_count,
        follower_count,
        time_recorded,
        ROW_NUMBER() OVER (PARTITION BY company_id ORDER BY time_recorded DESC) as rank
    from source

)

select * 
from renamed
where rank = 1
