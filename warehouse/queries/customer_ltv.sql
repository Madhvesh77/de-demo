SELECT

cu.first_name,

SUM(o.amount) lifetime_value

FROM customers cu

JOIN orders o

ON cu.id=o.customer_id

GROUP BY cu.first_name

ORDER BY lifetime_value DESC

LIMIT 10;