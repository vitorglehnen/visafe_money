from connection import connect


class Categoria:
    def __init__(self):
        self.__id = None
        self.__nome = None
        self.__conexao = connect.conexao_db()

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def registro_existente(self):
        cursor = self.__conexao.cursor()

        if self.__id is None:
            cursor.execute(f"""
                            SELECT ct_id
                            FROM categorias
                            WHERE ct_nome = '{self.__nome}';
                            """)
        else:
            cursor.execute(f"""
                            SELECT ct_id
                            FROM categorias
                            WHERE ct_nome = '{self.__nome}'
                            AND ct_id != {self.__id};
                            """)

        dataset = cursor.fetchall()
        cursor.close()

        return len(dataset)

    def insere_categoria(self):
        cursor = self.__conexao.cursor()
        cursor.execute(f"""
                        INSERT INTO categorias (ct_nome)
                        VALUES ('{self.__nome}');
                        """)
        cursor.close()
        self.__conexao.commit()

    def busca_categorias(self):
        cursor = self.__conexao.cursor()
        cursor.execute(f"""
                        SELECT ct_id, ct_nome
                        FROM categorias;
                        """)

        dataset = cursor.fetchall()
        cursor.close()

        return dataset

    def busca_categoria_por_nome(self):
        cursor = self.__conexao.cursor()
        cursor.execute(f"""
                        SELECT ct_id, ct_nome
                        FROM categorias
                        WHERE ct_nome = '{self.__nome}';
                        """)

        dataset = cursor.fetchall()
        cursor.close()

        return dataset

    def altera_categoria(self):
        cursor = self.__conexao.cursor()
        cursor.execute(f"""
                        UPDATE categorias
                        SET ct_nome = '{self.__nome}'
                        WHERE ct_id = {self.__id};
                        """)
        cursor.close()
        self.__conexao.commit()

    def excluir_categoria(self):
        cursor = self.__conexao.cursor()
        cursor.execute(f"""
                        DELETE FROM categorias
                        WHERE ct_id = {self.__id};
                        """)
        cursor.close()
        self.__conexao.commit()