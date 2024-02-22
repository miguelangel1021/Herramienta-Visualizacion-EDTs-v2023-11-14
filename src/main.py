from flask import Flask, send_file
from listasEnlazadas.enlace import crearListaEnlazada
import graphviz
import importlib
import json
import config as cf
from blueprints.requests import request_blueprint, lista_blueprint
from errors.errors import ApiError
from flask import Flask, jsonify



app = Flask(__name__)


app.register_blueprint(request_blueprint)
app.register_blueprint(lista_blueprint)
@app.errorhandler(ApiError)
def handle_exception(err):
    response = {
      "mssg": err.description
    }
    return jsonify(response), err.code

if __name__ == '__main__':
    app.run(debug=True)