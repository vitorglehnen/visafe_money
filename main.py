from flask import Flask
from endpoints.categorias import categorias
from endpoints.usuarios import usuarios

app = Flask(__name__)
app.register_blueprint(categorias)
app.register_blueprint(usuarios)

app.run(port=7777, host='0.0.0.0', debug=True)
