/****** Object:  User [zath320017]    Script Date: 3/25/21 1:09:11 AM ******/
CREATE USER [zath320017] FOR LOGIN [uath320017] WITH DEFAULT_SCHEMA=[dbo]
GO
ALTER ROLE [db_owner] ADD MEMBER [zath320017]
GO
/****** Object:  Table [dbo].[fabricacao]    Script Date: 3/25/21 1:09:11 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[fabricacao](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[id_produto] [int] NOT NULL,
	[quantidade_fabricacao] [int] NOT NULL,
	[data_fabricacao] [date] NOT NULL,
	[vencimento] [date] NOT NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[itensrepasse]    Script Date: 3/25/21 1:09:12 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[itensrepasse](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[id_repasse] [int] NOT NULL,
	[id_produto] [int] NOT NULL,
	[id_fabricacao] [int] NOT NULL,
	[quantidade] [int] NOT NULL,
	[valor_unitario] [float] NOT NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[itensvendas]    Script Date: 3/25/21 1:09:12 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[itensvendas](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[id_venda] [int] NOT NULL,
	[id_produto] [int] NOT NULL,
	[quantidade] [int] NOT NULL,
	[valor_unitario] [float] NOT NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[produto]    Script Date: 3/25/21 1:09:12 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[produto](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[nome_produto] [varchar](20) NOT NULL,
	[preco_atual] [real] NOT NULL,
	[ingredientes] [varchar](200) NOT NULL,
	[prazo_validade] [int] NOT NULL,
	[descricao] [varchar](100) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[repasse]    Script Date: 3/25/21 1:09:12 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[repasse](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[id_usuario] [int] NOT NULL,
	[data_entrega] [date] NOT NULL,
	[valor_repasse] [float] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[usuario]    Script Date: 3/25/21 1:09:12 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[usuario](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[nome_completo] [varchar](200) NOT NULL,
	[login] [varchar](10) NOT NULL,
	[senha] [varchar](8) NOT NULL,
	[cpf] [char](11) NOT NULL,
	[tipo_usuario] [varchar](100) NULL,
	[celular] [varchar](20) NULL,
	[forma_recebimento] [varchar](20) NOT NULL,
	[pix_chave] [varchar](30) NULL,
	[banco] [varchar](20) NULL,
	[tipo_conta] [varchar](20) NULL,
	[agencia] [varchar](20) NULL,
	[conta] [varchar](20) NULL,
	[cep] [int] NOT NULL,
	[lagradouro] [varchar](30) NOT NULL,
	[numero] [varchar](20) NOT NULL,
	[complemento] [varchar](20) NOT NULL,
	[cidade] [varchar](20) NOT NULL,
	[uf] [varchar](2) NOT NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[vendas]    Script Date: 3/25/21 1:09:12 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[vendas](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[id_usuario] [int] NOT NULL,
	[data_venda] [date] NOT NULL,
	[canal_venda] [varchar](20) NULL,
	[desconto_venda] [float] NULL,
	[preco_venda] [float] NOT NULL
) ON [PRIMARY]
GO
/****** Object:  Index [PK__fabricac__3213E83F7B6933AE]    Script Date: 3/25/21 1:09:12 AM ******/
ALTER TABLE [dbo].[fabricacao] ADD PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO
/****** Object:  Index [pkRepasse]    Script Date: 3/25/21 1:09:12 AM ******/
ALTER TABLE [dbo].[itensrepasse] ADD  CONSTRAINT [pkRepasse] PRIMARY KEY CLUSTERED 
(
	[id] ASC,
	[id_repasse] ASC,
	[id_produto] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO
/****** Object:  Index [pkItensVendas]    Script Date: 3/25/21 1:09:12 AM ******/
ALTER TABLE [dbo].[itensvendas] ADD  CONSTRAINT [pkItensVendas] PRIMARY KEY CLUSTERED 
(
	[id] ASC,
	[id_venda] ASC,
	[id_produto] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO
/****** Object:  Index [PK__produto__3213E83F8C880EB1]    Script Date: 3/25/21 1:09:12 AM ******/
ALTER TABLE [dbo].[produto] ADD PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO
/****** Object:  Index [PK__repasse__3213E83F8204D9F9]    Script Date: 3/25/21 1:09:12 AM ******/
ALTER TABLE [dbo].[repasse] ADD PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO
/****** Object:  Index [PK__usuario__3213E83F53448B93]    Script Date: 3/25/21 1:09:12 AM ******/
ALTER TABLE [dbo].[usuario] ADD PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO
/****** Object:  Index [PK__vendas__3213E83FFABD8E0A]    Script Date: 3/25/21 1:09:12 AM ******/
ALTER TABLE [dbo].[vendas] ADD PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO
SET ANSI_PADDING ON
GO
/****** Object:  Index [UQ__usuario__7838F272CD3A72A6]    Script Date: 3/25/21 1:09:12 AM ******/
ALTER TABLE [dbo].[usuario] ADD UNIQUE NONCLUSTERED 
(
	[login] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO
ALTER TABLE [dbo].[fabricacao]  WITH CHECK ADD  CONSTRAINT [fkfabricacaoproduto] FOREIGN KEY([id_produto])
REFERENCES [dbo].[produto] ([id])
GO
ALTER TABLE [dbo].[fabricacao] CHECK CONSTRAINT [fkfabricacaoproduto]
GO
ALTER TABLE [dbo].[itensrepasse]  WITH CHECK ADD  CONSTRAINT [fkRepasseFabricacao] FOREIGN KEY([id_fabricacao])
REFERENCES [dbo].[fabricacao] ([id])
GO
ALTER TABLE [dbo].[itensrepasse] CHECK CONSTRAINT [fkRepasseFabricacao]
GO
ALTER TABLE [dbo].[itensrepasse]  WITH CHECK ADD  CONSTRAINT [fkRepasseItens] FOREIGN KEY([id_repasse])
REFERENCES [dbo].[repasse] ([id])
GO
ALTER TABLE [dbo].[itensrepasse] CHECK CONSTRAINT [fkRepasseItens]
GO
ALTER TABLE [dbo].[itensrepasse]  WITH CHECK ADD  CONSTRAINT [fkRepasseProduto] FOREIGN KEY([id_produto])
REFERENCES [dbo].[produto] ([id])
GO
ALTER TABLE [dbo].[itensrepasse] CHECK CONSTRAINT [fkRepasseProduto]
GO
ALTER TABLE [dbo].[itensvendas]  WITH CHECK ADD  CONSTRAINT [fkItensVendasProduto] FOREIGN KEY([id_produto])
REFERENCES [dbo].[produto] ([id])
GO
ALTER TABLE [dbo].[itensvendas] CHECK CONSTRAINT [fkItensVendasProduto]
GO
ALTER TABLE [dbo].[itensvendas]  WITH CHECK ADD  CONSTRAINT [fkItensVendasVendas] FOREIGN KEY([id_venda])
REFERENCES [dbo].[vendas] ([id])
GO
ALTER TABLE [dbo].[itensvendas] CHECK CONSTRAINT [fkItensVendasVendas]
GO
ALTER TABLE [dbo].[repasse]  WITH CHECK ADD  CONSTRAINT [fkRepasseUsuario] FOREIGN KEY([id_usuario])
REFERENCES [dbo].[usuario] ([id])
GO
ALTER TABLE [dbo].[repasse] CHECK CONSTRAINT [fkRepasseUsuario]
GO
ALTER TABLE [dbo].[vendas]  WITH CHECK ADD  CONSTRAINT [fkVendasUsuario] FOREIGN KEY([id_usuario])
REFERENCES [dbo].[usuario] ([id])
GO
ALTER TABLE [dbo].[vendas] CHECK CONSTRAINT [fkVendasUsuario]
GO