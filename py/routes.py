from flask import Flask, make_response, request, render_template, redirect, send_from_directory
from main import insere_usuario
app = Flask("banco_adducis")

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




app.run()