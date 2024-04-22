from models.model import Actual
from flask import jsonify, request, Blueprint, Response, make_response
import importlib
import json
import config as cf
from listasEnlazadas.enlace import crearListaEnlazada,anadirNodoLista,anadirNodoListaFirst,eliminarNodoLista,encontrarNodoLista,findAdjacentNodeLista,darTodosLosNodos
from Arboles.enlace import crearBST, crearRBT, anadirNodoBST, anadirNodoRBT, eliminarNodoBST, eliminarNodoRBT, findAdjacentNodoBST, findAdjacentNodoRBT, listarNodosBST, listarNodosRBT, encontrarNodoBST, encontrarNodoRBT
from soporte.soporte import validarEstructura
from Grafos.enlace import crearGraph, adyacentesNodoGraph,anadirArcoGraph,anadirNodoGraph, eliminarNodoGraph, existeNodoGraph, encontrarNodosGraph, recorridosGraph
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
    if 'file' not in request.files:
        raise DefaultError('No file part')
    file = request.files['file']
    if file.filename == '':
        raise DefaultError('No selected file')
    
    file_content = file.read()
    spec = importlib.util.spec_from_loader('',loader=None, origin=file.filename)
    foo = importlib.util.module_from_spec(spec)
    exec(file_content, foo.__dict__)

    actual.file = foo
    return '',200



@request_blueprint.route('/config/porDefecto', methods= ['POST'])
def cargarArchvioPorDefecto():
    json = request.get_json()
    actual.type = json.get('type')
    archivo = ''
    if actual.type ==1 or actual.type == 2:
        archivo = "\\referencias\lista_disc.py"
    elif  actual.type == 3:
        archivo = "\\referencias\\arbol_BST_disc.py"
    elif  actual.type == 8:
        archivo = "\\referencias\\arbol_RBT_disc.py"
    else:
        archivo = "\\referencias\grafo_disc.py"

    spec = importlib.util.spec_from_file_location("",  cf.data_dir + archivo)
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
@request_blueprint.route('/listas/crearVacio', methods= ['GET'])
def crearListaVacia():
    actual.estructura = None
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
    actual.estructura = None
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
    actual.estructura = None
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



@request_blueprint.route('/listas/AñadirNodo', methods= ['POST'])
def añadirNodoLista():
    json = request.get_json()
    value = json.get('value').strip()
    raise DefaultError("Este es el error")
    if len(value) > 0:
        try:
            try:
                data = int(value)
            except:
                data = value
            try:
                if actual.estructura == None:
                    raise DefaultError("La estructura no ha sido creada correctamente")
                state, comment = validarEstructura([1,2], actual.type)
                if not state:
                        print(comment)
            except:
                raise DefaultError("La estructura no ha sido creada correctamente")
            if state:
                try:
                    respuesta = anadirNodoLista(actual.estructura, actual.type, data)
                except Exception as e:
                    raise DefaultError(e)
                
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

@request_blueprint.route('/listas/AñadirPrincipio', methods= ['POST'])
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
                if actual.estructura == None:
                    raise DefaultError("La estructura no ha sido creada correctamente")
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


@request_blueprint.route('/listas/EliminarNodo', methods= ['POST'])
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
                if actual.estructura == None:
                    raise DefaultError("La estructura no ha sido creada correctamente")
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

@request_blueprint.route('/listas/EncontarNodo', methods= ['POST'])
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
                if actual.estructura == None:
                    raise DefaultError("La estructura no ha sido creada correctamente")
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

@request_blueprint.route('/listas/EncontarAdyacentes', methods= ['POST'])
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
                if actual.estructura == None:
                    raise DefaultError("La estructura no ha sido creada correctamente")
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
            if actual.estructura == None:
                raise DefaultError("La estructura no ha sido creada correctamente")
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


