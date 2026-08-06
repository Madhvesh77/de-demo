SELECT

c.name,

SUM(oi.amount) revenue

FROM order_items oi

JOIN products p

ON oi.product_id=p.id

JOIN categories c

ON p.category_id=c.id

GROUP BY c.name

ORDER BY revenue DESC;