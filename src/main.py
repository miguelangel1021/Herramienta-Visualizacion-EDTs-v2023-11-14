from flask import Flask, send_file
from listasEnlazadas.enlace import crearListaEnlazada
import graphviz
import importlib
import json
import config as cf
from blueprints.requests import request_blueprint
from errors.errors import ApiError
from flask import Flask, jsonify
from flask_cors import CORS



app = Flask(__name__)

CORS(app)

app.register_blueprint(request_blueprint)


@app.errorhandler(ApiError)
def handle_exception(err):
    response = {
      "msg": err.description
    }
    return jsonify(response), err.code

if __name__ == '__main__':
    app.run(debug=True)