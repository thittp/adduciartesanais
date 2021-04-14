import pymysql.cursors

#conexão
con = pymysql.connect (host="adducis.ch3noq1jgsa1.us-east-2.rds.amazonaws.com",user="adducis",password="654artesanais",database="Usuarios", cursorclass=pymysql.cursors.DictCursor)


#preprarar metodo .cursor()
with con.cursor() as c:
    #Crirar uma consuta
    sql = "SELECT senha FROM usuario WHERE login=batman;"
    c.execute(sql)
    res = c.fetchone()

if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado ao servidor versão:", db_info)
    cursor = con.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print ("Conectado ao banco de dados", linha)
    senha = cursor.execute("SELECT * FROM usuario where login='batman';")
    print ("a senha de batman é", senha)

if con.is_connected():
    cursor = con.cursor()
    senha = cursor.execute("SELECT senha FROM Usuarios.usuario where login='batman';")
    print ("a senha de batman é", senha)


if con.is_connected():
    cursor.close()
    con.close()
    print("Conexção encerrada")