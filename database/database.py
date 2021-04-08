import mysql.connector as sql_db

class Conexao:

    def __init__(self, host, user, password, database):
        super.host = host
        super.user = user
        super.password = password
        super.database = database

    def connectMYSQL(super):
        database  = sql_db.connect(
            host=super.host,
            user=super.user,
            password=super.password,
            database=super.database
        )
        return database