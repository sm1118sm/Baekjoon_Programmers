-- 코드를 입력하세요
SELECT
    food_type,
    rest_id,
    rest_name,
    favorites
from rest_info as a
where favorites = (
    select 
        max(favorites) 
    from rest_info
    where food_type = a.food_type
)
order by food_type desc