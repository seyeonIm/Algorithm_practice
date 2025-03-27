-- 2022년 1월의 도서 판매 데이터를 기준으로 
-- 저자 별, 카테고리 별 매출액(TOTAL_SALES = 판매량 * 판매가) 을 구하여, 저자 ID(AUTHOR_ID), 저자명(AUTHOR_NAME), 카테고리(CATEGORY), 매출액(SALES) 리스트를 출력
SELECT b.AUTHOR_ID, AUTHOR_NAME, CATEGORY, sum(price*sales) as TOTAL_SALES
FROM book b
inner join author a on b.AUTHOR_ID = a.AUTHOR_ID
inner join book_sales s on b.book_id = s.book_id
where year(SALES_DATE)='2022' and month(SALES_DATE)=1
group by b.AUTHOR_ID, category
order by b.AUTHOR_ID, category desc
