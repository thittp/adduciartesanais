from contextlib import closing
import mysql.connector
import os
import werkzeug






###############################################
#### Funções auxiliares de banco de dados. ####
###############################################

# Converte uma linha em um dicionário.
def row_to_dict(description, row):
    if row is None: return None
    d = {}
    for i in range(0, len(row)):
        d[description[i][0]] = row[i]
    return d

# Converte uma lista de linhas em um lista de dicionários.
def rows_to_dict(description, rows):
    result = []
    for row in rows:
        result.append(row_to_dict(description, row))
    return result


####################################
#### Definições básicas de BD. ####
####################################


def conectar():
    return mysql.connector.connect(host="adducis.ch3noq1jgsa1.us-east-2.rds.amazonaws.com",user="adducis",password= "654artesanais",database="Usuarios")

def db_fazer_login(login, senha):
    with closing(conectar()) as con, closing(con.cursor()) as cur:
        cur.execute("SELECT login, senha, nome, tipo FROM usuario WHERE login = %s AND senha = %s;", (login, senha))
        return row_to_dict(cur.description, cur.fetchone())

def db_consultar_usuario(id):
    with closing(conectar()) as con, closing(con.cursor()) as cur:
        cur.execute("SELECT id, nome, login, senha, tipo, telefone FROM usuario WHERE id = (%s)", [id])
        return row_to_dict(cur.description, cur.fetchone())


def db_listar_usuarios():
    with closing(conectar()) as con, closing(con.cursor()) as cur:
        cur.execute("SELECT id, nome, login, senha, tipo, telefone FROM usuario")
        return rows_to_dict(cur.description, cur.fetchall())


def db_criar_usuario(nome, login, senha, tipo, telefone):
    with closing(conectar()) as con, closing(con.cursor()) as cur:
        cur.execute("INSERT INTO usuario (nome, login, senha, tipo, telefone) VALUES (%s, %s, %s, %s, %s)", [nome, login, senha, tipo, telefone])
        id = cur.lastrowid
        con.commit()
        return {'id': id, 'nome': nome, 'login': login, 'senha': senha, 'tipo': tipo, 'telefone': telefone}

def db_editar_usuario(id, nome, login, senha, tipo, telefone):
    with closing(conectar()) as con, closing(con.cursor()) as cur:
        cur.execute("UPDATE usuario SET nome = %s, login = %s, senha = %s, tipo = %s, telefone = %s WHERE id = %s", [nome, login, senha, tipo, telefone, id])
        con.commit()
        return {'id': id, 'nome': nome, 'login': login, 'senha': senha, 'tipo': tipo, 'telefone': telefone}


def db_deletar_usuario(id):
    with closing(conectar()) as con, closing(con.cursor()) as cur:
        cur.execute("DELETE FROM usuario WHERE id = %s", [id])
        con.commit()


def db_listar_insumos():
    with closing(conectar()) as con, closing(con.cursor()) as cur:
        cur.execute("SELECT I.id_insumo as id, I.nome, coalesce(sum(C.quantidade_insumo), '-') as soma,  coalesce(max(date_format(C.data_vencimento, '%d-%m-%Y')), '-') as vencimento FROM insumos AS I Left JOIN itemcompra AS C ON I.id_insumo = C.id_insumo GROUP BY I.id_insumo")
        return rows_to_dict(cur.description, cur.fetchall())


def db_criar_insumo(nome):
    with closing(conectar()) as con, closing(con.cursor()) as cur:
        cur.execute("INSERT INTO insumos (nome) VALUES (%s)", [nome])
        id_insumo = cur.lastrowid
        con.commit()
        return {'id_insumo': id_insumo, 'nome': nome}

def db_editar_insumo(id_insumo, nome):
    with closing(conectar()) as con, closing(con.cursor()) as cur:
        cur.execute("UPDATE insumos SET nome = %s WHERE id = %s", [nome, id_insumo])
        con.commit()
        return {'id_insumo': id_insumo, 'nome': nome}






#estoque
def db_listar_estoque():
    with closing(conectar()) as con, closing(con.cursor()) as cur:
        cur.execute("SELECT P.id_produto, P.nome, sum(F.quantidade) - sum(V.quantidade) AS quantidade FROM produto as P LEFT JOIN itemfabricacao AS F ON P.id_produto = F.id_produto LEFT JOIN itensvendas AS V ON P.id_produto = V.id_produto GROUP BY P.id_produto")
        return rows_to_dict(cur.description, cur.fetchall())


#produto
def db_criar_produto(nome, preco_atual, ingredientes, prazo_validade, descricao):
    with closing(conectar()) as con, closing(con.cursor()) as cur:
        cur.execute("INSERT INTO produto (nome, preco_atual, ingredientes, prazo_validade, descricao) VALUES (%s, %s, %s, %s, %s)", [nome, preco_atual, ingredientes, prazo_validade, descricao])
        id_produto = cur.lastrowid
        con.commit()
        return {'id_produto': id_produto, 'nome': nome, 'preco_atual': preco_atual, 'ingredientes': ingredientes, 'prazo_validade': prazo_validade, 'descricao': descricao}

def db_editar_produto(id_produto, nome):
    with closing(conectar()) as con, closing(con.cursor()) as cur:
        cur.execute("UPDATE produto SET nome = %s WHERE id = %s", [nome, id_insumo])
        con.commit()
        return {'id_produto': id_produto, 'nome': nome}


#fabricacao
def db_listar_fabricacao():
    with closing(conectar()) as con, closing(con.cursor()) as cur:
        cur.execute("SELECT F.id_fabricacao, F.data_fabricacao, coalesce(sum(I.quantidade), '-') as soma FROM fabricacao AS F Left JOIN itemfabricacao AS I ON F.id_fabricacao = I.id_fabricacao GROUP BY F.id_fabricacao")
        return rows_to_dict(cur.description, cur.fetchall())


#Caixa
def db_listar_saldo():
    with closing(conectar()) as con, closing(con.cursor()) as cur:
        cur.execute("SELECT X.data_registro as 'Data', format(coalesce(sum(X.valor_entrada),0)-(coalesce(sum(X.valor_saida),0)), 2) as ValorDia FROM caixa as X GROUP BY X.data_registro")
        return rows_to_dict(cur.description, cur.fetchall())


def db_listar_entradas():
    with closing(conectar()) as con, closing(con.cursor()) as cur:
        cur.execute("SELECT V.data_venda as 'Data', CONCAT('R$ ', Replace(FORMAT(sum(V.preco_venda), 2), '.', ',')) AS Valor FROM vendas as V GROUP BY V.data_venda")
        return rows_to_dict(cur.description, cur.fetchall())

def db_listar_saidas():
    with closing(conectar()) as con, closing(con.cursor()) as cur:
        cur.execute("SELECT C.data_compra as 'Data', CONCAT('R$ ', Replace(FORMAT(sum(C.preco_compra), 2), '.', ',')) AS Valor FROM compra as C GROUP BY C.data_compra")
        return rows_to_dict(cur.description, cur.fetchall())
