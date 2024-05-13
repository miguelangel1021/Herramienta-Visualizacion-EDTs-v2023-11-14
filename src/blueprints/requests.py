from datetime import datetime, timedelta
from models.model import Actual
from flask import jsonify, request, Blueprint, Response, make_response
import importlib
import json
import config as cf
from listasEnlazadas.enlace import crearListaEnlazada,anadirNodoLista,anadirNodoListaFirst,eliminarNodoLista,encontrarNodoLista,findAdjacentNodeLista,darTodosLosNodos
from Arboles.enlace import crearBST, crearRBT, anadirNodoBST, anadirNodoRBT, eliminarNodoBST, eliminarNodoRBT, findAdjacentNodoBST, findAdjacentNodoRBT, listarNodosBST, listarNodosRBT, encontrarNodoBST, encontrarNodoRBT
from soporte.soporte import validarEstructura
from Grafos.enlace import crearGraph, adyacentesNodoGraph,anadirArcoGraph,anadirNodoGraph, eliminarNodoGraph, existeNodoGraph, encontrarNodosGraph, recorridosGraph
from errors.errors import DefaultError, IdNotInRequest, ExpiredSessionId
from io import BytesIO
import base64
import uuid
from apscheduler.schedulers.background import BackgroundScheduler
import traceback




request_blueprint = Blueprint('config', __name__)

user_sessions={}

@request_blueprint.route('/config/create_session', methods=['GET'])
def create_session():
    # Generar un Session-Id único
    session_id = str(uuid.uuid4())

    # Crear una nueva estructura de datos de sesión para este Session-Id
    user_sessions[session_id] = Actual(None, None, None, None)

    user_sessions[session_id].lastAccesTime = datetime.now()
    # Devolver el Session-Id
    response = make_response(jsonify({'session_id': session_id}), 200)

    # Establecer la cookie en la respuesta
    response.set_cookie('session_id', session_id)

    return response

@request_blueprint.route('/config/type', methods= ['POST'])
def asignarEstructura():

    session_id = request.headers.get('Session-Id')
    if session_id is None:
        raise IdNotInRequest
    
    if session_id not in user_sessions:
        user_sessions[session_id] = Actual(None, None, None, None)
    
    user_sessions[session_id].lastAccesTime = datetime.now()
    
    json = request.get_json()
    user_sessions[session_id].type = json.get('type')
    return '',200

@request_blueprint.route('/config/cargar', methods= ['POST'])
def cargarArchvio():

    session_id = request.headers.get('Session-Id')
    if session_id is None:
        raise IdNotInRequest
    
    if session_id not in user_sessions:
        raise ExpiredSessionId

    if 'file' not in request.files:
        raise DefaultError('No file part')
    file = request.files['file']
    if file.filename == '':
        raise DefaultError('No selected file')
    try:
        file_content = file.read()
        spec = importlib.util.spec_from_loader('',loader=None, origin=file.filename)
        foo = importlib.util.module_from_spec(spec)
        exec(file_content, foo.__dict__)
    except Exception as e:
        raise DefaultError(e)
    
    user_sessions[session_id].lastAccesTime = datetime.now()
    user_sessions[session_id].file = foo

    return '',200



@request_blueprint.route('/config/porDefecto', methods= ['POST'])
def cargarArchvioPorDefecto():

    session_id = request.headers.get('Session-Id')
    if session_id is None:
        raise IdNotInRequest
    
    if session_id not in user_sessions:
        raise ExpiredSessionId
    
    user_sessions[session_id].lastAccesTime = datetime.now()
    
    json = request.get_json()
    user_sessions[session_id].type = json.get('type')
    archivo = ''
    if user_sessions[session_id].type ==1 or user_sessions[session_id].type == 2:
        archivo = "\\referencias\lista_disc.py"
    elif  user_sessions[session_id].type == 3:
        archivo = "\\referencias\\arbol_BST_disc.py"
    elif  user_sessions[session_id].type == 8:
        archivo = "\\referencias\\arbol_RBT_disc.py"
    else:
        archivo = "\\referencias\grafo_disc.py"


    spec = importlib.util.spec_from_file_location("",  cf.data_dir + archivo)
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)

    user_sessions[session_id].file = foo

    return '',200

@request_blueprint.route('/config/restart', methods= ['POST'])
def restart():

    session_id = request.headers.get('Session-Id')
    if session_id is None:
        raise IdNotInRequest
    
    if session_id not in user_sessions:
        raise ExpiredSessionId
    
    

    user_sessions[session_id]= Actual(None,None,None,None)
    user_sessions[session_id].lastAccesTime = datetime.now()

    return '',200



