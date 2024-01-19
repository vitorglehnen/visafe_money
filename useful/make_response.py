import json
from flask import Response


def make_response(mensagem, status_code):
    return Response(response=json.dumps(mensagem, ensure_ascii=False, sort_keys=False, indent=2), status=status_code, content_type='application/json; charset=utf-8')