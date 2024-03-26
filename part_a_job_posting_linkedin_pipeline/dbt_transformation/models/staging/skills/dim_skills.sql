{{
    config(
        materialized='table'
    )
}}
{{
    config(
        materialized='view'
    )
}}

select *
from {{ ref('skills') }}