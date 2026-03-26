WITH detalhes_de_vendas AS (
    SELECT 
        t1.id_product,
        t1.total AS receita_total_brl,
        (t2.usd_price * AVG((t1.total / t1.qtd) / t2.usd_price) OVER(PARTITION BY t1.sale_date)) AS custo_unitario_brl_dia,
        t1.qtd
    FROM vendas AS t1 
    LEFT JOIN custo_importacao AS t2 
        ON t1.id_product = t2.product_id
),
calculo_totais AS (
    SELECT 
        id_product,
        SUM(receita_total_brl) AS receita_total_brl,
        SUM(custo_unitario_brl_dia * qtd) AS custo_total_brl
    FROM detalhes_de_vendas
    GROUP BY id_product
)
SELECT 
    t3.id_product,
    p.product_name, 
    t3.receita_total_brl,
    (t3.receita_total_brl - t3.custo_total_brl) AS prejuizo_total,
    ((t3.receita_total_brl - t3.custo_total_brl) / t3.receita_total_brl) * 100 AS margem_percentual
FROM calculo_totais AS t3
INNER JOIN produtos AS p 
    ON t3.id_product = p.id_product
WHERE (t3.receita_total_brl - t3.custo_total_brl) < 0
ORDER BY margem_percentual ASC
LIMIT 10;