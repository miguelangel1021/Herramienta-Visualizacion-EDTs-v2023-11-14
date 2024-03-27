from models.model import Actual
from flask import jsonify, request, Blueprint, Response, make_response
import importlib
import json
import config as cf
from listasEnlazadas.enlace import crearListaEnlazada,anadirNodoLista,anadirNodoListaFirst,eliminarNodoLista,encontrarNodoLista,findAdjacentNodeLista,darTodosLosNodos
from soporte.soporte import validarEstructura
from errors.errors import DefaultError
from io import BytesIO
import base64


actual=Actual(None, None, None, None)
request_blueprint = Blueprint('config', __name__)



@request_blueprint.route('/config/type', methods= ['POST'])
def asignarEstructura():
    json = request.get_json()
    actual.type = json.get('type')
    return '',200

@request_blueprint.route('/config/cargar', methods= ['POST'])
def cargarArchvio():
    pass

@request_blueprint.route('/config/porDefecto', methods= ['POST'])
def cargarArchvioPorDefecto():
    spec = importlib.util.spec_from_file_location("",  cf.data_dir + "\\referencias\lista_disc.py")
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)
    actual.file = foo
    return '',200

@request_blueprint.route('/config/restart', methods= ['POST'])
def restart():
    actual.data = None
    actual.file = None
    actual.estructura = None
    actual.type = None
    return '',200



#Listas Enlazadas
lista_blueprint = Blueprint('listas', __name__)


@request_blueprint.route('/listas/crearVacio', methods= ['GET'])
def crearListaVacia():
    try:
        respuesta = crearListaEnlazada(actual.type, actual.file, "Vacia")
    except Exception as e:
        raise DefaultError(e)
    actual.estructura = respuesta[0]
    info = respuesta[2]
    image_base64 = base64.b64encode(respuesta[1]).decode('utf-8')
    # Crear un objeto JSON que contenga tanto la imagen SVG como la información adicional
    response_data = {
        'svg_image': image_base64,
        'info': info
    }
    return jsonify(response_data),200

@request_blueprint.route('/listas/crearEstatica', methods= ['GET'])
def crearListaEstatica():
    try:
        name = 'creation files/lista_enlazada_1.json'
        json_data = open(name)
        data = json.load(json_data)
        print(data)
    except:
        e = "\tProblema al cargar el archivo estatico " + name
        raise DefaultError(e)
    try:               
        respuesta = crearListaEnlazada(actual.type, actual.file, "Estática", data)
    except Exception as e:
        raise DefaultError(e)
    actual.estructura = respuesta[0]
    info = respuesta[2]
    image_base64 = base64.b64encode(respuesta[1]).decode('utf-8')
    # Crear un objeto JSON que contenga tanto la imagen SVG como la información adicional
    response_data = {
        'svg_image': image_base64,
        'info': info
    }
    return jsonify(response_data),200


@request_blueprint.route('/listas/crearArchivo', methods= ['GET'])
def crearListaArchivo():
    pass

"""@request_blueprint.route('/listas/crearRandom', methods= ['GET'])
def crearListaRandom():
    init = "Random"
    respuesta = crearListaEnlazada(actual.type, actual.file, init)
    actual.estructura = respuesta[0]

    response = make_response(respuesta[1])

    # Establecer el tipo de contenido
    response.headers['Content-Type'] = 'image/svg+xml'

    # Establecer los encabezados con la información adicional
    info = respuesta[2]
    response.headers['msj'] = info["msj"]
    response.headers['estado'] = info["estado"]
    response.headers['comment'] = info["comment"]
    response.headers['size'] = info["size"]
    return response,200"""

@request_blueprint.route('/listas/crearRandom', methods=['GET'])
def crearListaRandom():
    init = "Random"
    try:
        respuesta = crearListaEnlazada(actual.type, actual.file, init)
    except Exception as e:
        raise DefaultError(e)
    
    actual.estructura = respuesta[0]
    # Obtener la información adicional
    info = respuesta[2]
    # Convertir la imagen SVG a una cadena
    image_base64 = base64.b64encode(respuesta[1]).decode('utf-8')
    # Crear un objeto JSON que contenga tanto la imagen SVG como la información adicional
    response_data = {
        'svg_image': image_base64,
        'info': info
    }
    # Devolver el objeto JSON junto con la imagen SVG
    return jsonify(response_data), 200



@request_blueprint.route('/listas/AñadirNodo', methods= ['GET'])
def añadirNodoLista():
    json = request.get_json()
    value = json.get('value').strip()
    if len(value) > 0:
        try:
            try:
                data = int(value)
            except:
                data = value
            try:
                state, comment = validarEstructura([1,2], actual.type)
                if not state:
                        print(comment)
            except:
                raise DefaultError("La estructura no ha sido creada correctamente")
            if state:
                respuesta = anadirNodoLista(actual.estructura, actual.type, data)
        except Exception as e:
            raise DefaultError(e)

    actual.estructura = respuesta[0]

    info = respuesta[2]
    image_base64 = base64.b64encode(respuesta[1]).decode('utf-8')
    # Crear un objeto JSON que contenga tanto la imagen SVG como la información adicional
    response_data = {
        'svg_image': image_base64,
        'info': info
    }
    return jsonify(response_data),200

