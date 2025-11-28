-- 코드를 작성해주세요
select 
    a.id,
    case
        when ranking <= total / 4 then 'CRITICAL'
        when ranking <= total / 2 then 'HIGH'
        when ranking <= total / 4 * 3 then 'MEDIUM'
        else 'LOW'
    end as colony_name
from (
    select 
        e1.id,
        (select count(*) from ecoli_data) as total,
        (
            select count(*)
            from ecoli_data e2
            where e2.size_of_colony > e1.size_of_colony
        ) + 1 as ranking
    from ecoli_data e1
) a
order by a.id