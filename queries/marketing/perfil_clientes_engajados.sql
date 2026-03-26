SELECT
    t1.id_client,
    t3.full_name,
    SUM(t1.total) / COUNT(DISTINCT t1.sale_id) AS ticket_medio,
    COUNT(DISTINCT t2.actual_category) AS total_categorias_distintas
FROM vendas AS t1 
INNER JOIN produtos AS t2 
    ON t1.id_product = t2.id_product
INNER JOIN clientes_tratados AS t3
    ON t1.id_client = t3.id_client 
GROUP BY
    t1.id_client, 
    t3.full_name
HAVING 
    COUNT(DISTINCT t2.actual_category) >= 3
ORDER BY 
    ticket_medio DESC	
LIMIT 10;