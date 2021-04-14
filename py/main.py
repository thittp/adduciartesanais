from conexao import criar_conexao, fechar_conexao

def insere_usuario(con, nome, email, senha):
    cursor = con.cursor()
    sql = "iNSERT INTO usuario (nome, email, senha) values (%s, %s, %s)"
    valores = (nome, email, senha)
    cursor.execute(sql, valores)
    cursor.close()
    con.commit()


def main():
    con = criar_conexao("adducis.ch3noq1jgsa1.us-east-2.rds.amazonaws.com", "adducis", "654artesanais", "Usuarios")

    fechar_conexao









def conectar(host, usuario, senha, banco):
    return mysql.connector.connect(host=host, user=usuario, password=senha, database=banco)


def fechar_conexao(con):
    return con.close()

    
def db_fazer_login(login, senha):
    with closing(conectar()) as con, closing(con.cursor()) as cur:
        cur.execute("SELECT u.login, u.senha, u.nome FROM usuario u WHERE u.login = ? AND u.senha = ?", [login, senha])
        return row_to_dict(cur.description, cur.fetchone())



if __name__ == "__main__":
    app.run()