#Listas Enlazadas
@request_blueprint.route('/listas/crearVacio', methods= ['GET'])
def crearListaVacia():

    session_id = request.headers.get('Session-Id')
    if session_id is None:
        raise IdNotInRequest
    
    if session_id not in user_sessions:
        raise ExpiredSessionId
    
    user_sessions[session_id].lastAccesTime = datetime.now()
    user_sessions[session_id].estructura = None
    
    try:
        respuesta = crearListaEnlazada(user_sessions[session_id].type, user_sessions[session_id].file, "Vacia")
    except Exception as e:
        raise DefaultError(str(e))
    user_sessions[session_id].estructura = respuesta[0]
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

    session_id = request.headers.get('Session-Id')
    if session_id is None:
        raise IdNotInRequest
    
    if session_id not in user_sessions:
        raise ExpiredSessionId
    
    user_sessions[session_id].lastAccesTime = datetime.now()
    user_sessions[session_id].estructura = None
    try:
        name = 'creation files/lista_enlazada_1.json'
        json_data = open(name)
        data = json.load(json_data)
        print(data)
    except:
        e = "\tProblema al cargar el archivo estatico " + name
        raise DefaultError(str(e))
    try:               
        respuesta = crearListaEnlazada(user_sessions[session_id].type, user_sessions[session_id].file, "Estática", data)
    except Exception as e:
        raise DefaultError(str(e))
    user_sessions[session_id].estructura = respuesta[0]
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


@request_blueprint.route('/listas/crearRandom', methods=['GET'])
def crearListaRandom():

    session_id = request.headers.get('Session-Id')
    if session_id is None:
        raise IdNotInRequest
    
    if session_id not in user_sessions:
        raise ExpiredSessionId
    
    user_sessions[session_id].lastAccesTime = datetime.now()
    user_sessions[session_id].estructura = None

    init = "Random"
    try:
        respuesta = crearListaEnlazada(user_sessions[session_id].type, user_sessions[session_id].file, init)
    except Exception as e:
        raise DefaultError(str(e))
    
    user_sessions[session_id].estructura = respuesta[0]
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



@request_blueprint.route('/listas/AñadirNodo', methods= ['POST'])
def añadirNodoLista():

    session_id = request.headers.get('Session-Id')
    if session_id is None:
        raise IdNotInRequest
    
    if session_id not in user_sessions:
        raise ExpiredSessionId
    
    user_sessions[session_id].lastAccesTime = datetime.now()
    json = request.get_json()
    value = json.get('value').strip()
    if len(value) > 0:
        try:
            try:
                data = int(value)
            except:
                data = value
            try:
                if user_sessions[session_id].estructura == None:
                    raise DefaultError("La estructura no ha sido creada correctamente")
                state, comment = validarEstructura([1,2], user_sessions[session_id].type)
                if not state:
                        print(comment)
            except:
                raise DefaultError("La estructura no ha sido creada correctamente")
            if state:
                respuesta = anadirNodoLista(user_sessions[session_id].estructura, user_sessions[session_id].type, data)
        except Exception as e:
            raise DefaultError(str(e))
    else:
        raise DefaultError("Por favor ingrese el valor que será añadido a la lista.")
    user_sessions[session_id].estructura = respuesta[0]

    info = respuesta[2]
    image_base64 = base64.b64encode(respuesta[1]).decode('utf-8')
    # Crear un objeto JSON que contenga tanto la imagen SVG como la información adicional
    response_data = {
        'svg_image': image_base64,
        'info': info
    }
    return jsonify(response_data),200

@request_blueprint.route('/listas/AñadirPrincipio', methods= ['POST'])
def añadirNodoPrincipio():

    session_id = request.headers.get('Session-Id')
    if session_id is None:
        raise IdNotInRequest
    
    if session_id not in user_sessions:
        raise ExpiredSessionId
    
    user_sessions[session_id].lastAccesTime = datetime.now()
    json = request.get_json()
    value = json.get('value').strip()
    if len(value) > 0:
        try:
            try:
                data = int(value)
            except:
                data = value
            try:
                if user_sessions[session_id].estructura == None:
                    raise DefaultError("La estructura no ha sido creada correctamente")
                state, comment = validarEstructura([1,2], user_sessions[session_id].type)
                if not state:
                        print(comment)
            except:
                raise DefaultError("La estructura no ha sido creada correctamente")
            if state:
                respuesta = anadirNodoListaFirst(user_sessions[session_id].estructura, user_sessions[session_id].type, data)
        except Exception as e:
            raise DefaultError(str(e))
    else:
        raise DefaultError("Por favor ingrese el valor que será añadido al principio de la lista.")
    user_sessions[session_id].estructura = respuesta[0]
    info = respuesta[2]
    image_base64 = base64.b64encode(respuesta[1]).decode('utf-8')
    # Crear un objeto JSON que contenga tanto la imagen SVG como la información adicional
    response_data = {
        'svg_image': image_base64,
        'info': info
    }
    return jsonify(response_data),200


