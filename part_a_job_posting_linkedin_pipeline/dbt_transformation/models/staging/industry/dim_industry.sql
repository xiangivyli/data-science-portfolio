{{
    config(
        materialized='view'
    )
}}

select *
from {{ ref('industries') }}