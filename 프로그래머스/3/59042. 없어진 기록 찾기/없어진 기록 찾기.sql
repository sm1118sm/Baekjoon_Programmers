-- 코드를 입력하세요
SELECT
    b.animal_id,
    b.name
from animal_ins as a
right join animal_outs as b on a.animal_id = b.animal_id
where a.animal_id is null
order by b.animal_id