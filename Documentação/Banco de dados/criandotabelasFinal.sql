CREATE TABLE usuario (
  id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  nome_completo varchar(200) NOT NULL,
  login varchar(10) UNIQUE NOT NULL,
  senha varchar(8) NOT NULL,
  cpf char(11) NOT NULL,
  email varchar(30) NOT NULL,
  tipo_usuario varchar(50) NOT NULL,
  celular varchar(20) NOT NULL,
  pix_chave varchar(50),
  banco varchar(20),
  tipo_conta varchar(20),
  agencia varchar(7),
  conta varchar(15),
  cep int NOT NULL,
  logradouro varchar(30) NOT NULL,
  numero varchar(20) NOT NULL,
  complemento varchar(20),
  cidade varchar(20) NOT NULL,
  uf varchar(2) NOT NULL
);

CREATE TABLE convusuario (
  id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  nome_completo varchar(200) NOT NULL,
  email varchar(30) NOT NULL
);


CREATE TABLE produto (
  id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  nome_produto varchar(50) NOT NULL,
  preco_atual float(4) NOT NULL,
  ingredientes varchar(200) NOT NULL,
  prazo_validade int NOT NULL,
  descricao varchar(100)
);

CREATE TABLE fabricacao (
  id_fabricacao int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  data_fabricacao date NOT NULL
);


CREATE TABLE itemfabricacao (
  id_item INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  id_fabricacao INT NOT NULL,
  id_produto INT NOT NULL,
  quantidade INT NOT NULL,
  prazo_vencimento INT NOT NULL,
  CONSTRAINT fkItemfabricacaofabricacao FOREIGN KEY (id_fabricacao) REFERENCES fabricacao(id_fabricacao),
  CONSTRAINT fkItemfabricacaoProduto FOREIGN KEY (id_produto) REFERENCES produto(id)
);

CREATE TABLE repasse (
  id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  id_usuario int NOT NULL,
  data_entrega date NOT NULL,
  valor_repasse float,
  CONSTRAINT fkRepasseUsuario FOREIGN KEY (id_usuario) REFERENCES usuario(id)
);

CREATE TABLE itensrepasse (
  id INT NOT NULL AUTO_INCREMENT,
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

CREATE TABLE vendas (
  id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  id_usuario int NOT NULL,
  data_venda date NOT NULL,
  canal_venda varchar(20),
  desconto_venda float,
  preco_venda float NOT NULL, 
  CONSTRAINT fkVendasUsuario FOREIGN KEY (id_usuario) REFERENCES usuario(id)
);


CREATE TABLE itensvendas (
  id INT NOT NULL AUTO_INCREMENT,
  id_venda INT NOT NULL,
  id_produto INT NOT NULL,
  quantidade int NOT NULL,
  valor_unitario float NOT NULL,
  CONSTRAINT pkItensVendas PRIMARY KEY (id, id_venda, id_produto),
  CONSTRAINT fkItensVendasVendas FOREIGN KEY (id_venda) REFERENCES vendas(id),
  CONSTRAINT fkItensVendasProduto FOREIGN KEY (id_produto) REFERENCES produto(id)
);


CREATE TABLE insumos (
  id_insumo INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  nome_insumo VARCHAR(20)
);

CREATE TABLE compra (
  id_compra INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  data_compra DATE NOT NULL,
  preco_compra float NOT NULL
);

CREATE TABLE itemcompra (
  id_item INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  id_compra INT NOT NULL,
  id_insumo INT NOT NULL,
  data_vencimento date NOT NULL,
  quantidade_insumo INT NOT NULL,
  unidade_medida char(4) NOT NULL,
  preco_insumo FLOAT NOT NULL,
  CONSTRAINT fkItemcompracompra FOREIGN KEY (id_compra) REFERENCES compra(id_compra),
  CONSTRAINT fkItemcompraInsumo FOREIGN KEY (id_insumo) REFERENCES insumos(id_insumo)
);

CREATE TABLE utilizacao_insumo (
  id_utilizacao INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  id_insumo int NOT NULL,
  data_registro date NOT NULL,
  quantidade_utilizada int NOT NULL,
  CONSTRAINT fkUtilizacaoInsumo FOREIGN KEY (id_usumo) REFERENCES insumos(id)
);

CREATE TABLE caixa (
  id_caixa INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  data_registro date NOT NULL,
  valor_saida float,
  valor_entrada float
);