@request_blueprint.route('/listas/EliminarNodo', methods= ['POST'])
def eliminarNodo():

    session_id = request.headers.get('Session-Id')
    if session_id is None:
        raise IdNotInRequest
    
    if session_id not in user_sessions:
        raise ExpiredSessionId
    
    user_sessions[session_id].lastAccesTime = datetime.now()

    json = request.get_json()
    value = json.get('value').strip()
    if len(value) > 0:
        try:
            try:
                data = int(value)
            except:
                data = value
            try:
                if user_sessions[session_id].estructura == None:
                    raise DefaultError("La estructura no ha sido creada correctamente")
                state, comment = validarEstructura([1,2], user_sessions[session_id].type)
                if not state:
                        print(comment)
            except:
                raise DefaultError("La estructura no ha sido creada correctamente")
            if state:
                respuesta = eliminarNodoLista(user_sessions[session_id].estructura, user_sessions[session_id].type, data)
        except Exception as e:
            raise DefaultError(str(e))
    else:
        raise DefaultError("Por favor ingrese el valor que será eliminado de la lista.")
    user_sessions[session_id].estructura = respuesta[0]
    # Establecer los encabezados con la información adicional
    info = respuesta[2]
    image_base64 = base64.b64encode(respuesta[1]).decode('utf-8')
    # Crear un objeto JSON que contenga tanto la imagen SVG como la información adicional
    response_data = {
        'svg_image': image_base64,
        'info': info
    }
    return jsonify(response_data),200

@request_blueprint.route('/listas/EncontarNodo', methods= ['POST'])
def encontrarNodo():

    session_id = request.headers.get('Session-Id')
    if session_id is None:
        raise IdNotInRequest
    
    if session_id not in user_sessions:
        raise ExpiredSessionId
    
    user_sessions[session_id].lastAccesTime = datetime.now()
    json = request.get_json()
    value = json.get('value').strip()
    if len(value) > 0:
        try:
            try:
                data = int(value)
            except:
                data = value
            try:
                if user_sessions[session_id].estructura == None:
                    raise DefaultError("La estructura no ha sido creada correctamente")
                state, comment = validarEstructura([1,2], user_sessions[session_id].type)
                if not state:
                        print(comment)
            except:
                raise DefaultError("La estructura no ha sido creada correctamente")
            if state:
                respuesta = encontrarNodoLista(user_sessions[session_id].estructura, user_sessions[session_id].type, data)
        except Exception as e:
            raise DefaultError(str(e))
    else:
        raise DefaultError("Por favor ingrese el valor a buscar.")
    user_sessions[session_id].estructura = respuesta[0]
    
    info = respuesta[2]
    image_base64 = base64.b64encode(respuesta[1]).decode('utf-8')
    # Crear un objeto JSON que contenga tanto la imagen SVG como la información adicional
    response_data = {
        'svg_image': image_base64,
        'info': info
    }
    return jsonify(response_data),200

@request_blueprint.route('/listas/EncontarAdyacentes', methods= ['POST'])
def encontrarAdyacentes():

    session_id = request.headers.get('Session-Id')
    if session_id is None:
        raise IdNotInRequest
    
    if session_id not in user_sessions:
        raise ExpiredSessionId
    
    user_sessions[session_id].lastAccesTime = datetime.now()
    json = request.get_json()
    value = json.get('value').strip()
    if len(value) > 0:
        try:
            try:
                data = int(value)
            except:
                data = value
            try:
                if user_sessions[session_id].estructura == None:
                    raise DefaultError("La estructura no ha sido creada correctamente")
                state, comment = validarEstructura([1,2], user_sessions[session_id].type)
                if not state:
                        print(comment)
            except:
                raise DefaultError("La estructura no ha sido creada correctamente")
            if state:
                respuesta = findAdjacentNodeLista(user_sessions[session_id].estructura, user_sessions[session_id].type, data)
        except Exception as e:
            raise DefaultError(str(e))
    else:
        raise DefaultError("Por favor ingrese el valor a busacr.")
    user_sessions[session_id].estructura = respuesta[0]

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
    
    session_id = request.headers.get('Session-Id')
    if session_id is None:
        raise IdNotInRequest
    
    if session_id not in user_sessions:
        raise ExpiredSessionId
    
    user_sessions[session_id].lastAccesTime = datetime.now()
    try:
        try:
            if user_sessions[session_id].estructura == None:
                raise DefaultError("La estructura no ha sido creada correctamente")
            state, comment = validarEstructura([1,2], user_sessions[session_id].type)
            if not state:
                print(comment)
        except:
            raise DefaultError("La estructura no ha sido creada correctamente")
        if state:
            respuesta = darTodosLosNodos(user_sessions[session_id].estructura, user_sessions[session_id].type)
    except Exception as e:
        raise DefaultError(str(e))

    user_sessions[session_id].estructura = respuesta[0]

    info = respuesta[2]
    image_base64 = base64.b64encode(respuesta[1]).decode('utf-8')
    # Crear un objeto JSON que contenga tanto la imagen SVG como la información adicional
    response_data = {
        'svg_image': image_base64,
        'info': info
    }
    return jsonify(response_data),200


@request_blueprint.route('/arboles/crearRandom', methods= ['GET'])
def crearArbolRandom():

    session_id = request.headers.get('Session-Id')
    if session_id is None:
        raise IdNotInRequest
    
    if session_id not in user_sessions:
        raise ExpiredSessionId
    
    user_sessions[session_id].lastAccesTime = datetime.now()
    user_sessions[session_id].estructura = None
    init = "Random"
    try:
        if user_sessions[session_id].type == 3:
            respuesta = crearBST(init, user_sessions[session_id].file)
        else:
            respuesta = crearRBT(init, user_sessions[session_id].file)
    except Exception as e:
        raise DefaultError(str(e))
    user_sessions[session_id].estructura = respuesta[1]
    # Obtener la información adicional
    info = respuesta[2]
    order = respuesta[3]
    user_sessions[session_id].rbt_order = order
    # Convertir la imagen SVG a una cadena
    image_base64 = base64.b64encode(respuesta[0]).decode('utf-8')
    # Crear un objeto JSON que contenga tanto la imagen SVG como la información adicional
    response_data = {
        'svg_image': image_base64,
        'info': info
    }
    # Devolver el objeto JSON junto con la imagen SVG
    return jsonify(response_data), 200

