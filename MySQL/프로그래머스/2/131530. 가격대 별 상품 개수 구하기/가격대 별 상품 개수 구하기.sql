SELECT FLOOR(P.PRICE / 10000) * 10000 AS PRICE_GROUP, COUNT(*) AS PRODUCTS
FROM PRODUCT AS P
GROUP BY PRICE_GROUP
ORDER BY PRICE_GROUP