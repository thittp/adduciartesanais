import bd as bd



##########################################
#### Definições de regras de negócio. ####
##########################################

def criar_usuario(nome, login, senha, tipo, telefone):
    return bd.db_criar_usuario(nome, login, senha, tipo, telefone)


def editar_usuario(id, nome, login, senha, tipo, telefone):
    usuario = bd.db_consultar_usuario(id)
    if usuario is None:
        return 'não existe', None
    bd.db_editar_usuario(id, nome, login, senha, tipo, telefone)
    return 'alterado', usuario


def apagar_usuario(id):
    usuario = bd.db_consultar_usuario(id)
    if usuario is not None: bd.db_deletar_usuario(id)
    return usuario



# insumos
def criar_insumo(nome):
    return bd.db_criar_insumo(nome)


def editar_insumo(id_insumo):
    insumo = bd.db_consultar_insumo(id_insumo)
    if insumo is None:
        return 'não existe', None
    bd.db_editar_insumo(id_insumo, nome)
    return 'alterado', insumo


#produtos
def criar_produto(nome, preco_atual, ingredientes, prazo_validade, descricao):
    return bd.db_criar_produto(nome, preco_atual, ingredientes, prazo_validade, descricao)


def editar_produto(nome, preco_atual, ingredientes, prazo_validade, descricao):
    produto = bd.db_consultar_produto(id_produto)
    if produto is None:
        return 'não existe', None
    bd.db_editar_produto(id_produto, nome)
    return 'alterado', produto



