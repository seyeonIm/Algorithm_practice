-- 3개의 테이블에서 자동차 종류가 '세단' 또는 'SUV' 인 자동차 중
-- 2022년 11월 1일부터 2022년 11월 30일까지 대여 가능하고
-- 30일간의 대여 금액이 50만원 이상 200만원 미만인 자동차에 대해서
-- 자동차 ID, 자동차 종류, 대여 금액(컬럼명: FEE) 리스트를 출력
SELECT R.CAR_ID, R.CAR_TYPE, ROUND(R.DAILY_FEE * 30 * (100 - D.DISCOUNT_RATE) / 100)AS FEE
FROM CAR_RENTAL_COMPANY_CAR R
JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN D
ON R.CAR_TYPE = D.CAR_TYPE
WHERE R.CAR_TYPE IN ('세단', 'SUV') AND D.DURATION_TYPE = '30일 이상' AND R.CAR_ID NOT IN (
    SELECT CAR_ID FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE END_DATE >= '2022-11-01' AND START_DATE < '2022-12-01')
HAVING FEE BETWEEN 500000 AND 1999999
ORDER BY FEE DESC, R.CAR_TYPE, R.CAR_ID DESC
    