@request_blueprint.route('/arboles/crearRandom', methods= ['GET'])
def crearArbolRandom():
    actual.estructura = None
    init = "Random"
    try:
        if actual.type == 3:
            respuesta = crearBST(init, actual.file)
        else:
            respuesta = crearRBT(init, actual.file)
    except Exception as e:
        raise DefaultError(e)
    actual.estructura = respuesta[1]
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

@request_blueprint.route('/arboles/crearEstatico', methods= ['GET'])
def crearArbolEstatico():
    actual.estructura = None
    try:
        name = 'creation files/bst_1.json'
        json_data = open(name)
        data = json.load(json_data)
        print(data)
    except:
        e = "\tProblema al cargar el archivo estatico " + name
        raise DefaultError(e)
    try:  
        if actual.type == 3:
            respuesta = crearBST("Estática", actual.file, data)
        else:
            respuesta = crearRBT("Estática", actual.file, data)

    except Exception as e:
        raise DefaultError(e)
    actual.estructura = respuesta[1]
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


@request_blueprint.route('/arboles/crearVacio', methods= ['GET'])
def crearArbolVacio():
    actual.estructura = None
    try:
        if actual.type == 3:
            respuesta = crearBST("Vacia", actual.file)
        else:
            respuesta = crearRBT("Vacia", actual.file)
    except Exception as e:
        raise DefaultError(e)
    actual.estructura = respuesta[1]
    info = respuesta[2]
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
    json = request.get_json()
    value = json.get('value').strip()
    if len(value) > 0:
        try:
            try:
                data = int(value)
            except:
                data = value
            try:
                if actual.estructura == None:
                    raise DefaultError("La estructura no ha sido creada correctamente")
                state, comment = validarEstructura([3,8], actual.type)
                if not state:
                    print(comment)
            except:
                raise DefaultError("La estructura no ha sido creada correctamente")
            if state:
                if actual.type == 3:
                    respuesta = anadirNodoBST(actual.estructura, data)
                else:
                    respuesta = anadirNodoRBT(actual.estructura, data)
        except Exception as e:
            raise DefaultError(e)

    actual.estructura = respuesta[1]
    info = respuesta[2]
    image_base64 = base64.b64encode(respuesta[0]).decode('utf-8')
    # Crear un objeto JSON que contenga tanto la imagen SVG como la información adicional
    response_data = {
        'svg_image': image_base64,
        'info': info
    }
    return jsonify(response_data),200


@request_blueprint.route('/arboles/eliminarNodo', methods= ['POST'])
def EliminarNodoArbol():
    json = request.get_json()
    value = json.get('value').strip()
    if len(value) > 0:
        try:
            try:
                data = int(value)
            except:
                data = value
            try:
                if actual.estructura == None:
                    raise DefaultError("La estructura no ha sido creada correctamente")
                state, comment = validarEstructura([3,8], actual.type)
                if not state:
                    print(comment)
            except:
                raise DefaultError("La estructura no ha sido creada correctamente")
            if state:
                if actual.type == 3:
                    respuesta = eliminarNodoBST(actual.estructura, data)
                else:
                    respuesta = eliminarNodoRBT(actual.estructura, data)
        except Exception as e:
            raise DefaultError(e)

    actual.estructura = respuesta[1]
    info = respuesta[2]
    image_base64 = base64.b64encode(respuesta[0]).decode('utf-8')
    # Crear un objeto JSON que contenga tanto la imagen SVG como la información adicional
    response_data = {
        'svg_image': image_base64,
        'info': info
    }
    return jsonify(response_data),200

