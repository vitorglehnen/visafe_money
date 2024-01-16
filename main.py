from flask import Flask
from endpoints.categorias import categorias

app = Flask(__name__)
app.register_blueprint(categorias)

app.run(port=7777, host='0.0.0.0', debug=True)
