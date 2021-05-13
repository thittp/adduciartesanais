INSERT INTO insumos(nome_insumo) VALUES ('Bircabonato')




INSERT INTO compra(data_compra, preco_compra) VALUES (20210510, 12.15);
INSERT INTO compra(data_compra, preco_compra) VALUES (20210410, 123.15)

INSERT INTO itemcompra (id_compra, id_insumo, data_vencimento, quantidade_insumo, preco_insumo) VALUES (1, 1, 20210603, 20.00, 13.00)
);




INSERT INTO produto (nome_produto, preco_atual, ingredientes, prazo_validade, descricao) VALUES ('Cookie Chocolate Branco', 7.00, 'chocolate, farinha, leite', 15,'muito bommmm');
INSERT INTO produto (nome_produto, preco_atual, ingredientes, prazo_validade, descricao) VALUES ('Cookie Chocolate Preto', 8.00, 'chocolate, farinha, leite', 15,'muito gostoso')




INSERT INTO fabricacao (data_fabricacao) VALUES (20210510)


INSERT INTO itemfabricacao (id_fabricacao, id_produto, quantidade, prazo_vencimento) VALUES (1, 1, 10, 15);
INSERT INTO itemfabricacao (id_fabricacao, id_produto, quantidade, prazo_vencimento) VALUES (1, 2, 12, 15);


INSERT INTO vendas (id_usuario, data_venda, canal_venda, preco_venda) VALUES (2, 20210510, 'ifood', 5.00);
INSERT INTO vendas (id_usuario, data_venda, canal_venda, preco_venda) VALUES (2, 20210510, 'ifood', 10.00);
INSERT INTO vendas (id_usuario, data_venda, canal_venda, preco_venda) VALUES (2, 20210510, 'ifood', 15.00);
INSERT INTO vendas (id_usuario, data_venda, canal_venda, preco_venda) VALUES (2, 20210511, 'ifood', 15.00);
INSERT INTO vendas (id_usuario, data_venda, canal_venda, preco_venda) VALUES (2, 20210511, 'ifood', 10.00);
INSERT INTO vendas (id_usuario, data_venda, canal_venda, preco_venda) VALUES (2, 20210512, 'ifood', 1025.00)




INSERT INTO itensvendas (id_venda, id_produto, quantidade, valor_unitario) VALUES (1, 1, 2, 5.00);
INSERT INTO itensvendas (id_venda, id_produto, quantidade, valor_unitario) VALUES (1, 2, 6, 5.00)



INSERT INTO caixa (data_registro, valor_entrada) VALUES (20210510, 5.00);
INSERT INTO caixa (data_registro, valor_entrada) VALUES (20210510, 15.00);
INSERT INTO caixa (data_registro, valor_entrada) VALUES (20210510, 10.00);
INSERT INTO caixa (data_registro, valor_entrada) VALUES (20210511, 10.00);
INSERT INTO caixa (data_registro, valor_entrada) VALUES (20210512, 1205.00)


INSERT INTO caixa (data_registro, valor_saida) VALUES (20210510, 19.00);
INSERT INTO caixa (data_registro, valor_saida) VALUES (20210510, 15.00);
INSERT INTO caixa (data_registro, valor_saida) VALUES (20210511, 13.00);
INSERT INTO caixa (data_registro, valor_saida) VALUES (20210509, 11.00);
INSERT INTO caixa (data_registro, valor_saida) VALUES (20210512, 12.15)

