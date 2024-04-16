import random
from soporte.soporte import create_n_random
from .metodosGraficos import displayList
from .metodosValidacion import validar_lista_crear,validar_enlaces_anteriores,validar_lista_adyacentes,validar_lista_anadir, validar_lista_anadir_first, validar_lista_eliminar, validar_lista_encontrar,VALIDATION_STATES






def crearListaEnlazada(tipo, file, init, data={}):
    """
    Crea una lista enlazada

    Args:
        tipo: Sencilla o Doble
        file: Estructura de datos externa
        init: Vacia o Random
        data: JSON con informacion de creacion (nodos)
    Returns:
        La lista enlazada
    Raises:
        Exception
    """
    nuevoTipoError = False
    if tipo == 1: txt = 'Sencilla - ' + init
    else: txt = 'Doble - ' + init
    
    txtNodos = ''
    try:
        estructura = file.listaEnlazada(tipo)
    except:
        e = "\tProblema al crear la lista enlazada, método listaEnlazada()"
        raise Exception(e)
    long = 0
    nodos = list()
    if init == 'Random':
        txtNodos = '\tValores: '
        long = random.randint(5,15)
        nodos = create_n_random(long)
        for i in nodos:
            txtNodos = txtNodos + str(i) + ', '
            try:
                estructura.addNode_byValue(i)
            except:
                e = '\tProblema al añadir el elemento "'+str(i)+'", método addNode_byValue()'
                raise Exception(e)
        ''' CORRECCION Borrar esta validacion
        for i in range(0,len(nodos)):
            x = estructura.findAdjacentNode(nodos[i])
            if tipo == 2 and len(x) < 2 and i != 0 and i != len(nodos)-1:
                estructura = file.listaEnlazada(tipo)
                nuevoTipoError = True
        '''

    elif init == 'Estática' or init == 'Archivo':
        try:
            txtNodos = '\tValores: '
            nodos = data["valores"]
        except:
            raise Exception("El formato del archivo ingresado no es válido")
        for i in nodos:
            txtNodos = txtNodos + str(i) + ', '
            try:
                estructura.addNode_byValue(i)
            except:
                e = '\tProblema al añadir el elemento "'+str(i)+'", método addNode_byValue()'
                raise Exception(e)
        ''' CORRECCION Borrar esta validacion
        for i in range(0,len(nodos)):
            x = estructura.findAdjacentNode(nodos[i])
            if tipo == 2 and len(x) < 2 and i != 0 and i != len(nodos)-1:
                estructura = file.listaEnlazada(tipo)
                nuevoTipoError = True
        '''
    dis = displayList(estructura, tipo) 
    
    try:
        st_nodos = estructura.getNodeValues()
    except:
        e = '\tProblema al obtener todos los Elementos, método getNodeValues()'
        raise Exception(e)
    state_val, comment = validar_lista_crear(nodos, st_nodos, tipo)
    
    if nuevoTipoError == False:
        print('Crear Lista Enlazada', txt)
        print(state_val)
        print(comment)
        print('Total elementos: ' + str(len(estructura.getNodeValues())))

        response = { 
            "msj": 'Crear Lista Enlazada ' + txt,
            "estado": state_val,
            "comment": comment,
            "size": 'Total elementos: ' + str(len(estructura.getNodeValues()))
        }

    else:
        response = {"msj":'ERROR: La estructura no tiene los dobles enlaces' }
        print('ERROR: La estructura no tiene los dobles enlaces')
    return estructura, dis ,response 

def anadirNodoLista(estructura, tipo, nodo):
    """
    Añade un nodo a lista

    Args:
        estructura: lista enlazada
        tipo: tipo de lista (1: sencilla, 2:doble)
        nodo: valor del nodo
    Returns:
        -
    Raises:
        Exception
    """
    init_test = list()                                         # CORRECCION Agregar
    end_test = list()                                         # CORRECCION Agregar
    try:
        init_test = estructura.getNodeValues()
    except:
        e = '\tProblema al obtener los nodos hacia adelante, método getNodeValues()'
        raise Exception(e)
    
    if tipo == 2:                                             # CORRECCION Agregar
        try:
            init_test_anteriores = estructura.getNodeValuesReverse()      # CORRECCION Agregar
        except:
            e = '\tProblema al obtener los nodos hacia atras, método getNodeValuesReverse()'
            raise Exception(e)
    
    try:
        estructura.addNode_byValue(nodo)              # METODO DE PRUEBA
        end_test = estructura.getNodeValues()
        if tipo == 2:                                                             # CORRECCION Agregar
            end_test_anteriores = estructura.getNodeValuesReverse()               # CORRECCION Agregar
            state_val, end_val, end_val_anteriores, comment = validar_enlaces_anteriores(init_test, end_test, end_test_anteriores, 'addNodeLast', nodo, tipo)  # CORRECCION Agregar
        if tipo == 1 or (tipo == 2 and state_val == VALIDATION_STATES[1]):        # CORRECCION Agregar
            state_val, end_val, comment = validar_lista_anadir(init_test, end_test, nodo, tipo)
