with company as (
    select *
    from `cedar-style-412618`.`job_postings_project`.`companies`
),

employee as (
    select *
    from `cedar-style-412618`.`job_postings_project`.`employee_counts`
)

select company.*,
        employee.employee_count,
        employee.follower_count
from company
left join employee
on company.company_id = employee.company_id