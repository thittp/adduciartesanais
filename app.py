from flask import Flask, make_response, request, render_template, redirect, send_from_directory
from contextlib import closing
import mysql.connector
import os
import werkzeug



app = Flask(__name__)

### Partes de login. ###
@app.route("/")
@app.route("/login")
def menu():
    logado = autenticar_login()
    if logado is None:
        return render_template("/index.html", erro = "")
    if logado['tipo']=="admin":
        return render_template("dashmaster.html", logado = logado, mensagem = "")
    else:
        return render_template("dashvendedor.html", logado = logado, mensagem = "")  


@app.route("/login", methods = ["POST"])
def login():
    # Extrai os dados do formulário.
    f = request.form
    if "login" not in f or "senha" not in f:
        return ":(", 422
    login = f["login"]
    senha = f["senha"]

    # Faz o processamento.
    logado = db_fazer_login(login, senha)

    # Monta a resposta.
    if logado is None:
        return render_template("index.html", erro = "Ops. A senha estava errada.")
    resposta = make_response(redirect("/"))

    # Armazena o login realizado com sucesso em cookies (autenticação).
    resposta.set_cookie("login", login, samesite = "Strict")
    resposta.set_cookie("senha", senha, samesite = "Strict")
    return resposta

@app.route("/logout", methods = ["POST"])
def logout():
    # Monta a resposta.
    resposta = make_response(render_template("index.html", mensagem = "Tchau."))

    # Limpa os cookies com os dados de login (autenticação).
    resposta.set_cookie("login", "", samesite = "Strict")
    resposta.set_cookie("senha", "", samesite = "Strict")
    return resposta


## Dasboard ####


@app.route("/dashmaster")
def dashmaster():
    # Autenticação.
    logado = autenticar_login()
    if logado is None:
        return redirect("/")
    if logado['tipo']=="admin":
        return render_template("dashmaster.html", logado = logado, mensagem = "")
    else:
        return render_template("dashvendedor.html", logado = logado, mensagem = "")  


### Cadastro de usuarios. ###

# Tela de listagem de usuarios.
@app.route("/usuarios")
def listar_usuarios_api():
    # Autenticação.
    logado = autenticar_login()
    if logado is None:
        return redirect("/")

    # Faz o processamento.
    lista = db_listar_usuarios()

    # Monta a resposta.
    return render_template("usuarios.html", logado = logado, usuarios = lista)

# Tela com o formulário de criação de usuario.
@app.route("/usuarios/novo", methods = ["GET"])
def form_criar_usuario_api():
    # Autenticação.
    logado = autenticar_login()
    if logado is None:
        return redirect("/")

    # Faz o processamento.
    usuario = {'id': 'novo', 'nome': '', 'login': '', 'senha': '', 'tipo': '', 'telefone': ''}

    # Monta a resposta.
    return render_template("form_usuario.html", logado = logado, usuario = usuario)

# Tela com o formulário de alteração de usuario existente.
@app.route("/usuarios/<int:id>", methods = ["GET"])
def form_alterar_usuario_api(id):
    # Autenticação.
    logado = autenticar_login()
    if logado is None:
        return redirect("/")

    # Faz o processamento.
    usuario = db_consultar_usuario(id)
    

    # Monta a resposta.
    if usuario is None:
        return render_template("usuarios.html", logado = logado, mensagem = f"Esse usuario não existe."), 404
    return render_template("form_usuario.html", logado = logado, convite = usuario)


### insumos ###
@app.route("/insumos")
def listar_insumos_api():
    # Autenticação.
    logado = autenticar_login()
    if logado is None:
        return redirect("/")

    # Faz o processamento.
    lista = db_listar_insumos()

    # Monta a resposta.
    return render_template("insumos.html", logado = logado, insumo = lista)

# Tela com o formulário de inserção de insumo.
@app.route("/insumos/novo", methods = ["GET"])
def form_inserir_insumo_api():
    # Autenticação.
    logado = autenticar_login()
    if logado is None:
        return redirect("/")

    # Faz o processamento.
    #aluno = {'id_aluno': 'novo', 'nome': '', 'sexo': '', 'id_serie': '', 'id_foto': ''}

    # Monta a resposta.
    return render_template("cad_insumo.html", logado = logado)




### estoque ###
@app.route("/estoque")
def listar_estoque_api():
    # Autenticação.
    logado = autenticar_login()
    if logado is None:
        return redirect("/")

    # Faz o processamento.
    lista = db_listar_estoque()

    # Monta a resposta.
    return render_template("estoque.html", logado = logado, produto = lista)


