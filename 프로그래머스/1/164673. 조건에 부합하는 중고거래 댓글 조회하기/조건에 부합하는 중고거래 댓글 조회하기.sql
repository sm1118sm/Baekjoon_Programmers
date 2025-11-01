-- 코드를 입력하세요
SELECT
    a.title,
    a.board_id,
    b.reply_id,
    b.writer_id,
    b.contents,
    substr(b.created_date, 1, 10) as created_date
from USED_GOODS_BOARD as a
join USED_GOODS_REPLY as b on a.board_id = b.board_id
where a.created_date like '2022-10-%'
order by b.created_date, a.title