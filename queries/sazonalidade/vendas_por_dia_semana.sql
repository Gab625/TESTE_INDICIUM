SELECT
    t1.dia_semana,
    COALESCE(SUM(t2.total), 0) AS total_vendas_brl
FROM calendar AS t1 
LEFT JOIN vendas AS t2 
    ON t1.data = t2.sale_date
GROUP BY 
    t1.dia_semana 
ORDER BY 
    total_vendas_brl DESC;