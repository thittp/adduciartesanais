from flask import Flask, make_response, request, render_template, redirect, send_from_directory
from contextlib import closing
import regras as rg
import bd as bd
import os
import werkzeug

#import matplotlib as plt



app = Flask(__name__)

### Partes de login. ###
@app.route("/")
@app.route("/login")
def menu():
    logado = autenticar_login()
    if logado is None:
        return render_template("/login.html", erro = "")
    if logado['tipo']=="admin":
        return redirect('/caixa')
    else:
        return redirect('/caixa')


@app.route("/login", methods = ["POST"])
def login():
    # Extrai os dados do formulário.
    f = request.form
    if "login" not in f or "senha" not in f:
        return ":(", 422
    login = f["login"]
    senha = f["senha"]

    # Faz o processamento.
    logado = bd.db_fazer_login(login, senha)

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
    lista = bd.db_listar_usuarios()

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
    usuario = bd.db_consultar_usuario(id)
    

    # Monta a resposta.
    if usuario is None:
        # Faz o processamento.
        lista = bd.db_listar_usuarios()
        return render_template("usuarios.html", logado = logado, usuarios = lista, mensagem = f"Esse usuario não existe."), 404
    return render_template("form_usuario.html", logado = logado, usuario = usuario)

# Processa o formulário de criação de usuarios. 
@app.route("/usuarios/novo", methods = ["POST"])
def criar_usuario_api():
    # Autenticação.
    logado = autenticar_login()
    if logado is None:
        return redirect("/")

    # Extrai os dados do formulário.
    nome = request.form["nome"]
    login = request.form["login"]
    senha = request.form["senha"]
    tipo = request.form["tipo"]
    telefone = request.form["telefone"]

    # Faz o processamento.
    usuario = rg.criar_usuario(nome, login, senha, tipo, telefone)

    # Monta a resposta.
    mensagem = f"O usuario {nome} foi criado com o id {usuario['id']}."
    # Faz o processamento.
    lista = bd.db_listar_usuarios()
    return render_template("usuarios.html", usuarios = lista, logado = logado, mensagem = mensagem)

# Processa o formulário de alteração de usuarios.
@app.route("/usuarios/<int:id>", methods = ["POST"])
def editar_usuario_api(id):
    # Autenticação.
    logado = autenticar_login()
    if logado is None:
        return redirect("/")

    # Extrai os dados do formulário.
    nome = request.form["nome"]
    login = request.form["login"]
    senha = request.form["senha"]
    tipo = request.form["tipo"]
    telefone = request.form["telefone"]

    # Faz o processamento.
    status, usuario = rg.editar_usuario(id, nome, login, senha, tipo, telefone)
    lista = bd.db_listar_usuarios()

    # Monta a resposta.
    if status == 'não existe':
        mensagem = "Esse usuario nem mesmo existia mais."
        return render_template("usuarios.html", logado = logado, usuarios = lista, mensagem = mensagem), 404
    mensagem = f"O usuario {nome} com o id {id} foi editado."
    return render_template("usuarios.html", logado = logado, usuarios = lista, mensagem = mensagem)

# Processa o botão de excluir um usuarios.
@app.route("/usuarios/<int:id>", methods = ["DELETE"])
def deletar_usuario_api(id):
    # Autenticação.
    logado = autenticar_login()
    if logado is None:
        return redirect("/")

    # Faz o processamento.
    usuario = rg.apagar_usuario(id)
    lista = bd.db_listar_usuarios()

    # Monta a resposta.
    if usuario is None:
        return render_template("usuarios.html", logado = logado, usuarios = lista, mensagem = "Esse usuario nem mesmo existia mais."), 404
    mensagem = f"O usuario com o id {id} foi excluído."
    return render_template("usuarios.html", logado = logado, usuarios = lista, mensagem = mensagem)



### Produtos ###
@app.route("/produtos")
def listar_prosutos_api():
    # Autenticação.
    logado = autenticar_login()
    if logado is None:
        return redirect("/")

    # Faz o processamento.
    lista = bd.db_listar_produtos()

    # Monta a resposta.
    return render_template("produtos.html", logado = logado, produto = lista)
    



### insumo ###
@app.route("/insumo")
def listar_insumo_api():
    # Autenticação.
    logado = autenticar_login()
    if logado is None:
        return redirect("/")

    # Faz o processamento.
    lista = bd.db_listar_insumo()

    # Monta a resposta.
    return render_template("insumo.html", logado = logado, insumo = lista)

# Tela com o formulário de criação de insumo.
@app.route("/insumo/novo", methods = ["GET"])
def form_criar_insumo_api():
    # Autenticação.
    logado = autenticar_login()
    if logado is None:
        return redirect("/")

    # Faz o processamento.
    insumo = {'id_insumo': 'novo', 'nome': ''}

    # Monta a resposta.
    return render_template("cad_insumo.html", logado = logado, insumo = insumo)

