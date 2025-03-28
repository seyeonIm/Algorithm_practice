-- 2021년에 가입한 전체 회원들 중 상품을 구매한 회원수와 
-- 상품을 구매한 회원의 비율(=2021년에 가입한 회원 중 상품을 구매한 회원수 / 2021년에 가입한 전체 회원 수)
SELECT YEAR(SALES_DATE) as YEAR, 
    MONTH(SALES_DATE) as month, 
    count(distinct(s.USER_ID)) as PURCHASED_USER, 
    round(
        count(distinct s.USER_ID) / 
        (select count(u.user_id) from USER_INFO u where year(u.JOINED)=2021), 1) as PUCHASED_RATIO
from USER_INFO i 
right join ONLINE_SALE s
    on i.USER_ID = s.USER_ID
where year(i.JOINED)='2021'
group by year(s.SALES_DATE), month(s.SALES_DATE)
order by year(s.SALES_DATE), month(s.SALES_DATE)