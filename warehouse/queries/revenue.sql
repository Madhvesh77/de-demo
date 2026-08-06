SELECT

SUM(amount) AS revenue

FROM payments

WHERE status='SUCCESS';