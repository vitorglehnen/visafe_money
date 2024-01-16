import json
from flask import Flask, jsonify, request, Blueprint, make_response
from connection import connect

conexao = connect.conexao_db()
categorias = Blueprint('categorias', __name__)


@categorias.route('/categorias/incluir', methods=['POST'])
def categorias_incluir():
    nome = request.json['nome']

    if nome == '':
        response = {
            "response": "O valor de codbuff não pode estar vazio!"
        }
        return jsonify(response['response'])

    cursor = conexao.cursor()
    cursor.execute(f"""
                    INSERT INTO categorias.item(nome)
	                VALUES ({nome})
                    """)

    conexao.commit()
    cursor.close()

    return jsonify('Categoria inserida com sucesso!')


@categorias.route('/categorias/listar', methods=['GET'])
def listar_categorias():
    cursor = conexao.cursor()

    cursor.execute(f"""
                    SELECT ct_id, ct_nome
	                FROM public.categorias;
                    """)

    dataset = cursor.fetchall()
    cursor.close()

    if len(dataset) == 0:
        return jsonify("Nenhuma categoria existente na base de dados!")

    categorias = []

    for registro in dataset:
        categorias.append({
            'codigo': registro[0],
            'nome': registro[1]
        })

    response = {
        'categorias': categorias
    }

    return make_response(jsonify(response), 200)