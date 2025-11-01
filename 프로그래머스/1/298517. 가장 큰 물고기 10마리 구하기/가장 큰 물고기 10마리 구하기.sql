-- 코드를 작성해주세요
select 
    id, length
from fish_info
where length is not null
order by length desc
limit 10