#        if tipo == 2 and len(estructura.findAdjacentNode(nodo)) != 1:  # CORRECCION  Borrar
#            raise Exception('No creo su conexion hacia atras')         # CORRECCION Borrar
    except Exception as e:
#        if e != 'No creo su conexion hacia atras':                     # CORRECCION Borrar
#           e = 'exception original['+str(e)+']\n'+'\tProblema al añadir el elemento "'+str(nodo)+'", método addNode_byValue()'
#           raise Exception(e)
        e = 'Problema original ' + str(e) + '\n'                        # CORRECCION Agregar
        e += '\tProblema al añadir el elemento "'+str(nodo)+'", método addNode_byValue()'
        raise Exception(e)
    
    #out.clear_output()
    dis=displayList(estructura, tipo)
    # print('Tipo Lista: ' + str(tipo))
    print('Total elementos: ' + str(len(end_test)))
    print('Añadir elemento al Final')
    print(state_val, comment)

    response = { 
            "msj": 'Añadir elemento al Final',
            "estado": state_val,
            "comment": comment,
            "size": 'Total elementos: ' +  str(len(end_test)),
            "Recorrido esperado hacia adelante": None,
            "Recorrido obtenido hacia adelante": None,
            "Recorrido esperado hacia atras": None,
            "Recorrido obtenido hacia atras": None
        }

    if state_val != VALIDATION_STATES[1]: # Si no fue exitoso, mostrar los resultados esperados y obtenidos
        print('Recorrido esperado hacia adelante: ', end_val)
        print('Recorrido obtenido hacia adelante: ', end_test)
        response['Recorrido esperado hacia adelante'] = end_val
        response['Recorrido obtenido hacia adelante'] = end_test
        if tipo == 2:
            print('Recorrido esperado hacia atras:', end_val_anteriores)
            print('Recorrido obtenido hacia atras:  ', end_test_anteriores)
            response['Recorrido esperado hacia atras'] = end_val_anteriores
            response['Recorrido obtenido hacia atra'] = end_test_anteriores
    return estructura, dis, response