### caixa ###
@app.route("/caixa")
def listar_entradas_api():
    # Autenticação.
    logado = autenticar_login()
    if logado is None:
        return redirect("/")

    # Faz o processamento.
    lista = db_listar_saldo()
    lista1 = db_listar_entradas()
    lista2 = db_listar_saidas()

    # Monta a resposta.
    return render_template("caixa.html", logado = logado, saldo = lista, entradas = lista1, saidas = lista2)





###############################################
#### Coisas internas da controller da API. ####
###############################################

def extensao_arquivo(filename):
    if '.' not in filename: return ''
    return filename.rsplit('.', 1)[1].lower()

def salvar_arquivo_upload():
    import uuid
    if "foto" in request.files:
        foto = request.files["foto"]
        e = extensao_arquivo(foto.filename)
        if e in ['jpg', 'jpeg', 'png', 'gif', 'svg', 'webp']:
            u = uuid.uuid1()
            n = f"{u}.{e}"
            foto.save(os.path.join("alunos_fotos", n))
            return n
    return ""

def deletar_foto(id_foto):
    if id_foto == '': return
    p = os.path.join("alunos_fotos", id_foto)
    if os.path.exists(p):
        os.remove(p)

def autenticar_login():
    login = request.cookies.get("login", "")
    senha = request.cookies.get("senha", "")
    return db_fazer_login(login, senha)


##########################################
#### Definições de regras de negócio. ####
##########################################

def criar_usuario(nome, login, senha, tipo, telefone):
    return db_criar_usuario(nome, login, senha, tipo, telefone)

def editar_usuario(id, nome, login, senha, tipo, telefone):
    convite = db_consultar_usaurio(id)
    db_editar_usuario(id, nome, login, senha, tipo, telefone)
    return 'alterado', usuario

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
#### Definições básicas de DAO. ####
####################################


def conectar():
    return mysql.connector.connect(host="adducis.ch3noq1jgsa1.us-east-2.rds.amazonaws.com",user="adducis",password= "654artesanais",database="Usuarios")

def db_fazer_login(login, senha):
    with closing(conectar()) as con, closing(con.cursor()) as cur:
        cur.execute("SELECT login, senha, nome, tipo FROM usuario WHERE login = %s AND senha = %s;", (login, senha))
        return row_to_dict(cur.description, cur.fetchone())

def db_consultar_usuario(id):
    with closing(conectar()) as con, closing(con.cursor()) as cur:
        cur.execute("SELECT id, nome, login, senha, tipo FROM usuario WHERE a.id_aluno = %s;", (id_aluno))
        return row_to_dict(cur.description, cur.fetchone())


def db_listar_usuarios():
    with closing(conectar()) as con, closing(con.cursor()) as cur:
        cur.execute("SELECT id, nome, login, senha, tipo, telefone FROM usuario")
        return rows_to_dict(cur.description, cur.fetchall())


def db_criar_usuario(nome, login, senha, tipo, telefone):
    with closing(conectar()) as con, closing(con.cursor()) as cur:
        cur.execute("INSERT INTO usuario (nome, login, senha, tipo, telefone) VALUES (?, ?, ?, ?)", [nome, login, senha, tipo, telefone])
        id = cur.lastrowid
        con.commit()
        return {'id': id, 'nome': nome, 'login': login, 'senha': senha, 'tipo': tipo, 'telefone': telefone}

def db_editar_aluno(id, nome, login, senha, tipo, telefone):
    with closing(conectar()) as con, closing(con.cursor()) as cur:
        cur.execute("UPDATE aluno SET nome = ?, login = ?, senha = ?, tipo = ?, telefone = ? WHERE id = ?", [nome, login, senha, tipo, telefone, id])
        con.commit()
        return {'id': id, 'nome': nome, 'login': login, 'senha': senha, 'tipo': tipo, 'telefone': telefone}



def db_listar_insumos():
    with closing(conectar()) as con, closing(con.cursor()) as cur:
        cur.execute("SELECT I.id_insumo, I.nome_insumo, coalesce(sum(C.quantidade_insumo), '-') as soma,  min(date_format(C.data_vencimento, '%d-%m-%Y')) as vencimento FROM insumos AS I LEFT JOIN itemcompra AS C ON I.id_insumo = C.id_insumo Where C.data_vencimento > CURDATE() GROUP BY I.id_insumo")
        return rows_to_dict(cur.description, cur.fetchall())


def db_listar_estoque():
    with closing(conectar()) as con, closing(con.cursor()) as cur:
        cur.execute("SELECT P.id, P.nome_produto, sum(F.quantidade) - sum(V.quantidade) AS quantidade FROM produto as P LEFT JOIN itemfabricacao AS F ON P.id = F.id_produto LEFT JOIN itensvendas AS V ON P.id = V.id_produto GROUP BY P.id")
        return rows_to_dict(cur.description, cur.fetchall())

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




########################
#### Inicialização. ####
########################

if __name__ == "__main__":
    app.run(debug=True)