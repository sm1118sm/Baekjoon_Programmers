-- 코드를 입력하세요
SELECT
    hour,
    count(hour) as count
from (select hour(datetime) as hour from animal_outs) as c
where hour between 9 and 19
group by hour
order by hour
