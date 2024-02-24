from flask import Flask, jsonify, request, Blueprint, make_response, Response
from useful.make_response import make_response
from entities.usuario import Usuario

usuarios = Blueprint('usuarios', __name__)


@usuarios.route('/usuarios/incluir', methods=['POST'])
def incluir_categoria():
    usuario_object = Usuario()

    usuario_object.set_nome(request.json['nome'])
    usuario_object.set_senha(request.json['senha'])

    if usuario_object.get_nome() == '':
        response = {
            "response": "O campo nome é obrigatório!"
        }
        return jsonify(response['response'])
    if usuario_object.get_senha() == '':
        response = {
            "response": "O campo senha é obrigatório!"
        }
        return jsonify(response['response'])

    if usuario_object.registro_existente() > 0:
        status_code = 409
        resposta_erro = {
            "status_code": status_code,
            "response": "Usuário cadastrado já com o mesmo nome!"
        }

        return make_response(resposta_erro, status_code)

    usuario_object.insere_usuario()
    usuario_object.set_id(usuario_object.busca_usuario_por_nome()[0][0])

    status_code = 201
    resposta_sucesso = {
        "status_code": status_code,
        "response": "usuario inserida com sucesso!",
        "codigo": usuario_object.get_id(),
        "nome": usuario_object.get_nome()
    }

    return make_response(resposta_sucesso, status_code)


@usuarios.route('/usuarios/listar', methods=['GET'])
def listar_usuario():
    usuario_object = Usuario()

    usuarios_cadastradas = usuario_object.busca_usuarios()

    if len(usuarios_cadastradas) == 0:
        code_status = 404
        response = {
            "status_code": code_status,
            "response": "Nenhuma usuario cadastrada!"
        }
        return jsonify(response['response'])

    usuarios = []

    for registro in usuarios_cadastradas:
        usuarios.append({
            'codigo': registro[0],
            'nome': registro[1]
        })

    resposta = {
        'usuarios': usuarios
    }

    return make_response(resposta, 200)


@usuarios.route('/usuarios/alterar/<id>', methods=['PUT'])
def alterar_usuario(id):
    usuario_object = Usuario()

    usuario_object.set_nome(request.json['nome'])
    usuario_object.set_id(id)

    if usuario_object.get_nome() == '':
        response = {
            "response": "O campo nome é obrigatório!"
        }
        return jsonify(response['response'])

    if usuario_object.registro_existente() > 0:
        status_code = 409
        resposta_erro = {
            "status_code": status_code,
            "response": "usuario cadastrada já com o mesmo nome!"
        }

        return make_response(resposta_erro, status_code)

    usuario_object.altera_usuario()

    status_code = 200
    resposta_sucesso = {
        "status_code": status_code,
        "response": "usuario alterada com sucesso!",
        "nome": usuario_object.get_nome()
    }

    return make_response(resposta_sucesso, status_code)


@usuarios.route('/usuarios/excluir/<id>', methods=['DELETE'])
def excluir_usuario(id):
    usuario_object = Usuario()
    usuario_object.set_id(id)

    if usuario_object.registro_existente() == 0:
        status_code = 404
        resposta_erro = {
            "status_code": status_code,
            "response": "usuario não encontrada!"
        }

        return make_response(resposta_erro, status_code)

    usuario_object.excluir_usuario()

    status_code = 200
    resposta_sucesso = {
        "status_code": status_code,
        "response": "usuario deletada com sucesso!",
        "id": usuario_object.get_id()
    }

    return make_response(resposta_sucesso, status_code)
