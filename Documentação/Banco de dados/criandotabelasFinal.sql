CREATE TABLE usuario (
  id int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  nome_completo varchar(200) NOT NULL,
  login varchar(10) UNIQUE NOT NULL,
  senha varchar(8) NOT NULL,
  cpf char(11) NOT NULL,
  tipo_usuario varchar(100),
  celular varchar(20),
  forma_recebimento varchar(20) NOT NULL,
  pix_chave varchar(30),
  banco varchar(20),
  tipo_conta varchar(20),
  agencia varchar(20),
  conta varchar(20),
  cep int NOT NULL,
  lagradouro varchar(30) NOT NULL,
  numero varchar(20) NOT NULL,
  complemento varchar(20) NOT NULL,
  cidade varchar(20) NOT NULL,
  uf varchar(2) NOT NULL
);


CREATE TABLE produto (
  id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
  nome_produto varchar(20) NOT NULL,
  preco_atual float(4) NOT NULL,
  ingredientes varchar(200) NOT NULL,
  prazo_validade int NOT NULL,
  descricao varchar(100)
);

CREATE TABLE fabricacao (
  id int AUTO_INCREMENT PRIMARY KEY NOT NULL,
  id_produto int NOT NULL,
  quantidade_fabricacao int NOT NULL,
  data_fabricacao date NOT NULL,
  vencimento date NOT NULL,
  CONSTRAINT fkfabricacaoproduto FOREIGN KEY (id_produto) REFERENCES produto(id)
);

CREATE TABLE repasse (
  id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
  id_usuario int NOT NULL,
  data_entrega date NOT NULL,
  valor_repasse float,
  CONSTRAINT fkRepasseUsuario FOREIGN KEY (id_usuario) REFERENCES usuario(id)
);

CREATE TABLE itensrepasse (
  id INT AUTO_INCREMENT NOT NULL,
  id_repasse int NOT NULL,
  id_produto int NOT NULL,
  id_fabricacao int NOT NULL,
  quantidade int NOT NULL,
  valor_unitario Float NOT NULL,
  CONSTRAINT pkRepasse PRIMARY KEY (id, id_repasse, id_produto),
  CONSTRAINT fkRepasseItens FOREIGN KEY (id_repasse) REFERENCES repasse(id),
  CONSTRAINT fkRepasseProduto FOREIGN KEY (id_produto) REFERENCES produto(id),
  CONSTRAINT fkRepasseFabricacao FOREIGN KEY (id_fabricacao) REFERENCES	fabricacao(id)
);

CREATE TABLE vendas(
  id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
  id_usuario int NOT NULL,
  data_venda date NOT NULL,
  canal_venda varchar(20),
  desconto_venda float,
  preco_venda float NOT NULL, 
  CONSTRAINT fkVendasUsuario FOREIGN KEY (id_usuario) REFERENCES usuario(id)
);


CREATE TABLE itensvendas(
  id INT AUTO_INCREMENT NOT NULL,
  id_venda INT NOT NULL,
  id_produto INT NOT NULL,
  quantidade int NOT NULL,
  valor_unitario float NOT NULL,
  CONSTRAINT pkItensVendas PRIMARY KEY (id, id_venda, id_produto),
  CONSTRAINT fkItensVendasVendas FOREIGN KEY (id_venda) REFERENCES vendas(id),
  CONSTRAINT fkItensVendasProduto FOREIGN KEY (id_produto) REFERENCES produto(id)
);
