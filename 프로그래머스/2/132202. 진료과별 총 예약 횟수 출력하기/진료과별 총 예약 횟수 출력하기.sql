-- 2022년 5월에 예약한 환자 수를 진료과코드 별로 조회
-- 진료과별 예약한 환자 수를 기준으로 오름차순 정렬하고, 예약한 환자 수가 같다면 진료과 코드 asc
SELECT MCDP_CD as "진료과코드", COUNT(*) as "5월예약건수"
FROM APPOINTMENT
WHERE APNT_YMD LIKE "2022-05%"
GROUP BY MCDP_CD
ORDER BY COUNT(MCDP_CD) ASC, MCDP_CD ASC


