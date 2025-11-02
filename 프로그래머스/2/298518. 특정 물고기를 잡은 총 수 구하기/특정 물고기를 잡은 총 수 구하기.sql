-- 코드를 작성해주세요
select 
    count(*) as fish_count
from fish_info as a
join FISH_NAME_INFO as b on a.fish_type = b.fish_type
where b.fish_name in ('BASS', 'SNAPPER')