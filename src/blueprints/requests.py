from models.model import Actual
from flask import jsonify, request, Blueprint, Response, make_response
import importlib
import json
import config as cf
from listasEnlazadas.enlace import crearListaEnlazada,anadirNodoLista,anadirNodoListaFirst,eliminarNodoLista,encontrarNodoLista,findAdjacentNodeLista,darTodosLosNodos
from soporte.soporte import validarEstructura
from errors.errors import IncompleteEstructure



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


lista_blueprint = Blueprint('listas', __name__)


@request_blueprint.route('/listas/crearVacio', methods= ['GET'])
def crearListaVacia():
    respuesta = crearListaEnlazada(actual.type, actual.file, "Vacia")
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
    return response,200

@request_blueprint.route('/listas/crearEstatica', methods= ['GET'])
def crearListaEstatica():
    try:
        name = 'creation files/lista_enlazada_1.json'
        json_data = open(name)
        data = json.load(json_data)
        print(data)
    except:
        e = "\tProblema al cargar el archivo estatico " + name
        raise Exception (e)               
    respuesta = crearListaEnlazada(actual.type, actual.file, "Estática", data)
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
    return response,200

@request_blueprint.route('/listas/crearArchivo', methods= ['GET'])
def crearListaArchivo():
    pass

@request_blueprint.route('/listas/crearRandom', methods= ['GET'])
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
    return response,200

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
                raise IncompleteEstructure
            if state:
                respuesta = anadirNodoLista(actual.estructura, actual.type, data)
        except Exception as e:
                print('Hubo un problema al intentar añadir un elemento')
                print(e)

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
    response.headers['Recorrido esperado hacia adelante'] = info['Recorrido esperado hacia adelante'] 
    response.headers['Recorrido obtenido hacia adelante'] = info['Recorrido obtenido hacia adelante']
    if actual.type == 2:
        response.headers['Recorrido esperado hacia atras'] = info['Recorrido esperado hacia atras'] 
        response.headers['Recorrido obtenido hacia atras'] = info['Recorrido obtenido hacia atras']

    return response,200

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
                raise IncompleteEstructure
            if state:
                respuesta = anadirNodoListaFirst(actual.estructura, actual.type, data)
        except Exception as e:
                print('Hubo un problema al intentar añadir un elemento')
                print(e)

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
    response.headers['Recorrido esperado hacia adelante'] = info['Recorrido esperado hacia adelante'] 
    response.headers['Recorrido obtenido hacia adelante'] = info['Recorrido obtenido hacia adelante']
    if actual.type == 2:
        response.headers['Recorrido esperado hacia atras'] = info['Recorrido esperado hacia atras'] 
        response.headers['Recorrido obtenido hacia atras'] = info['Recorrido obtenido hacia atras']

    return response,200


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
                raise IncompleteEstructure
            if state:
                respuesta = eliminarNodoLista(actual.estructura, actual.type, data)
        except Exception as e:
                print('Hubo un problema al intentar eliminar un elemento')
                print(e)

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
    response.headers['Recorrido esperado hacia adelante'] = info['Recorrido esperado hacia adelante'] 
    response.headers['Recorrido obtenido hacia adelante'] = info['Recorrido obtenido hacia adelante']
    if actual.type == 2:
        response.headers['Recorrido esperado hacia atras'] = info['Recorrido esperado hacia atras'] 
        response.headers['Recorrido obtenido hacia atras'] = info['Recorrido obtenido hacia atras']

    return response,200

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
                raise IncompleteEstructure
            if state:
                respuesta = encontrarNodoLista(actual.estructura, actual.type, data)
        except Exception as e:
                print('Hubo un problema al intentar encontrar un elemento')
                print(e)

    actual.estructura = respuesta[0]

    response = make_response(respuesta[1])

    # Establecer el tipo de contenido
    response.headers['Content-Type'] = 'image/svg+xml'

    # Establecer los encabezados con la información adicional
    info = respuesta[2]
    response.headers['msj'] = info["msj"]
    response.headers['estado'] = info["estado"]
    response.headers['comment'] = info["comment"]

    return response,200

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
                raise IncompleteEstructure
            if state:
                respuesta = findAdjacentNodeLista(actual.estructura, actual.type, data)
        except Exception as e:
                print('Hubo un problema al intentar encontrar un elemento')
                print(e)

    actual.estructura = respuesta[0]

    response = make_response(respuesta[1])

    # Establecer el tipo de contenido
    response.headers['Content-Type'] = 'image/svg+xml'

    # Establecer los encabezados con la información adicional
    info = respuesta[2]
    response.headers['msj'] = info["msj"]
    response.headers['estado'] = info["estado"]
    response.headers['comment'] = info["comment"]
    response.headers['existe'] = info["existe"]

    return response,200


@request_blueprint.route('/listas/EncontrarTodos', methods= ['GET'])
def encontrarTodos():
    
    try:
        try:
            state, comment = validarEstructura([1,2], actual.type)
            if not state:
                print(comment)
        except:
            raise IncompleteEstructure
        if state:
            respuesta = darTodosLosNodos(actual.estructura, actual.type)
    except Exception as e:
        print('Hubo un problema al intentar encontrar todos los elementos')
        print(e)

    actual.estructura = respuesta[0]

    response = make_response(respuesta[1])

    # Establecer el tipo de contenido
    response.headers['Content-Type'] = 'image/svg+xml'

    # Establecer los encabezados con la información adicional
    info = respuesta[2]
    response.headers['msj'] = info["msj"]
    response.headers['size'] = info["size"]
    response.headers['Elementos'] = info["Elementos"]

    return response,200