# Tela com o formulário de alteração de insumo existente.
@app.route("/insumo/<int:id_insumo>", methods = ["GET"])
def form_alterar_insumo_api(id_insumo):
    # Autenticação.
    logado = autenticar_login()
    if logado is None:
        return redirect("/")

    # Faz o processamento.
    insumo = bd.db_consultar_insumo(id_insumo)
    

    # Monta a resposta.
    if insumo is None:
        return render_template("insumo.html", logado = logado, mensagem = f"Esse insumo não existe."), 404
    return render_template("cad_insumo.html", logado = logado, insumo = insumo)

# Processa o formulário de criação de insumo. 
@app.route("/insumo/novo", methods = ["POST"])
def criar_insumo_api():
    # Autenticação.
    logado = autenticar_login()
    if logado is None:
        return redirect("/")

    # Extrai os dados do formulário.
    nome = request.form["nome"]

    # Faz o processamento.
    insumo = rg.criar_insumo(nome)

    # Monta a resposta.
    mensagem = f"O Insumo foi criado com o id."
    return redirect('/insumo')
    #redirect('/insumo')


# Processa o formulário de alteração de insumo.
@app.route("/insumo/<int:id_insumo>", methods = ["POST"])
def editar_insumo_api(id_insumo):
    # Autenticação.
    logado = autenticar_login()
    if logado is None:
        return redirect("/")

    # Extrai os dados do formulário.
    nome = request.form["nome"]


    # Faz o processamento.
    status, insumo = rg.editar_insumo(id_insumo, nome)

    # Monta a resposta.
    if status == 'não existe':
        mensagem = "Esse insumo nem mesmo existia mais."
        return render_template("insumo.html", logado = logado, mensagem = mensagem), 404
    mensagem = f"O insumo {nome} com o id {id_insumo} foi editado."
    return render_template("insumo.html", logado = logado, mensagem = mensagem)


### compra ###
@app.route("/insumo/compra")
def listar_compra_api():
    # Autenticação.
    logado = autenticar_login()
    if logado is None:
        return redirect("/")

    # Faz o processamento.
    lista = bd.db_listar_compra()

    # Monta a resposta.
    return render_template("compra.html", logado = logado, compra = lista)

# Tela com o formulário de criação de compra.
@app.route("/insumo/compra/novo", methods = ["GET"])
def form_criar_compra_api():
    # Autenticação.
    logado = autenticar_login()
    if logado is None:
        return redirect("/")

    # Faz o processamento.
  
    compra = {'id_compra': 'novo', 'data_compra': '', 'preco_compra': ''}

    # Monta a resposta.
    return render_template("cad_compra.html", logado = logado, compra = compra)


# Processa o formulário de criação de compra. 
@app.route("/insumo/compra/novo", methods = ["POST"])
def criar_compra_api():
    # Autenticação.
    logado = autenticar_login()
    if logado is None:
        return redirect("/")

    # Extrai os dados do formulário.
    data_compra = request.form["data_compra"]
    preco_compra = request.form["preco_compra"]

    # Faz o processamento.
    compra = rg.criar_compra(data_compra, preco_compra)

    # Monta a resposta.
    mensagem = f"O aluno  foi criado com o id ."
    return redirect('/insumo')



### itemcompra ###
@app.route("/insumo/compra/item<int:id_compra>")
def listar_itemcompra_api(id_compra):
    # Autenticação.
    logado = autenticar_login()
    if logado is None:
        return redirect("/")

    # Faz o processamento.
    compra = bd.db_consultar_compra(id_compra)
    itemcompra = bd.db_listar_item()

    # Monta a resposta.
    return render_template("item_compra.html", logado = logado, compra = compra, itemcompra = itemcompra)








### estoque ###
@app.route("/estoque")
def listar_estoque_api():
    # Autenticação.
    logado = autenticar_login()
    if logado is None:
        return redirect("/")

    # Faz o processamento.
    lista = bd.db_listar_estoque()

    # Monta a resposta.
    return render_template("estoque.html", logado = logado, produto = lista)


### Produto ###
# Tela com o formulário de criação de produto.
@app.route("/produtos/novo", methods = ["GET"])
def form_criar_produto_api():
    # Autenticação.
    logado = autenticar_login()
    if logado is None:
        return redirect("/")

    # Faz o processamento.
    produto = {'id_produto': 'novo', 'nome': '', 'preco_atual': '', 'ingredientes': '', 'prazo_validade':'', 'descricao':''}

    # Monta a resposta.
    return render_template("cad_produto.html", logado = logado, produto = produto)

