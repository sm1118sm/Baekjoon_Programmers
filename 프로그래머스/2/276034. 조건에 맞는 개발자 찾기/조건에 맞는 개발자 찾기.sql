-- 코드를 작성해주세요
select 
    id,
    email,
    first_name,
    last_name
from DEVELOPERS
where skill_code & (select code from skillcodes where name = 'Python') != 0
or skill_code & (select code from skillcodes where name = 'C#') != 0
order by id