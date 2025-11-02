-- 코드를 입력하세요
SELECT
    product_code as category,
    count(product_code) as products
from (select substr(product_code, 1, 2) as product_code from product) as sub
group by product_code
order by category