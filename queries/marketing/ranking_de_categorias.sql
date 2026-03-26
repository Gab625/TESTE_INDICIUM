WITH top_10_clientes AS (
    SELECT
        t1.id_client,
        SUM(t1.total) / COUNT(DISTINCT t1.sale_id) AS ticket_medio,
        COUNT(DISTINCT t2.actual_category) AS total_categorias_distintas
    FROM vendas AS t1 
    INNER JOIN produtos AS t2 
        ON t1.id_product = t2.id_product
    INNER JOIN clientes_tratados AS t3
        ON t1.id_client = t3.id_client 
    GROUP BY 
        t1.id_client
    HAVING 
        COUNT(DISTINCT t2.actual_category) >= 3
    ORDER BY 
        ticket_medio DESC	
    LIMIT 10
) 
SELECT
    t5.actual_category AS categoria,
    SUM(t4.qtd) AS quantidade_total
FROM vendas AS t4
INNER JOIN top_10_clientes AS top 
    ON t4.id_client = top.id_client
INNER JOIN produtos AS t5
    ON t4.id_product = t5.id_product
GROUP BY 
    t5.actual_category
ORDER BY
    quantidade_total desc;