def anadirNodoListaFirst(estructura, tipo, nodo):
    """
    Añade un nodo a lista

    Args:
        estructura: lista enlazada
        tipo: tipo de lista (1: sencilla, 2:doble)
        nodo: valor del nodo
    Returns:
        -
    Raises:
        Exception
    """
    init_test = list()                                         # CORRECCION Agregar
    end_test = list()                                         # CORRECCION Agregar
    try:
        init_test = estructura.getNodeValues()
    except:
        e = '\tProblema al obtener los nodos hacia adelante, método getNodeValues()'
        raise Exception(e)
    if tipo == 2:                                             # CORRECCION Agregar
        try:
            init_test_anteriores = estructura.getNodeValuesReverse()      # CORRECCION Agregar
        except:
            e = '\tProblema al obtener los nodos hacia atras, método getNodeValuesReverse()'
            raise Exception(e)
    try:
        estructura.addNode_byValueFirst(nodo)                  # METODO DE PRUEBA
        end_test = estructura.getNodeValues()
        if tipo == 2:                                                             # CORRECCION Agregar
            end_test_anteriores = estructura.getNodeValuesReverse()               # CORRECCION Agregar
            state_val, end_val, end_val_anteriores, comment = validar_enlaces_anteriores(init_test, end_test, end_test_anteriores, 'addNodeFirst', nodo, tipo)  # CORRECCION Agregar
        if tipo == 1 or (tipo == 2 and state_val == VALIDATION_STATES[1]):              # CORRECCION Agregar
            state_val, end_val, comment = validar_lista_anadir_first(init_test, end_test, nodo, tipo) 
    except Exception as e:
        e = 'Problema original ' + str(e) + '\n'                        # CORRECCION Agregar
        e = '\tProblema al añadir el elemento "'+str(nodo)+'", método addNode_byValueFirst()'
        raise Exception(e)
    
    #out.clear_output()
    dis = displayList(estructura, tipo)
    print('Total elementos: ' + str(len(end_test)))           # CORRECCION modificar
    print('Añadir elemento al Principio')
    # print('Tipo Lista: ' + str(tipo))

    print(state_val, comment)

    response = { 
            "msj": 'Añadir elemento al Principio',
            "estado": state_val,
            "comment": comment,
            "size": 'Total elementos: ' + str(len(end_test)),
            "Recorrido esperado hacia adelante": None,
            "Recorrido obtenido hacia adelante": None,
            "Recorrido esperado hacia atras": None,
            "Recorrido obtenido hacia atras": None
        }

    if state_val != VALIDATION_STATES[1]: # Si no fue exitoso, mostrar los resultados esperados y obtenidos
        print('Recorrido esperado hacia adelante:', end_val)
        print('Recorrido obtenido hacia adelante:', end_test)
        response['Recorrido esperado hacia adelante'] = end_val
        response['Recorrido obtenido hacia adelante'] = end_test
        if tipo == 2:
            print('Recorrido esperado hacia atras:', end_val_anteriores)
            print('Recorrido obtenido hacia atras:', end_test_anteriores)
            response['Recorrido esperado hacia atras'] = end_val_anteriores
            response['Recorrido obtenido hacia atra'] = end_test_anteriores
    
    return estructura,dis,response 


def eliminarNodoLista(estructura, tipo, nodo):
    """
    Elimina un nodo de la lista

    Args:
        estructura: lista enlazada
        tipo: tipo de la lista (1:sencilla, 2:doble)
        nodo: valor del nodo
    Returns:
        -
    Raises:
        Exception
    """
    try:
        init_test = estructura.getNodeValues()
    except:
        e = '\tProblema al obtener todos los nodos, método getNodeValues()'
        raise Exception(e)
    if tipo == 2:                                             # CORRECCION Agregar
        try:
            init_test_anteriores = estructura.getNodeValuesReverse()      # CORRECCION Agregar
        except:
            e = '\tProblema al obtener los nodos hacia atras, método getNodeValuesReverse()'
            raise Exception(e)
    try:
        ans = estructura.deleteNode_byValue(nodo)             # Aplicacion METODO DE PRUEBA
        end_test = estructura.getNodeValues()
        if tipo == 2:                                                             # CORRECCION Agregar
            end_test_anteriores = estructura.getNodeValuesReverse()               # CORRECCION Agregar
            state_val, end_val, end_val_anteriores, comment = validar_enlaces_anteriores(init_test, end_test, end_test_anteriores, 'deleteNode', nodo, tipo)  # CORRECCION Agregar

        if tipo == 1 or (tipo == 2 and state_val == VALIDATION_STATES[1]):              # CORRECCION Agregar
            state_val, end_val, comment = validar_lista_eliminar(init_test, end_test, nodo, tipo, ans) 
    except Exception as e:
        e = 'Problema original ' + str(e) + '\n'                        # CORRECCION Agregar
        e = '\tProblema al eliminar el elemento "'+str(nodo)+'", método deleteNode_byValue()'
        raise Exception(e)                                              # CORRECCION Agregar
    #out.clear_output()
    dis = displayList(estructura, tipo)
    print('Total elementos: ' + str(len(end_test)))
    print('Eliminar elemento')
    
    print(state_val, comment)
    response = { 
            "msj": 'Eliminar elemento',
            "estado": state_val,
            "comment": comment,
            "size": 'Total elementos: ' + str(len(end_test)),
            "Recorrido esperado hacia adelante": None,
            "Recorrido obtenido hacia adelante": None,
            "Recorrido esperado hacia atras": None,
            "Recorrido obtenido hacia atras": None
        }

    if state_val != VALIDATION_STATES[1]: # Si no fue exitoso, mostrar los resultados esperados y obtenidos
        print('Recorrido esperado hacia adelante:', end_val)
        print('Recorrido obtenido hacia adelante:', end_test)
        response['Recorrido esperado hacia adelante'] = end_val
        response['Recorrido obtenido hacia adelante'] = end_test
        if tipo == 2:
            print('Recorrido esperado hacia atras:', end_val_anteriores)
            print('Recorrido obtenido hacia atras:', end_test_anteriores)
            response['Recorrido esperado hacia atras'] = end_val_anteriores
            response['Recorrido obtenido hacia atra'] = end_test_anteriores
    return estructura,dis,response 