@request_blueprint.route('/arboles/encontrarNodo', methods= ['POST'])
def EncontrarNodoArbol():
    json = request.get_json()
    value = json.get('value').strip()
    if len(value) > 0:
        try:
            try:
                data = int(value)
            except:
                data = value
            try:
                if actual.estructura == None:
                    raise DefaultError("La estructura no ha sido creada correctamente")
                state, comment = validarEstructura([3,8], actual.type)
                if not state:
                    print(comment)
            except:
                raise DefaultError("La estructura no ha sido creada correctamente")
            if state:
                if actual.type == 3:
                    respuesta = encontrarNodoBST(actual.estructura, data)
                else:
                    respuesta = encontrarNodoRBT(actual.estructura, data)
        except Exception as e:
            raise DefaultError(e)

    actual.estructura = respuesta[1]
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
    json = request.get_json()
    value = json.get('value').strip()
    if len(value) > 0:
        try:
            try:
                data = int(value)
            except:
                data = value
            try:
                if actual.estructura == None:
                    raise DefaultError("La estructura no ha sido creada correctamente")
                state, comment = validarEstructura([3,8], actual.type)
                if not state:
                    print(comment)
            except:
                raise DefaultError("La estructura no ha sido creada correctamente")
            if state:
                if actual.type == 3:
                    respuesta = findAdjacentNodoBST(actual.estructura, data)
                else:
                    respuesta = findAdjacentNodoRBT(actual.estructura, data)
        except Exception as e:
            raise DefaultError(e)

    actual.estructura = respuesta[1]
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
    json = request.get_json()
    order= json.get('order')
    try:
        if actual.estructura == None:
            raise DefaultError("La estructura no ha sido creada correctamente")
        state, comment = validarEstructura([3,8], actual.type)
        if not state:
            print(comment)
        if state:
            if actual.type == 3:
                respuesta = listarNodosBST(actual.estructura, order)
            else:
                respuesta = listarNodosRBT(actual.estructura, order)
    except Exception as e:
        raise DefaultError(e)

    actual.estructura = respuesta[1]
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
    actual.estructura = None
    init = "Random"
    try:
        respuesta = crearGraph(init, actual.type ,actual.file, labels=True)
    except Exception as e:
        raise DefaultError(e)
    actual.estructura = respuesta[1]
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
    actual.estructura = None
    try:
        name = 'creation files/graph_1.json'
        json_data = open(name)
        data = json.load(json_data)
        print(data)
    except:
        e = "\tProblema al cargar el archivo estatico " + name
        raise DefaultError(e)
    try:  
        respuesta = crearGraph("Estática", actual.type ,actual.file,data,labels=True)
    except Exception as e:
        raise DefaultError(e)
    actual.estructura = respuesta[1]
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


@request_blueprint.route('/grafos/crearVacio', methods= ['GET'])
def crearGrafoVacio():
    actual.estructura = None
    try:
        respuesta = crearGraph("Vacia", actual.type ,actual.file,labels=True)
    except Exception as e:
        raise DefaultError(e)
    actual.estructura = respuesta[1]
    info = respuesta[2]
    image_base64 = base64.b64encode(respuesta[0]).decode('utf-8')
    # Crear un objeto JSON que contenga tanto la imagen SVG como la información adicional
    response_data = {
        'svg_image': image_base64,
        'info': info
    }
    return jsonify(response_data),200