@request_blueprint.route('/arboles/crearEstatico', methods= ['GET'])
def crearArbolEstatico():

    session_id = request.headers.get('Session-Id')
    if session_id is None:
        raise IdNotInRequest
    
    if session_id not in user_sessions:
        raise ExpiredSessionId
    
    user_sessions[session_id].lastAccesTime = datetime.now()
    user_sessions[session_id].estructura = None

    try:
        name = 'creation files/bst_1.json'
        json_data = open(name)
        data = json.load(json_data)
        print(data)
    except:
        e = "\tProblema al cargar el archivo estatico " + name
        raise DefaultError(str(e))
    
    try:  
        if user_sessions[session_id].type == 3:
            respuesta = crearBST("Estática", user_sessions[session_id].file, data)
        else:
            respuesta = crearRBT("Estática", user_sessions[session_id].file, data)

    except Exception as e:
        print(e)
        raise DefaultError(str(e))
    user_sessions[session_id].estructura = respuesta[1]
    info = respuesta[2]
    order = respuesta[3]
    user_sessions[session_id].rbt_order = order
    image_base64 = base64.b64encode(respuesta[0]).decode('utf-8')
    # Crear un objeto JSON que contenga tanto la imagen SVG como la información adicional
    response_data = {
        'svg_image': image_base64,
        'info': info
    }

    #Prueba para verificar si se crea correctamente la imagen
    """nombre_archivo = 'imagen.svg'  # Puedes ajustar el nombre y la extensión del archivo según sea necesario

    # Escribir los bytes de la imagen en el archivo
    with open(nombre_archivo, 'wb') as f:
        f.write(respuesta[0])"""

    return jsonify(response_data),200


@request_blueprint.route('/arboles/crearVacio', methods= ['GET'])
def crearArbolVacio():
    session_id = request.headers.get('Session-Id')
    if session_id is None:
        raise IdNotInRequest
    
    if session_id not in user_sessions:
        raise ExpiredSessionId
    
    user_sessions[session_id].lastAccesTime = datetime.now()
    user_sessions[session_id].estructura = None

    try:
        if user_sessions[session_id].type == 3:
            respuesta = crearBST("Vacia", user_sessions[session_id].file)
        else:
            respuesta = crearRBT("Vacia", user_sessions[session_id].file)
    
    except Exception as e:
        raise DefaultError(str(e))
    user_sessions[session_id].estructura = respuesta[1]
    info = respuesta[2]
    order = respuesta[3]
    user_sessions[session_id].rbt_order = order
    image_base64 = base64.b64encode(respuesta[0]).decode('utf-8')
    # Crear un objeto JSON que contenga tanto la imagen SVG como la información adicional
    response_data = {
        'svg_image': image_base64,
        'info': info
    }
    return jsonify(response_data),200

@request_blueprint.route('/arboles/crearArchivo', methods= ['GET'])
def crearArbolArchivo():
    pass


@request_blueprint.route('/arboles/añadirNodo', methods= ['POST'])
def AñadirNodoArbol():

    session_id = request.headers.get('Session-Id')
    if session_id is None:
        raise IdNotInRequest
    
    if session_id not in user_sessions:
        raise ExpiredSessionId
    
    user_sessions[session_id].lastAccesTime = datetime.now()
    json = request.get_json()
    value = json.get('value').strip()
    if len(value) > 0:
        try:
            try:
                data = int(value)
            except:
                data = value
            try:
                if user_sessions[session_id].estructura == None:
                    raise DefaultError("La estructura no ha sido creada correctamente")
                state, comment = validarEstructura([3,8], user_sessions[session_id].type)
                if not state:
                    print(comment)
            except:
                raise DefaultError("La estructura no ha sido creada correctamente")
            if state:
                if user_sessions[session_id].type == 3:
                    respuesta = anadirNodoBST(user_sessions[session_id].estructura, data)
                else:
                    respuesta = anadirNodoRBT(user_sessions[session_id].estructura, data, user_sessions[session_id].rbt_order)
        except Exception as e:
            raise DefaultError(str(e))
    else:
        raise DefaultError("Por favor ingrese un valor para añadir")
    user_sessions[session_id].estructura = respuesta[1]
    info = respuesta[2]
    order = respuesta[3]
    user_sessions[session_id].rbt_order = order
    image_base64 = base64.b64encode(respuesta[0]).decode('utf-8')
    # Crear un objeto JSON que contenga tanto la imagen SVG como la información adicional
    response_data = {
        'svg_image': image_base64,
        'info': info
    }
    return jsonify(response_data),200


