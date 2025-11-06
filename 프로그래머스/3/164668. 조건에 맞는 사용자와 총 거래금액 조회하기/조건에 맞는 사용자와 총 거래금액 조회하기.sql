-- 코드를 입력하세요
SELECT
    b.user_id,
    b.nickname,
    sum(a.price) as total_sales
from USED_GOODS_BOARD as a
join USED_GOODS_USER as b on a.writer_id = b.user_id
where a.status = 'DONE'
group by b.user_id, b.nickname
having sum(a.price) >= 700000
order by total_sales