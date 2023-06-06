1.
SELECT c.login, 
       COUNT ("inDelivery") 
FROM "Couriers" AS c 
LEFT OUTER JOIN "Orders" AS o ON c.id = o."courierId" 
WHERE "inDelivery" = true 
GROUP BY c.login;


2.
SELECT track, 
       CASE 
           WHEN "inDelivery" = true THEN 1 
           WHEN cancelled = true THEN -1 
           WHEN finished = true THEN 2 
           ELSE 0 
       END 
AS status 
FROM "Orders";