@request_blueprint.route('/arboles/eliminarNodo', methods= ['POST'])
def EliminarNodoArbol():

    session_id = request.headers.get('Session-Id')
    if session_id is None:
        raise IdNotInRequest
    
    if session_id not in user_sessions:
        raise ExpiredSessionId
    
    user_sessions[session_id].lastAccesTime = datetime.now()
    json = request.get_json()
    value = json.get('value').strip()
    if len(value) > 0:
        try:
            try:
                data = int(value)
            except:
                data = value
            try:
                if user_sessions[session_id].estructura == None:
                    raise DefaultError("La estructura no ha sido creada correctamente")
                state, comment = validarEstructura([3,8], user_sessions[session_id].type)
                if not state:
                    print(comment)
            except:
                raise DefaultError("La estructura no ha sido creada correctamente")
            if state:
                if user_sessions[session_id].type == 3:
                    respuesta = eliminarNodoBST(user_sessions[session_id].estructura, data)
                else:
                    respuesta = eliminarNodoRBT(user_sessions[session_id].estructura, data, user_sessions[session_id].rbt_order)
        except Exception as e:
            raise DefaultError(str(e))
    else:
        raise DefaultError("Por favor ingrese un valor para eliminar")
    user_sessions[session_id].estructura = respuesta[1]
    info = respuesta[2]
    order = respuesta[3]
    user_sessions[session_id].rbt_order = order
    image_base64 = base64.b64encode(respuesta[0]).decode('utf-8')
    # Crear un objeto JSON que contenga tanto la imagen SVG como la información adicional
    response_data = {
        'svg_image': image_base64,
        'info': info
    }
    return jsonify(response_data),200

@request_blueprint.route('/arboles/encontrarNodo', methods= ['POST'])
def EncontrarNodoArbol():

    session_id = request.headers.get('Session-Id')
    if session_id is None:
        raise IdNotInRequest
    
    if session_id not in user_sessions:
        raise ExpiredSessionId
    
    user_sessions[session_id].lastAccesTime = datetime.now()
    json = request.get_json()
    value = json.get('value').strip()
    if len(value) > 0:
        try:
            try:
                data = int(value)
            except:
                data = value
            try:
                if user_sessions[session_id].estructura == None:
                    raise DefaultError("La estructura no ha sido creada correctamente")
                state, comment = validarEstructura([3,8], user_sessions[session_id].type)
                if not state:
                    print(comment)
            except:
                raise DefaultError("La estructura no ha sido creada correctamente")
            if state:
                if user_sessions[session_id].type == 3:
                    respuesta = encontrarNodoBST(user_sessions[session_id].estructura, data)
                else:
                    respuesta = encontrarNodoRBT(user_sessions[session_id].estructura, data)
        except Exception as e:
            raise DefaultError(str(e))
    else:
        raise DefaultError("Por favor ingrese un valor para buscar en le arbol")
    user_sessions[session_id].estructura = respuesta[1]
    info = respuesta[2]
    image_base64 = base64.b64encode(respuesta[0]).decode('utf-8')
    # Crear un objeto JSON que contenga tanto la imagen SVG como la información adicional
    response_data = {
        'svg_image': image_base64,
        'info': info
    }
    return jsonify(response_data),200

@request_blueprint.route('/arboles/encontrarAdyacentes', methods= ['POST'])
def EncontrarAdyacentesArbol():

    session_id = request.headers.get('Session-Id')
    if session_id is None:
        raise IdNotInRequest
    
    if session_id not in user_sessions:
        raise ExpiredSessionId
    
    user_sessions[session_id].lastAccesTime = datetime.now()
    json = request.get_json()
    value = json.get('value').strip()
    if len(value) > 0:
        try:
            try:
                data = int(value)
            except:
                data = value
            try:
                if user_sessions[session_id].estructura == None:
                    raise DefaultError("La estructura no ha sido creada correctamente")
                state, comment = validarEstructura([3,8], user_sessions[session_id].type)
                if not state:
                    print(comment)
            except:
                raise DefaultError("La estructura no ha sido creada correctamente")
            if state:
                if user_sessions[session_id].type == 3:
                    respuesta = findAdjacentNodoBST(user_sessions[session_id].estructura, data)
                else:
                    respuesta = findAdjacentNodoRBT(user_sessions[session_id].estructura, data)
        except Exception as e:
            raise DefaultError(str(e))
    else:
        raise DefaultError("Por favor ingrese un valor")
    user_sessions[session_id].estructura = respuesta[1]
    info = respuesta[2]
    image_base64 = base64.b64encode(respuesta[0]).decode('utf-8')
    # Crear un objeto JSON que contenga tanto la imagen SVG como la información adicional
    response_data = {
        'svg_image': image_base64,
        'info': info
    }
    return jsonify(response_data),200