# Tela com o formulário de alteração de produto existente.
@app.route("/estoque/<int:id_produto>", methods = ["GET"])
def form_alterar_produto_api(id_produto):
    # Autenticação.
    logado = autenticar_login()
    if logado is None:
        return redirect("/")

    # Faz o processamento.
    produto = bd.db_consultar_produto(id_produto)
    

    # Monta a resposta.
    if produto is None:
        return render_template("estoque.html", logado = logado, mensagem = f"Esse produto não existe."), 404
    return render_template("cad_produto.html", logado = logado, produto = produto)


# Processa o formulário de criação de produto.
@app.route("/produtos/novo", methods = ["POST"])
def criar_produto_api():
    # Autenticação.
    logado = autenticar_login()
    if logado is None:
        return redirect("/")

    # Extrai os dados do formulário.
    nome = request.form["nome"]
    preco_atual = request.form["preco_atual"]
    ingredientes = request.form["ingredientes"]
    prazo_validade = request.form["prazo_validade"]
    descricao = request.form["descricao"]

    # Faz o processamento.
    produto = rg.criar_produto(nome, preco_atual, ingredientes, prazo_validade, descricao)

    # Monta a resposta.
    mensagem = f"O usuario {nome} foi criado com o id {produto['id_produto']}."
    return redirect('/produtos')
    #render_template("estoque.html", logado = logado, mensagem = mensagem)



# Processa o formulário de alteração de produto.
@app.route("/estoque/<int:id_produto>", methods = ["POST"])
def editar_produto_api(id_produto):
    # Autenticação.
    logado = autenticar_login()
    if logado is None:
        return redirect("/")

    # Extrai os dados do formulário.
    nome = request.form["nome"]


    # Faz o processamento.
    status, produto = rg.editar_produto(id_produto, nome)

    # Monta a resposta.
    if status == 'não existe':
        mensagem = "Esse produto nem mesmo existia mais."
        return render_template("estoque.html", logado = logado, mensagem = mensagem), 404
    mensagem = f"O produto {nome} com o id {id} foi editado."
    return render_template("produto.html", logado = logado, mensagem = mensagem)


#Fabricação#
@app.route("/fabricacao")
def listar_fabricacao_api():
    # Autenticação.
    logado = autenticar_login()
    if logado is None:
        return redirect("/")

    # Faz o processamento.
    lista = bd.db_listar_fabricacao()

    # Monta a resposta.
    return render_template("fabricacao.html", logado = logado, fabricacao = lista)


# Tela com o formulário de criação de fabricação.
@app.route("/estoque/novafabricacao", methods = ["GET"])
def form_criar_fabricacao_api():
    # Autenticação.
    logado = autenticar_login()
    if logado is None:
        return redirect("/")

    # Faz o processamento.
    fabricacao = {'id_produto': 'novo', 'data_fabricacao': ''}

    # Monta a resposta.
    return render_template("cad_fabricacao.html", logado = logado, fabricacao = fabricacao)

# Tela com o formulário de alteração de fabricacao existente.


# Processa o formulário de criação de fabricacao.
@app.route("/estoque/novafabricacao", methods = ["POST"])
def criar_fabricacao_api():
    # Autenticação.
    logado = autenticar_login()
    if logado is None:
        return redirect("/")

    # Extrai os dados do formulário.
    data_fabricacao = request.form["data_fabricacao"]

    # Faz o processamento.
    fabricacao = rg.criar_fabricacao(data_fabricacao)

    # Monta a resposta.
    mensagem = f"O usuario {nome} foi criado com o id {fabricacao['id_fabricacao']}."
    return render_template("fabricacao.html", logado = logado, mensagem = mensagem)



# Processa o formulário de alteração de fabricacao.

# Tela com o formulário de criação de novo item de fabricação.
@app.route("/fabricação/novo", methods = ["GET"])
def form_criar_itemfabricacao_api():
    # Autenticação.
    logado = autenticar_login()
    if logado is None:
        return redirect("/")

    # Faz o processamento.
    itemfabricacao = {'id_item': 'novo', 'id_fabricacao': '', 'id_produto': '', 'quantidade': '', 'prazo_vencimento': ''}

    # Monta a resposta.
    return render_template("cad_itemfabricacao.html", logado = logado, itemfabricacao = itemfabricacao)














### caixa ###
@app.route("/caixa")
def listar_entradas_api():
    # Autenticação.
    logado = autenticar_login()
    if logado is None:
        return redirect("/")

    # Faz o processamento.
    lista = bd.db_listar_saldo()
    lista1 = bd.db_listar_entradas()
    lista2 = bd.db_listar_saidas()

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
    return bd.db_fazer_login(login, senha)





########################
#### Inicialização. ####
########################

if __name__ == "__main__":
    app.run(debug=True)