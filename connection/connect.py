import psycopg2 as db


def conexao_db():
    parametros = {
        "host": "localhost",
        "database": "visafe",
        "user": "postgres",
        "password": "postgres"}

    conexao = db.connect(**parametros)

    return conexao