def encontrarNodoLista(estructura, tipo, nodo):
    """
    Encuentra un nodo en la estrcutura

    Args:
        estructura: lista enlazada
        tipo: tipo de la lista (1:sencilla, 2:doble)
        nodo: valor del nodo
    Returns:
        -
    Raises:
        Exception
    """
    try:
        ans = estructura.isNodeValue(nodo)
        nodos = estructura.getNodeValues()
        state_val, ans_val, comment = validar_lista_encontrar(nodos, nodo, ans) 
    except:
        e = '\tProblema al buscar el elemento "' + str(nodo) + '", método isNodeValue()'
        raise Exception(e)
    #out.clear_output()
    lista = list()
    lista.append(nodo)
    if ans_val:
        dis = displayList(estructura, tipo, lista)
    else:    
        dis = displayList(estructura, tipo)

    print("Buscar elemento")
    print(state_val, comment)
    response = { 
            "msj": 'Buscar elemento',
            "estado": state_val,
            "comment": comment
        }
    return estructura,dis, response

def findAdjacentNodeLista(estructura, tipo, nodo):
    """
    Encuentra los adyacentes de un nodo a lista

    Args:
        estructura: lista enlazada
        tipo: tipo de la lista (1:sencilla, 2:doble)
        nodo: valor del nodo
    Returns:
        -
    Raises:
        Exception
    """
    try:
        init_test = estructura.getNodeValues()
    except:
        e = '\tProblema al obtener todos los nodos, método getNodeValues()'
        raise Exception(e)
    try:
        listaAdj = estructura.findAdjacentNode(nodo)
        state_val, listaAdj_val, comment, exists = validar_lista_adyacentes(init_test, listaAdj, nodo, tipo)
        # comment = 'El elemento "'+ str(nodo)+ '" tiene '+str(len(listaAdj))+' adyacente(s): ' + str(listaAdj)
        # state_val = VALIDATION_STATES[1]
        # exists = True
    except Exception as e:   # CORRECCION Modificar
        e = 'Problema original ' + str(e) + '\n'                        # CORRECCION Agregar
        e += 'TamaNo: '  + str(estructura.estructura['size']) + ' Elementos en lista: ' + str(init_test)
        e += '\tProblema al buscar los adyacentes del elemento "' + str(nodo) + '" , método findAdjacentNode()\n'
        raise Exception(e)
    
    #out.clear_output()
    dis = displayList(estructura, tipo, listaAdj)

    
    print('Encontrar Adyacentes')
    response = { 
            "msj": 'Encontrar Adyacentes',
            "estado": state_val,
            "comment": comment,
            "existe" : None
        }
    if not exists:
        print('\tEl elemento "'+str(nodo)+ '" NO existe en la lista')
        response['existe'] = 'El elemento "'+str(nodo)+ '" NO existe en la lista'
    print(state_val, comment)

    
    return estructura,dis, response

def darTodosLosNodos(estructura, tipo):
    """
    Retorna una lista con todos los nodos de la lista

    Args:
        estructura: lista enlazada
        tipo: tipo de la lista (1:sencilla, 2:doble)
    Returns:
        -
    Raises:
        Exception
    """
    try:
        nodos = estructura.getNodeValues()
    except:
        raise Exception('\tProblema al obtener todos los elemento, método getNodeValues()')
    #out.clear_output()
    dis = displayList(estructura, tipo)
    txt = ''
    for i in nodos:
        txt = txt + str(i) + ', '
    
    response = { 
            "msj": 'Encontrar Todos',
            "size": str(len(nodos)),
            "Elementos": str(txt[:-2]),
        }

    print('Encontrar Todos')
    print('\tTotal Elementos:', str(len(nodos)))
    print('\tElementos:', txt[:-2])

    return estructura, dis, response