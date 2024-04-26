with company as (
    select *
    from {{ source('job_postings_project', 'companies') }}
),

employee as (
    select
        company_id,
        employee_count,
        follower_count,
        time_recorded,
        ROW_NUMBER() OVER (PARTITION BY company_id ORDER BY time_recorded DESC) as rank
    from {{ source('job_postings_project', 'employee_counts') }}
    where rank = 1
)

select company.*,
        employee.employee_count,
        employee.follower_count
from company
left join employee
on company.company_id = employee.company_id