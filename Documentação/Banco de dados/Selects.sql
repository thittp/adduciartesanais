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




GROUP BY P.id_produto


