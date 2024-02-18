from flask import Flask, send_file
from listasEnlazadas.enlace import crearListaEnlazada
import graphviz
import importlib
import json

app = Flask(__name__)

@app.route('/get_graph_image')
def get_graph_image():

    try:
        spec = importlib.util.spec_from_file_location("", r"C:\Users\migue\Documents\Proyecto de Grado\Herramienta-Visualizacion-EDTs-v2023-11-14\Herramienta-Visualizacion-EDTs-v2023-11-14\referencias\lista_disc.py")
        foo = importlib.util.module_from_spec(spec)
  
        spec.loader.exec_module(foo)
        file = foo
        name = 'creation files/lista_enlazada_1.json'
        json_data = open(name)
        data = json.load(json_data)
    except:
        e = "\tProblema al cargar el archivo estatico " + name
        raise Exception (e)               
    return crearListaEnlazada(1, file,'Random', data)[1]
    

if __name__ == '__main__':
    app.run(debug=True)