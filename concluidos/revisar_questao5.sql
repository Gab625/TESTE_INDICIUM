-- top 10 cliente com maior ticket medio e diversidade_de_categoria maior ou igual a 3
/**/

select
	t1.id_client,
	t3.full_name,
	SUM(t1.total) / COUNT(DISTINCT t1.id) AS ticket_medio,
	COUNT(distinct t2.actual_category) as total_categorias_distintas
from 
	vendas as t1 
inner join produtos as t2 
on t1.id_product = t2.code
inner join clientes_raw as t3
on t1.id_client = t3.code
group by
	t1.id_client, 
	t3.full_name
having 
	COUNT(distinct t2.actual_category) >= 3
order by 
	SUM(t1.total) / COUNT(DISTINCT t1.id) desc	
limit 10;

-- categoria mais vendida entre os top 10 tickets medios
with top_10_clientes as (
		select
			t1.id_client,
			sum(t1.total) / count(distinct t1.id) as ticket_medio,
			count(distinct t2.actual_category) as total_categorias_distintas
		from 
			vendas as t1 
		inner join produtos as t2 
		on t1.id_product = t2.code
		inner join clientes_raw as t3
		on t1.id_client = t3.code
		group by 
			t1.id_client
		having 
			count(distinct t2.actual_category) >= 3
		order by 
			sum(t1.total) / count(distinct t1.id) desc	
		limit 10
) 
select
    t5.actual_category as categoria,
    sum(t4.qtd) as quantidade_total
from 
	vendas as t4
inner join top_10_clientes as top 
on t4.id_client = top.id_client
inner join produtos as t5
on t4.id_product = t5.code
group by 
	t5.actual_category
order by
	quantidade_total desc
limit 1;





select sum(total)/(count(distinct id)) from vendas where id_client = 42;


select 
	count(distinct actual_category)
from 
	produtos as t1 
inner join vendas as t2 
on t1.code = t2.id_product
group by t2.id_client
having count(distinct actual_category) > 2;


select * from produtos;





select * from clientes_raw;



IMPORT FOREIGN SCHEMA public LIMIT TO (produtos) 
FROM SERVER servidor_clientes_raw INTO public;


select count(*) from vendas;