@request_blueprint.route('/grafos/añadirNodo', methods= ['POST'])
def AñadirNodoGrafo():
    json = request.get_json()
    value = json.get('value').strip()
    if len(value) > 0:
        try:
            try:
                if actual.estructura == None:
                    raise DefaultError("La estructura no ha sido creada correctamente")
                state, comment = validarEstructura([4,7], actual.type)
                if not state:
                    print(comment)
            except:
                raise DefaultError("La estructura no ha sido creada correctamente")
            if state:
                respuesta = anadirNodoGraph(actual.estructura, actual.type, True, value)    
        except Exception as e:
            raise DefaultError(e)

    actual.estructura = respuesta[1]
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
    json = request.get_json()
    value = json.get('value').strip()
    if len(value) > 0:
        try:
            try:
                if actual.estructura == None:
                    raise DefaultError("La estructura no ha sido creada correctamente")
                state, comment = validarEstructura([4,7], actual.type)
                if not state:
                    print(comment)
            except:
                raise DefaultError("La estructura no ha sido creada correctamente")
            if state:
                respuesta = eliminarNodoGraph(actual.estructura, actual.type, True, value)    
        except Exception as e:
            raise DefaultError(e)

    actual.estructura = respuesta[1]
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
    json = request.get_json()
    value = json.get('value').strip()
    if len(value) > 0:
        try:
            try:
                if actual.estructura == None:
                    raise DefaultError("La estructura no ha sido creada correctamente")
                state, comment = validarEstructura([4,7], actual.type)
                if not state:
                    print(comment)
            except:
                raise DefaultError("La estructura no ha sido creada correctamente")
            if state:
                respuesta = existeNodoGraph(actual.estructura, actual.type, True, value)    
        except Exception as e:
            raise DefaultError(e)

    actual.estructura = respuesta[1]
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
    json = request.get_json()
    origen = json.get('origen').strip()
    destino = json.get('destino').strip()
    peso = json.get('peso')
    if len(origen) > 0 and len(destino)>0:
        try:
            try:
                if actual.estructura == None:
                    raise DefaultError("La estructura no ha sido creada correctamente")
                state, comment = validarEstructura([4,7], actual.type)
                if not state:
                    print(comment)
            except:
                raise DefaultError("La estructura no ha sido creada correctamente")
            if state:
                respuesta = anadirArcoGraph(actual.estructura, actual.type, True, origen, destino, peso)    
        except Exception as e:
            raise DefaultError(e)

    actual.estructura = respuesta[1]
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
    json = request.get_json()
    value = json.get('value').strip()
    if len(value) > 0:
        try:
            try:
                if actual.estructura == None:
                    raise DefaultError("La estructura no ha sido creada correctamente")
                state, comment = validarEstructura([4,7], actual.type)
                if not state:
                    print(comment)
            except:
                raise DefaultError("La estructura no ha sido creada correctamente")
            if state:
                respuesta = adyacentesNodoGraph(actual.estructura, actual.type, True, value)    
        except Exception as e:
            raise DefaultError(e)

    actual.estructura = respuesta[1]
    info = respuesta[2]
    image_base64 = base64.b64encode(respuesta[0]).decode('utf-8')
    # Crear un objeto JSON que contenga tanto la imagen SVG como la información adicional
    response_data = {
        'svg_image': image_base64,
        'info': info
    }
    return jsonify(response_data),200

@request_blueprint.route('/grafos/todosNodos', methods= ['GET'])
def NodosGrafo():
    try:
        try:
            if actual.estructura == None:
                raise DefaultError("La estructura no ha sido creada correctamente")
            state, comment = validarEstructura([4,7], actual.type)
            if not state:
                print(comment)
        except:
            raise DefaultError("La estructura no ha sido creada correctamente")
        if state:
            respuesta = encontrarNodosGraph(actual.estructura, actual.type, True)    
    except Exception as e:
        raise DefaultError(e)

    actual.estructura = respuesta[1]
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
    json = request.get_json()
    nodo = json.get('vertice').strip()
    recorrido = json.get('recorrido')
    if len(nodo) > 0:
        try:
            try:
                if actual.estructura == None:
                    raise DefaultError("La estructura no ha sido creada correctamente")
                state, comment = validarEstructura([4,7], actual.type)
                if not state:
                    print(comment)
            except:
                raise DefaultError("La estructura no ha sido creada correctamente")
            if state:
                if '*' in recorrido and len(nodo) > 0:
                    recorrido = recorrido.replace('*', '')
                    respuesta = recorridosGraph(actual.estructura, actual.type, True, recorrido, nodo)
                else:
                    respuesta = recorridosGraph(actual.estructura, actual.type, True, recorrido, nodo)  
        except Exception as e:
            raise DefaultError(e)
    actual.estructura = respuesta[1]
    info = respuesta[2]
    image_base64 = base64.b64encode(respuesta[0]).decode('utf-8')
    # Crear un objeto JSON que contenga tanto la imagen SVG como la información adicional
    response_data = {
        'svg_image': image_base64,
        'info': info
    }
    return jsonify(response_data),200
