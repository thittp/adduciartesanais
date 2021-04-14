from flask import Flask, make_response, request, render_template, redirect, send_from_directory
from contextlib import closing
import mysql.connector
import os
import werkzeug

app = Flask(__name__)



@app.route("/")
@app.route("/login")
def menu():
    # Autenticação.
    logado = autenticar_login()
    if logado is None:
        return render_template("/login.html", erro = "")

    # Monta a resposta.
    return render_template("admimaster.html", logado = logado, mensagem = "")

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
        return render_template("login.html", erro = "Ops. A senha estava errada.")
    resposta = make_response(redirect("/"))

    # Armazena o login realizado com sucesso em cookies (autenticação).
    resposta.set_cookie("login", login, samesite = "Strict")
    resposta.set_cookie("senha", senha, samesite = "Strict")
    return resposta

@app.route("/logout", methods = ["POST"])
def logout():
    # Monta a resposta.
    resposta = make_response(render_template("login.html", mensagem = "Tchau."))

    # Limpa os cookies com os dados de login (autenticação).
    resposta.set_cookie("login", "", samesite = "Strict")
    resposta.set_cookie("senha", "", samesite = "Strict")
    return resposta






def autenticar_login():
    login = request.cookies.get("login", "")
    senha = request.cookies.get("senha", "")
    return db_fazer_login(login, senha)




def conectar(host, usuario, senha, banco):
    return mysql.connector.connect(host=host, user=usuario, password=senha, database=banco)

def db_inicializar():
    with closing(conectar()) as con, closing(con.cursor()) as cur:
        cur.executescript(sql_create)
        con.commit()


def fechar_conexao(con):
    return con.close()



def db_fazer_login(login, senha):
    with closing(conectar()) as con, closing(con.cursor()) as cur:
        cur.execute("SELECT u.login, u.senha, u.nome FROM usuario u WHERE u.login = ? AND u.senha = ?", [login, senha])
    return row_to_dict(cur.description, cur.fetchone())









    
########################
#### Inicialização. ####
########################

if __name__ == "__main__":
#    db_inicializar()
    app.run()