from connection import connect


class Usuario:
    def __init__(self):
        self.__id = None
        self.__nome = None
        self.__senha = None
        self.__saldo_conta = None

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_senha(self):
        return self.__senha

    def set_senha(self, senha):
        self.__senha = senha

    def get_saldo_conta(self):
        return self.__saldo_conta

    def set_saldo_conta(self, saldo_conta):
        self.__saldo_conta = saldo_conta

    def registro_existente(self):
        conexao = connect.conexao_db()
        cursor = conexao.cursor()

        if self.__id is None:
            cursor.execute(f"""
                            SELECT us_id
                            FROM usuarios
                            WHERE us_nome = '{self.__nome}';
                            """)
        else:
            cursor.execute(f"""
                            SELECT us_id
                            FROM usuarios
                            WHERE us_nome = '{self.__nome}'
                            AND us_id != {self.__id};
                            """)

        dataset = cursor.fetchall()
        cursor.close()

        return len(dataset)

    def insere_usuario(self):
        conexao = connect.conexao_db()
        cursor = conexao.cursor()
        cursor.execute(f"""
                        INSERT INTO usuarios (us_nome, us_senha, us_saldoconta)
                        VALUES ('{self.__nome}', '{self.__senha}', 0);
                        """)
        cursor.close()
        conexao.commit()

    def busca_usuarios(self):
        conexao = connect.conexao_db()
        cursor = conexao.cursor()
        cursor.execute(f"""
                        SELECT us_id, us_nome, us_saldo_conta
                        FROM usuarios;
                        """)

        dataset = cursor.fetchall()
        cursor.close()

        return dataset

    def busca_usuario_por_nome(self):
        conexao = connect.conexao_db()
        cursor = conexao.cursor()
        cursor.execute(f"""
                        SELECT us_id
                        FROM usuarios
                        WHERE us_nome = '{self.__nome}';
                        """)

        dataset = cursor.fetchall()
        cursor.close()

        return dataset
