import mysql.connector


con = mysql.connector.connect(host="adducis.ch3noq1jgsa1.us-east-2.rds.amazonaws.com",user="adducis",password="654artesanais",database="Usuarios")



if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado ao servidor versão:", db_info)
    cursor = con.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print ("Conectado ao banco de dados", linha)
    cursor.execute("SELECT nome FROM usuario WHERE login='batman';")
    senha = cursor.fetchone()
    print ("O nome do batman é", senha)

if con.is_connected():
    cursor = con.cursor()
    cursor.execute("SELECT senha FROM Usuarios.usuario where login='batman';")
    senha = cursor.fetchone()
    print ("a senha de batman é", senha)

if con.is_connected():
    login = "batman"
    senha = "morcego"
    cursor = con.cursor()
    cursor.execute("SELECT login, senha, nome FROM usuario WHERE login = %s AND senha = %s;", (login, senha))
    senha = cursor.fetchone()
    print ("a", senha)




if con.is_connected():
    cursor.close()
    con.close()
    print("Conexão encerrada")