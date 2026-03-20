WITH detalhes_de_vendas AS (
    SELECT 
        t1.id_product,
        t1.total AS receita_BRL,
        (t2.usd_price * AVG((t1.total / t1.qtd) / t2.usd_price) OVER(PARTITION BY t1.sale_date)) AS custo_unitario_BRL_dia,
        t1.qtd
    FROM vendas AS t1 
    LEFT JOIN custo AS t2 ON t1.id_product = t2.product_id
),
calculo_totais AS (
    SELECT 
        id_product,
        SUM(receita_BRL) AS receita_total_BRL,
        SUM(custo_unitario_BRL_dia * qtd) AS custo_total_BRL
    FROM detalhes_de_vendas
    GROUP BY id_product
)
SELECT 
    id_product,
    receita_total_BRL,
    (receita_total_BRL - custo_total_BRL) AS prejuizo_total,
    (receita_total_BRL - custo_total_BRL) / receita_total_BRL * 100 AS margem_percentual
FROM calculo_totais
where (receita_total_BRL - custo_total_BRL) < 0
ORDER BY margem_percentual asc;














WITH base_calculo AS (
    SELECT 
        t1.id_product,
        t1.sale_date,
        t1.total / t1.qtd AS valor_venda_unit_BRL,
        t2.usd_price AS valor_custo_unit_USD,
        -- Calculamos a média da cotação uma única vez aqui
        AVG((t1.total / t1.qtd) / t2.usd_price) OVER(PARTITION BY t1.sale_date) AS media_cotacao_dia
    FROM vendas AS t1 
    LEFT JOIN custo AS t2 ON t1.id_product = t2.product_id
)
SELECT 
    id_product,
    media_cotacao_dia,
    valor_venda_unit_BRL,
    -- Agora usamos o alias para os cálculos subsequentes
    (valor_custo_unit_USD * media_cotacao_dia) AS valor_custo_unit_BRL,
    (valor_venda_unit_BRL - (valor_custo_unit_USD * media_cotacao_dia)) AS prejuizo_unitario,
    -- Cálculo do percentual de perda/margem
    ((valor_venda_unit_BRL - (valor_custo_unit_USD * media_cotacao_dia)) / valor_venda_unit_BRL) * 100 AS percentual_de_perda_pct
FROM base_calculo;





select * from custo;
select * from vendas;