@request_blueprint.route('/listas/AñadirPrincipio', methods= ['GET'])
def añadirNodoPrincipio():
    json = request.get_json()
    value = json.get('value').strip()
    if len(value) > 0:
        try:
            try:
                data = int(value)
            except:
                data = value
            try:
                state, comment = validarEstructura([1,2], actual.type)
                if not state:
                        print(comment)
            except:
                raise DefaultError("La estructura no ha sido creada correctamente")
            if state:
                respuesta = anadirNodoListaFirst(actual.estructura, actual.type, data)
        except Exception as e:
            raise DefaultError(e)

    actual.estructura = respuesta[0]
    info = respuesta[2]
    image_base64 = base64.b64encode(respuesta[1]).decode('utf-8')
    # Crear un objeto JSON que contenga tanto la imagen SVG como la información adicional
    response_data = {
        'svg_image': image_base64,
        'info': info
    }
    return jsonify(response_data),200


@request_blueprint.route('/listas/EliminarNodo', methods= ['GET'])
def eliminarNodo():
    json = request.get_json()
    value = json.get('value').strip()
    if len(value) > 0:
        try:
            try:
                data = int(value)
            except:
                data = value
            try:
                state, comment = validarEstructura([1,2], actual.type)
                if not state:
                        print(comment)
            except:
                raise DefaultError("La estructura no ha sido creada correctamente")
            if state:
                respuesta = eliminarNodoLista(actual.estructura, actual.type, data)
        except Exception as e:
            raise DefaultError(e)

    actual.estructura = respuesta[0]
    # Establecer los encabezados con la información adicional
    info = respuesta[2]
    image_base64 = base64.b64encode(respuesta[1]).decode('utf-8')
    # Crear un objeto JSON que contenga tanto la imagen SVG como la información adicional
    response_data = {
        'svg_image': image_base64,
        'info': info
    }
    return jsonify(response_data),200

@request_blueprint.route('/listas/EncontarNodo', methods= ['GET'])
def encontrarNodo():
    json = request.get_json()
    value = json.get('value').strip()
    if len(value) > 0:
        try:
            try:
                data = int(value)
            except:
                data = value
            try:
                state, comment = validarEstructura([1,2], actual.type)
                if not state:
                        print(comment)
            except:
                raise DefaultError("La estructura no ha sido creada correctamente")
            if state:
                respuesta = encontrarNodoLista(actual.estructura, actual.type, data)
        except Exception as e:
            raise DefaultError(e)

    actual.estructura = respuesta[0]
    
    info = respuesta[2]
    image_base64 = base64.b64encode(respuesta[1]).decode('utf-8')
    # Crear un objeto JSON que contenga tanto la imagen SVG como la información adicional
    response_data = {
        'svg_image': image_base64,
        'info': info
    }
    return jsonify(response_data),200

@request_blueprint.route('/listas/EncontarAdyacentes', methods= ['GET'])
def encontrarAdyacentes():
    json = request.get_json()
    value = json.get('value').strip()
    if len(value) > 0:
        try:
            try:
                data = int(value)
            except:
                data = value
            try:
                state, comment = validarEstructura([1,2], actual.type)
                if not state:
                        print(comment)
            except:
                raise DefaultError("La estructura no ha sido creada correctamente")
            if state:
                respuesta = findAdjacentNodeLista(actual.estructura, actual.type, data)
        except Exception as e:
            raise DefaultError(e)

    actual.estructura = respuesta[0]

    info = respuesta[2]
    image_base64 = base64.b64encode(respuesta[1]).decode('utf-8')
    # Crear un objeto JSON que contenga tanto la imagen SVG como la información adicional
    response_data = {
        'svg_image': image_base64,
        'info': info
    }

    return jsonify(response_data),200


@request_blueprint.route('/listas/EncontrarTodos', methods= ['GET'])
def encontrarTodos():
    
    try:
        try:
            state, comment = validarEstructura([1,2], actual.type)
            if not state:
                print(comment)
        except:
            raise DefaultError("La estructura no ha sido creada correctamente")
        if state:
            respuesta = darTodosLosNodos(actual.estructura, actual.type)
    except Exception as e:
        raise DefaultError(e)

    actual.estructura = respuesta[0]

    info = respuesta[2]
    image_base64 = base64.b64encode(respuesta[1]).decode('utf-8')
    # Crear un objeto JSON que contenga tanto la imagen SVG como la información adicional
    response_data = {
        'svg_image': image_base64,
        'info': info
    }
    return jsonify(response_data),200