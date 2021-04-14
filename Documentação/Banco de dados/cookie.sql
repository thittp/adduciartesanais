CREATE TABLE `fabricacao` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_produto` int NOT NULL,
  `quantidade_fabricacao` int NOT NULL,
  `data_fabricacao` date NOT NULL,
  `vencimento` date NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `itensrepasse` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_repasse` int NOT NULL,
  `id_produto` int NOT NULL,
  `id_fabricacao` int NOT NULL,
  `quantidade` int NOT NULL,
  `valor_unitario` float NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `itensvendas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_venda` int NOT NULL,
  `id_produto` int NOT NULL,
  `quantidade` int NOT NULL,
  `valor_unitario` float NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `produto` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome_produto` varchar(20) NOT NULL,
  `preco_atual` real NOT NULL,
  `ingredientes` varchar(200) NOT NULL,
  `prazo_validade` int NOT NULL,
  `descricao` varchar(100),
  PRIMARY KEY (`id`)
);

CREATE TABLE `repasse` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_usuario` int NOT NULL,
  `data_entrega` date NOT NULL,
  `valor_repasse` float,
  PRIMARY KEY (`id`)
);

CREATE TABLE `usuario` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome_completo` varchar(200) NOT NULL,
  `login` varchar(10) NOT NULL,
  `senha` varchar(8) NOT NULL,
  `cpf` char(11) NOT NULL,
  `tipo_usuario` varchar(100),
  `celular` varchar(20),
  `forma_recebimento` varchar(20) NOT NULL,
  `pix_chave` varchar(30),
  `banco` varchar(20),
  `tipo_conta` varchar(20),
  `agencia` varchar(20),
  `conta` varchar(20),
  `cep` int NOT NULL,
  `logradouro` varchar(30) NOT NULL,
  `numero` varchar(20) NOT NULL,
  `complemento` varchar(20) NOT NULL,
  `cidade` varchar(20) NOT NULL,
  `uf` varchar(2) NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `vendas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_usuario` int NOT NULL,
  `data_venda` date NOT NULL,
  `canal_venda` varchar(20),
  `desconto_venda` float,
  `preco_venda` float NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `insumos` (
  `id_insumo` INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `nome_insumo` VARCHAR(20)
);

CREATE TABLE `abastecimento` (
  `id_abastecimento` INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `data_compra` DATE NOT NULL,
  `id_insumo` INT NOT NULL AUTO_INCREMENT,
  `data_vencimento` date NOT NULL,
  `quantidade_insumo` int NOT NULL,
  `preco_insumo` float NOT NULL
);

CREATE TABLE `utilizacao_insumo` (
  `id_utilizacao` INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `id_insumo` int NOT NULL,
  `data_registro` date NOT NULL,
  `quantidade_utilizada` int NOT NULL
);

ALTER TABLE `repasse` ADD FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id`);

ALTER TABLE `vendas` ADD FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id`);

ALTER TABLE `itensvendas` ADD FOREIGN KEY (`id_venda`) REFERENCES `vendas` (`id`);

ALTER TABLE `produto` ADD FOREIGN KEY (`id`) REFERENCES `fabricacao` (`id_produto`);

ALTER TABLE `itensrepasse` ADD FOREIGN KEY (`id_repasse`) REFERENCES `repasse` (`id`);

ALTER TABLE `itensrepasse` ADD FOREIGN KEY (`id_produto`) REFERENCES `produto` (`id`);

ALTER TABLE `itensvendas` ADD FOREIGN KEY (`id_produto`) REFERENCES `produto` (`id`);

ALTER TABLE `fabricacao` ADD FOREIGN KEY (`id`) REFERENCES `itensrepasse` (`id_fabricacao`);

ALTER TABLE `utilizacao_insumo` ADD FOREIGN KEY (`id_insumo`) REFERENCES `insumos` (`id_insumo`);

ALTER TABLE `insumos` ADD FOREIGN KEY (`id_insumo`) REFERENCES `abastecimento` (`id_insumo`);