@request_blueprint.route('/arboles/nodos', methods= ['POST'])
def NodosArbol():

    session_id = request.headers.get('Session-Id')
    if session_id is None:
        raise IdNotInRequest
    
    if session_id not in user_sessions:
        raise ExpiredSessionId
    
    user_sessions[session_id].lastAccesTime = datetime.now()
    
    json = request.get_json()
    order= json.get('order')
    try:
        if user_sessions[session_id].estructura == None:
            raise DefaultError("La estructura no ha sido creada correctamente")
        state, comment = validarEstructura([3,8], user_sessions[session_id].type)
        if not state:
            print(comment)
        if state:
            if user_sessions[session_id].type == 3:
                respuesta = listarNodosBST(user_sessions[session_id].estructura, order)
            else:
                respuesta = listarNodosRBT(user_sessions[session_id].estructura, order)
    except Exception as e:
        traceback.print_exc()
        raise DefaultError(str(e))

    user_sessions[session_id].estructura = respuesta[1]
    info = respuesta[2]
    image_base64 = base64.b64encode(respuesta[0]).decode('utf-8')
    # Crear un objeto JSON que contenga tanto la imagen SVG como la información adicional
    response_data = {
        'svg_image': image_base64,
        'info': info
    }
    return jsonify(response_data),200


@request_blueprint.route('/grafos/crearRandom', methods= ['GET'])
def crearGrafoRandom():

    session_id = request.headers.get('Session-Id')
    if session_id is None:
        raise IdNotInRequest
    
    if session_id not in user_sessions:
        raise ExpiredSessionId
    
    user_sessions[session_id].lastAccesTime = datetime.now()
    user_sessions[session_id].estructura = None

    init = "Random"
    try:
        respuesta = crearGraph(init, user_sessions[session_id].type ,user_sessions[session_id].file, labels=True)
    except Exception as e:
        raise DefaultError(str(e))
    user_sessions[session_id].estructura = respuesta[1]
    # Obtener la información adicional
    info = respuesta[2]
    # Convertir la imagen SVG a una cadena
    image_base64 = base64.b64encode(respuesta[0]).decode('utf-8')
    # Crear un objeto JSON que contenga tanto la imagen SVG como la información adicional
    response_data = {
        'svg_image': image_base64,
        'info': info
    }
    # Devolver el objeto JSON junto con la imagen SVG
    return jsonify(response_data), 200

@request_blueprint.route('/grafos/crearVacio', methods= ['GET'])
def crearGrafoVacio():

    session_id = request.headers.get('Session-Id')
    if session_id is None:
        raise IdNotInRequest
    
    if session_id not in user_sessions:
        raise ExpiredSessionId
    
    user_sessions[session_id].lastAccesTime = datetime.now()
    user_sessions[session_id].estructura = None

    init = "Vacio"
    try:
        respuesta = crearGraph(init, user_sessions[session_id].type ,user_sessions[session_id].file, labels=True)
    except Exception as e:
        raise DefaultError(str(e))
    user_sessions[session_id].estructura = respuesta[1]
    # Obtener la información adicional
    info = respuesta[2]
    # Convertir la imagen SVG a una cadena
    image_base64 = base64.b64encode(respuesta[0]).decode('utf-8')
    # Crear un objeto JSON que contenga tanto la imagen SVG como la información adicional
    response_data = {
        'svg_image': image_base64,
        'info': info
    }
    # Devolver el objeto JSON junto con la imagen SVG
    return jsonify(response_data), 200

@request_blueprint.route('/grafos/crearEstatico', methods= ['GET'])
def crearGrafoEstatico():

    session_id = request.headers.get('Session-Id')
    if session_id is None:
        raise IdNotInRequest
    
    if session_id not in user_sessions:
        raise ExpiredSessionId
    
    user_sessions[session_id].lastAccesTime = datetime.now()
    user_sessions[session_id].estructura = None
    try:
        name = 'creation files/graph_1.json'
        json_data = open(name)
        data = json.load(json_data)
        print(data)
    except:
        e = "\tProblema al cargar el archivo estatico " + name
        raise DefaultError(str(e))
    try:  
        respuesta = crearGraph("Estática", user_sessions[session_id].type ,user_sessions[session_id].file,data,labels=True)
    except Exception as e:
        print(e)
        raise DefaultError(str(e))
    user_sessions[session_id].estructura = respuesta[1]
    info = respuesta[2]
    image_base64 = base64.b64encode(respuesta[0]).decode('utf-8')
    # Crear un objeto JSON que contenga tanto la imagen SVG como la información adicional
    response_data = {
        'svg_image': image_base64,
        'info': info
    }


    #Prueba para verificar si se crea correctamente la imagen
    """nombre_archivo = 'imagen.svg'  # Puedes ajustar el nombre y la extensión del archivo según sea necesario

    # Escribir los bytes de la imagen en el archivo
    with open(nombre_archivo, 'wb') as f:
        f.write(respuesta[0])"""

 
    return jsonify(response_data),200


@request_blueprint.route('/grafos/crearArchivo', methods= ['GET'])
def crearGrafosArchivo():
    pass

