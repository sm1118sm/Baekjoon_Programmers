-- 코드를 입력하세요
SELECT
    distinct(a.car_id) as car_id
from CAR_RENTAL_COMPANY_CAR as a
join CAR_RENTAL_COMPANY_RENTAL_HISTORY as b on a.car_id = b.car_id
where a.car_type = '세단' and b.start_date like '2022-10%'
order by a.car_id desc