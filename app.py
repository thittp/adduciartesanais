from flask import Flask, make_response, request, render_template, redirect, send_from_directory
from contextlib import closing
import mysql.connector
import os
import werkzeug



app = Flask(__name__)


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




### usuarios ###
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

# Tela com o formulário de criação de um novo usuario.
@app.route("/usuario/novo", methods = ["GET"])
def form_criar_usuario_api():
    # Autenticação.
    logado = autenticar_login()
    if logado is None:
        return redirect("/")

    # Faz o processamento.
    #aluno = {'id_aluno': 'novo', 'nome': '', 'sexo': '', 'id_serie': '', 'id_foto': ''}

    # Monta a resposta.
    return render_template("form_convite.html", logado = logado)



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

def db_consultar_usuario(id):
    with closing(conectar()) as con, closing(con.cursor()) as cur:
        cur.execute("SELECT id, nome, login, senha, tipo FROM usuario WHERE a.id_aluno = %s;", (id_aluno))
        return row_to_dict(cur.description, cur.fetchone())


def db_listar_usuarios():
    with closing(conectar()) as con, closing(con.cursor()) as cur:
        cur.execute("SELECT id, nome, login, senha, telefone, tipo FROM usuario")
        return rows_to_dict(cur.description, cur.fetchall())

def db_fazer_login(login, senha):
    with closing(conectar()) as con, closing(con.cursor()) as cur:
        cur.execute("SELECT login, senha, nome, tipo FROM usuario WHERE login = %s AND senha = %s;", (login, senha))
        return row_to_dict(cur.description, cur.fetchone())



def db_listar_insumos():
    with closing(conectar()) as con, closing(con.cursor()) as cur:
        cur.execute("SELECT I.id_insumo, I.nome_insumo, coalesce(sum(C.quantidade_insumo), '-') as soma FROM insumos AS I LEFT JOIN itemcompra AS C ON I.id_insumo = C.id_insumo GROUP BY I.id_insumo")
        return rows_to_dict(cur.description, cur.fetchall())

########################
#### Inicialização. ####
########################

if __name__ == "__main__":
    app.run(debug=True)