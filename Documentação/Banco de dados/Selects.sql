SELECT I.id_insumo, I.nome_insumo, coalesce(sum(C.quantidade_insumo), '-') as soma,  min(date_format(C.data_vencimento, "%d-%m-%Y")) as vencimento
FROM insumos AS I
LEFT JOIN itemcompra AS C ON I.id_insumo = C.id_insumo
Where C.data_vencimento > CURDATE()
GROUP BY I.id_insumo










CASE when coluna1 IS NULL THEN 0,







SELECT Tipo, SUM(Quantidade) AS 'Quantidade em Estoque'
FROM Produtos
GROUP BY Tipo


SELECT  sum(quantidade) [as New_Coluna] FROM itemCompra ON Açucar