@request_blueprint.route('/grafos/añadirNodo', methods= ['POST'])
def AñadirNodoGrafo():

    session_id = request.headers.get('Session-Id')
    if session_id is None:
        raise IdNotInRequest
    
    if session_id not in user_sessions:
        raise ExpiredSessionId
    user_sessions[session_id].lastAccesTime = datetime.now()

    json = request.get_json()
    value = json.get('value').strip()
    if len(value) > 0:
        try:
            try:
                if user_sessions[session_id].estructura == None:
                    raise DefaultError("La estructura no ha sido creada correctamente")
                state, comment = validarEstructura([4,7], user_sessions[session_id].type)
                if not state:
                    print(user_sessions[session_id].type ,state, comment)
            except:
                raise DefaultError("La estructura no ha sido creada correctamente")
            if state:
                respuesta = anadirNodoGraph(user_sessions[session_id].estructura, user_sessions[session_id].type, True, value)    
        except Exception as e:
            raise DefaultError(str(e))
    else:
        raise DefaultError("Por favor ingrese un valor para añadir al grafo")
    user_sessions[session_id].estructura = respuesta[1]
    info = respuesta[2]
    image_base64 = base64.b64encode(respuesta[0]).decode('utf-8')
    # Crear un objeto JSON que contenga tanto la imagen SVG como la información adicional
    response_data = {
        'svg_image': image_base64,
        'info': info
    }
    return jsonify(response_data),200

@request_blueprint.route('/grafos/eliminarNodo', methods= ['POST'])
def EliminarNodoGrafo():

    session_id = request.headers.get('Session-Id')
    if session_id is None:
        raise IdNotInRequest
    
    if session_id not in user_sessions:
        raise ExpiredSessionId
    
    user_sessions[session_id].lastAccesTime = datetime.now()
    json = request.get_json()
    value = json.get('value').strip()
    if len(value) > 0:
        try:
            try:
                if user_sessions[session_id].estructura == None:
                    raise DefaultError("La estructura no ha sido creada correctamente")
                state, comment = validarEstructura([4,7], user_sessions[session_id].type)
                if not state:
                    print(comment)
            except:
                raise DefaultError("La estructura no ha sido creada correctamente")
            if state:
                respuesta = eliminarNodoGraph(user_sessions[session_id].estructura, user_sessions[session_id].type, True, value)    
        except Exception as e:
            raise DefaultError(str(e))
    else:
        raise DefaultError("Por favor ingrese un valor para eliminar del grafo.")
    user_sessions[session_id].estructura = respuesta[1]
    info = respuesta[2]
    image_base64 = base64.b64encode(respuesta[0]).decode('utf-8')
    # Crear un objeto JSON que contenga tanto la imagen SVG como la información adicional
    response_data = {
        'svg_image': image_base64,
        'info': info
    }
    return jsonify(response_data),200

@request_blueprint.route('/grafos/encontrarNodo', methods= ['POST'])
def EncontrarNodoGrafo():

    session_id = request.headers.get('Session-Id')
    if session_id is None:
        raise IdNotInRequest
    
    if session_id not in user_sessions:
        raise ExpiredSessionId
    
    user_sessions[session_id].lastAccesTime = datetime.now()
    json = request.get_json()
    value = json.get('value').strip()
    if len(value) > 0:
        try:
            try:
                if user_sessions[session_id].estructura == None:
                    raise DefaultError("La estructura no ha sido creada correctamente")
                state, comment = validarEstructura([4,7], user_sessions[session_id].type)
                if not state:
                    print(comment)
            except:
                raise DefaultError("La estructura no ha sido creada correctamente")
            if state:
                respuesta = existeNodoGraph(user_sessions[session_id].estructura, user_sessions[session_id].type, True, value)    
        except Exception as e:
            raise DefaultError(str(e))
    else:
        raise DefaultError("Por favor ingrese el valor a buscar")
    user_sessions[session_id].estructura = respuesta[1]
    info = respuesta[2]
    image_base64 = base64.b64encode(respuesta[0]).decode('utf-8')
    # Crear un objeto JSON que contenga tanto la imagen SVG como la información adicional
    response_data = {
        'svg_image': image_base64,
        'info': info
    }
    return jsonify(response_data),200

@request_blueprint.route('/grafos/añadirArco', methods= ['POST'])
def AñadirArco():

    session_id = request.headers.get('Session-Id')
    if session_id is None:
        raise IdNotInRequest
    
    if session_id not in user_sessions:
        raise ExpiredSessionId
    
    user_sessions[session_id].lastAccesTime = datetime.now()
    json = request.get_json()
    origen = json.get('origen').strip()
    destino = json.get('destino').strip()
    peso = json.get('peso')
    if len(origen) > 0 and len(destino)>0:
        try:
            try:
                if user_sessions[session_id].estructura == None:
                    raise DefaultError("La estructura no ha sido creada correctamente")
                state, comment = validarEstructura([4,7], user_sessions[session_id].type)
                if not state:
                    print(comment)
            except:
                raise DefaultError("La estructura no ha sido creada correctamente")
            if state:
                respuesta = anadirArcoGraph(user_sessions[session_id].estructura, user_sessions[session_id].type, True, origen, destino, peso)    
        except Exception as e:
            raise DefaultError(str(e))
    else:
        raise DefaultError("Por favor ingrese los valores para añadir el arco correctamente.")
    user_sessions[session_id].estructura = respuesta[1]
    info = respuesta[2]
    image_base64 = base64.b64encode(respuesta[0]).decode('utf-8')
    # Crear un objeto JSON que contenga tanto la imagen SVG como la información adicional
    response_data = {
        'svg_image': image_base64,
        'info': info
    }
    return jsonify(response_data),200

