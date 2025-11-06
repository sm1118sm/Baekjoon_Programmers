-- 코드를 작성해주세요
select
    b.dept_id,
    a.dept_name_en,
    round(avg(b.sal), 0) as avg_sal
from hr_department as a
join hr_employees as b on a.dept_id = b.dept_id
group by b.dept_id
order by avg_sal desc