-- 코드를 입력하세요
SELECT
    dr_name,
    dr_id,
    mcdp_cd,
    substr(hire_ymd, 1, 10) as hire_ymd
from doctor
where mcdp_cd in ('CS', 'GS')
order by hire_ymd desc, dr_name