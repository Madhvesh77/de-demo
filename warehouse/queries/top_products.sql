SELECT

p.name,

SUM(oi.quantity) units_sold,

SUM(oi.amount) revenue

FROM order_items oi

JOIN products p

ON oi.product_id=p.id

GROUP BY p.name

ORDER BY revenue DESC

LIMIT 10;