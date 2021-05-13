SELECT I.id_insumo, I.nome_insumo, coalesce(sum(C.quantidade_insumo), '-') as soma,  min(date_format(C.data_vencimento, '%d-%m-%Y')) as vencimento
FROM insumos AS I
LEFT JOIN itemcompra AS C ON I.id_insumo = C.id_insumo
Where C.data_vencimento > CURDATE()
GROUP BY I.id_insumo


convusuarios







CASE when coluna1 IS NULL THEN 0,







SELECT Tipo, SUM(Quantidade) AS 'Quantidade em Estoque'
FROM Produtos
GROUP BY Tipo


SELECT  sum(quantidade) [as New_Coluna] FROM itemCompra ON Açucar




SELECT I.id_insumo, I.nome_insumo, coalesce(sum(C.quantidade_insumo), '-') as soma,  min(date_format(C.data_vencimento, '%d-%m-%Y')) as vencimento
FROM insumos AS I
LEFT JOIN itemcompra AS C ON I.id_insumo = C.id_insumo
Where C.data_vencimento > CURDATE()
GROUP BY I.id_insumo


SELECT P.id, P.nome_produto, SUM(F.quantidade) - SUM(V.quantidade) as quantidade
FROM produto as P 
Join itemvenda as V ON P.id = V.id_produto
LEFT JOIN itemfabricacao AS F ON P.id = F.id_produto
GROUP BY P.id_produto

coalesce(subtract(c
subtract
GROUP BY P.id_produto

SELECT P.id, P.nome_produto, sum(F.quantidade) - sum(V.quantidade) AS quantidade
FROM produto as P
LEFT JOIN itemfabricacao AS F ON P.id = F.id_produto
LEFT JOIN itensvendas AS V ON P.id = V.id_produto
GROUP BY P.id




SELECT X.data_registro as 'Data', format(coalesce(sum(X.valor_entrada),0)-(coalesce(sum(X.valor_saida),0)), 2) as ValorDia,  as ValorSaldo
FROM caixa as X
GROUP BY X.data_registro

select 'D' tipo, conta_debito conta, valor
from lancamento
where not conta_debito is null
union all
select 'C' tipo, conta_credito, valor
from lancamento
where not conta_credito is null



SELECT X.data_registro as 'Data', format(coalesce(sum(X.valor_entrada),0)-(coalesce(sum(X.valor_saida),0)), 2) as ValorDia
FROM caixa as X
GROUP BY X.data_registro



SELECT X.data_registo as 'Data',
	sum(case when tipo='saida' then valor else 0 end) valor_saida,
	sum(case when tipo='entrada' then valor else 0 end) valor_entrada,
From 
    
GROUP BY X.data_registro




select
    X.data_registro,  X.total_saida, X.total_entrada,
    abs(X.total_saida - X.total_entrada) saldo,
    (case when X.total_saida > X.total_entrada then 'saida' else 'entrada' end) tp
from (
	SELECT data_registo as 'Data',
		sum(case when tipo='saida' then valor else 0 end) valor_saida,
		sum(case when tipo='entrada' then valor else 0 end) valor_entrada,
	From  (
            select 'saida' tipo, valor_saida data, valor
            from caixa
            where not valor_saida is null
            union all
            select 'entrada' tipo, valor_entrada, valor
            from caixa
            where not valor_entrada is null
    ) tab
    group by
        data_registro
) X
left join data_registro on data_registro = X.data_registro








IF SQL%NOTFOUND THEN 0


Saldo is valor do dia anterior + vendas dia atual - compra dia atual


SELECT V.data_venda as 'Data', CONCAT('R$ ', Replace(FORMAT(sum(V.preco_venda), 2), '.', ',')) AS Valor
FROM vendas as V
FROM compra as C
GROUP BY V.data_venda




SELECT C.data_compra as 'Data', CONCAT('R$ ', Replace(FORMAT(sum(C.preco_compra), 2), '.', ',')) AS Valor
FROM compra as C
GROUP BY C.data_compra