@request_blueprint.route('/grafos/encontrarAdyacents', methods= ['POST'])
def encontrarAdyacentesGrafo():

    session_id = request.headers.get('Session-Id')
    if session_id is None:
        raise IdNotInRequest
    
    if session_id not in user_sessions:
        raise ExpiredSessionId
    
    user_sessions[session_id].lastAccesTime = datetime.now()
    json = request.get_json()
    value = json.get('value').strip()
    if len(value) > 0:
        try:
            try:
                if user_sessions[session_id].estructura == None:
                    raise DefaultError("La estructura no ha sido creada correctamente")
                state, comment = validarEstructura([4,7], user_sessions[session_id].type)
                if not state:
                    print(comment)
            except:
                raise DefaultError("La estructura no ha sido creada correctamente")
            if state:
                respuesta = adyacentesNodoGraph(user_sessions[session_id].estructura, user_sessions[session_id].type, True, value)    
        except Exception as e:
            raise DefaultError(str(e))
    else:
        raise DefaultError("Por favor ingrese el valor a buscar")
    user_sessions[session_id].estructura = respuesta[1]
    info = respuesta[2]
    image_base64 = base64.b64encode(respuesta[0]).decode('utf-8')
    # Crear un objeto JSON que contenga tanto la imagen SVG como la información adicional
    response_data = {
        'svg_image': image_base64,
        'info': info
    }
    return jsonify(response_data),200

@request_blueprint.route('/grafos/encontrarTodos', methods= ['GET'])
def NodosGrafo():


    session_id = request.headers.get('Session-Id')
    if session_id is None:
        raise IdNotInRequest
    
    if session_id not in user_sessions:
        raise ExpiredSessionId
    
    user_sessions[session_id].lastAccesTime = datetime.now()
    try:
        try:
            if user_sessions[session_id].estructura == None:
                raise DefaultError("La estructura no ha sido creada correctamente")
            state, comment = validarEstructura([4,7], user_sessions[session_id].type)
            if not state:
                print(comment)
        except:
            raise DefaultError("La estructura no ha sido creada correctamente")
        if state:
            respuesta = encontrarNodosGraph(user_sessions[session_id].estructura, user_sessions[session_id].type, True)    
    except Exception as e:
        raise DefaultError(str(e))

    user_sessions[session_id].estructura = respuesta[1]
    info = respuesta[2]
    image_base64 = base64.b64encode(respuesta[0]).decode('utf-8')
    # Crear un objeto JSON que contenga tanto la imagen SVG como la información adicional
    response_data = {
        'svg_image': image_base64,
        'info': info
    }
    return jsonify(response_data),200


@request_blueprint.route('/grafos/recorridos', methods= ['POST'])
def recorridosGrafo():

    session_id = request.headers.get('Session-Id')
    if session_id is None:
        raise IdNotInRequest
    
    if session_id not in user_sessions:
        raise ExpiredSessionId
    
    user_sessions[session_id].lastAccesTime = datetime.now()
    json = request.get_json()
    nodo = json.get('vertice').strip()
    recorrido = json.get('recorrido')
    try:
        try:
            if user_sessions[session_id].estructura == None:
                raise DefaultError("La estructura no ha sido creada correctamente")
            state, comment = validarEstructura([4,7], user_sessions[session_id].type)
            if not state:
                print(comment)
        except:
            raise DefaultError("La estructura no ha sido creada correctamente")
        if state:
            if '*' in recorrido and len(nodo) > 0:
                recorrido = recorrido.replace('*', '')
                respuesta = recorridosGraph(user_sessions[session_id].estructura, user_sessions[session_id].type, True, recorrido, nodo)
            elif '*' in recorrido:
                raise DefaultError("Ingrese un nodo de partida para ejecutar el recorrido.")
            else:
                 respuesta = recorridosGraph(user_sessions[session_id].estructura, user_sessions[session_id].type, True, recorrido)  
    except Exception as e:
        traceback.print_exc()
        raise DefaultError(str(e))
    user_sessions[session_id].estructura = respuesta[1]
    info = respuesta[2]
    image_base64 = base64.b64encode(respuesta[0]).decode('utf-8')
    # Crear un objeto JSON que contenga tanto la imagen SVG como la información adicional
    response_data = {
        'svg_image': image_base64,
        'info': info
    }
    return jsonify(response_data),200



def clean_inactive_sessions():
    now = datetime.now()
    inactive_threshold = timedelta(minutes=10)

    sessions_to_remove = []
    for session_id, session_data in user_sessions.items():
        last_access_time = session_data.lastAccesTime
        if (now - last_access_time) > inactive_threshold:
            sessions_to_remove.append(session_id)

    for session_id in sessions_to_remove:
        del user_sessions[session_id]
        print("eliminado: "+(session_id))


scheduler = BackgroundScheduler()
scheduler.add_job(clean_inactive_sessions, 'interval', minutes=5)  # Ejecutar cada 5 minutos
scheduler.start()


@request_blueprint.route('/verificar', methods= ['GET'])
def verificar():
    sessions = []
    for session_id, session_data in user_sessions.items():
            sessions.append(session_id)
    return jsonify(sessions), 200