with company as (
    select *
    from {{ source('job_postings_project', 'companies') }}
),

employee_counts as (
    select
        company_id,
        employee_count,
        follower_count,
        time_recorded,
        ROW_NUMBER() OVER (PARTITION BY company_id ORDER BY time_recorded DESC) as rank
    from {{ source('job_postings_project', 'employee_counts') }}
)

select company.*,
        employee_counts.employee_count,
        employee_counts.follower_count
from company
left join employee_counts
on company.company_id = employee_counts.company_id
where employee_counts.rank = 1