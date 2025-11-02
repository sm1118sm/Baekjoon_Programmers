-- 코드를 입력하세요
SELECT
    a.category,
    sum(b.sales) as total_sales
from book as a
join book_sales as b on a.book_id = b.book_id
where b.sales_date like '2022-01%'
group by a.category
order by a.category