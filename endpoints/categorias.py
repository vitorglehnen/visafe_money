from flask import Flask, jsonify, request, Blueprint, make_response, Response
from useful.make_response import make_response
from entities.categoria import Categoria

categorias = Blueprint('categorias', __name__)


@categorias.route('/categorias/incluir', methods=['POST'])
def categorias_incluir():
    categoria_object = Categoria()
    categoria_object.set_nome(request.json['nome'])

    if categoria_object.get_nome() == '':
        response = {
            "response": "O campo nome é obrigatório!"
        }
        return jsonify(response['response'])

    if categoria_object.registro_existente() > 0:
        status_code = 409
        resposta_erro = {
            "status_code": status_code,
            "response": "Categoria cadastrada já com o mesmo nome!"
        }

        return make_response(resposta_erro, status_code)

    categoria_object.insere_categoria()

    status_code = 201
    resposta_sucesso = {
        "status_code": status_code,
        "response": "Categoria inserida com sucesso!",
        "nome": categoria_object.get_nome()
    }

    return make_response(resposta_sucesso, status_code)


@categorias.route('/categorias/listar', methods=['GET'])
def listar_categorias():
    categoria_object = Categoria()

    categorias_cadastradas = categoria_object.busca_categorias()

    if len(categorias_cadastradas) == 0:
        code_status = 404
        response = {
            "status_code": code_status,
            "response": "Nenhuma categoria cadastrada!"
        }
        return jsonify(response['response'])

    categorias = []

    for registro in categorias_cadastradas:
        categorias.append({
            'codigo': registro[0],
            'nome': registro[1]
        })

    resposta = {
        'categorias': categorias
    }

    return make_response(resposta, 200)


@categorias.route('/categorias/alterar/<id>', methods=['PUT'])
def alterar_categoria(id):
    categoria_object = Categoria()

    categoria_object.set_nome(request.json['nome'])
    categoria_object.set_id(id)

    if categoria_object.get_nome() == '':
        response = {
            "response": "O campo nome é obrigatório!"
        }
        return jsonify(response['response'])

    if categoria_object.registro_existente() > 0:
        status_code = 409
        resposta_erro = {
            "status_code": status_code,
            "response": "Categoria cadastrada já com o mesmo nome!"
        }

        return make_response(resposta_erro, status_code)

    categoria_object.altera_categoria()

    status_code = 200
    resposta_sucesso = {
        "status_code": status_code,
        "response": "Categoria alterada com sucesso!",
        "nome": categoria_object.get_nome()
    }

    return make_response(resposta_sucesso, status_code)


@categorias.route('/categorias/excluir/<id>', methods=['DELETE'])
def excluir_categoria(id):
    categoria_object = Categoria()
    categoria_object.set_id(id)

    if categoria_object.registro_existente() == 0:
        status_code = 404
        resposta_erro = {
            "status_code": status_code,
            "response": "Categoria não encontrada!"
        }

        return make_response(resposta_erro, status_code)

    categoria_object.excluir_categoria()

    status_code = 200
    resposta_sucesso = {
        "status_code": status_code,
        "response": "Categoria deletada com sucesso!",
        "id": categoria_object.get_id()
    }

    return make_response(resposta_sucesso, status_code)
