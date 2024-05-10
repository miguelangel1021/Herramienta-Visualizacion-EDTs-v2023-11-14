import random
from DISClib.ADT import orderedmap as omap
from soporte.soporte import create_n_random
from .metodosValidacion import validar_bst_crear,validar_bst_anadir,validar_bst_adyacentes,validar_bst_darNodos,validar_bst_eliminar,validar_bst_encontrar,VALIDATION_STATES,validar_rbt_adyacentes,validar_rbt_anadir,validar_rbt_crear,validar_rbt_eliminar,validar_rbt_encontrar
from .metodosGraficos import displayBST, displayRBT



def crearBST(init, file, data={}):
    """
    Crea un arbol BST

    Args:
        init: Vacia, Random, Estática, Archivo
        file: Estructura de datos externa
        data: JSON con la información de la inicializacion de la estructura

    Returns:
        La estructura de datos creada
    Raises:
        Exception
    """
    try:
        print('Crear BST')
        estructura = file.bst()
    except Exception as e:
        print('Error')
        #e = "\tProblema al crear el arbol BST, método bst()"
        print(e)
        raise Exception(e + "\tProblema al crear el arbol BST, método bst()")
    long = 0
    nodos = list()
    if init == 'Random':
        long = random.randint(5,10)
        nodos = create_n_random(long)
    elif init == 'Estática' or init == 'Archivo':
        try:
            nodos = data["valores"]
        except:
            raise Exception("El formato del archivo ingresado no es válido")
    for key in nodos:
        try:
            estructura.addNode_byValue(key)
        except:
            e = '\tProblema al añadir el elemento "'+str(key)+'", método addNode_byValue()'
            raise Exception(e)

    try:
        end_test = estructura.getNodeValues("Preorder")
    except:
        e = '\tProblema al obtener todos los Elementos, método getNodeValues()'
        raise Exception(e)

    state_val, end_val, comment = validar_bst_crear(nodos, end_test)

    #out.clear_output()
    dis = displayBST(estructura) 
    print("Total llaves: " + str(len(end_test)))
    print('Crear BST', init)
    print(state_val, comment)
    print('BST Preorden:', end_test)
    print('Size BST', estructura.size())
    print('Height BST', estructura.height())
    print('minKey BST', estructura.minKey())

    info = {"Total llaves": str(len(end_test)),
            'Crear BST': init,
            'state': state_val,
            'comment': comment,
            'BST Preorden': end_test,
            'Size BST': estructura.size(),
            'Height BST': estructura.height(),
            'minKey BST': estructura.minKey(),
            'Se esperaba BST Preorden': None,
            'Se obtuvo BST Preorden': None}
    
    if state_val != VALIDATION_STATES[1]: # Si no fue exitoso, mostrar los resultados esperados y obtenidos
        print('Se esperaba BST Preorden:', end_val)
        print('Se obtuvo BST Preorden  :', end_test)
        info['Se esperaba BST Preorden'] = end_val
        info['Se obtuvo BST Preorden'] = end_test

    return dis, estructura, info

def anadirNodoBST(estructura, nodo):
    """
    Añade un nodo al BST

    Args:
        estructura: lista enlazada
        nodo: valor del nodo
    Returns:
        -
    Raises:
        Exception
    """
    try:
        init_test = estructura.getNodeValues("Preorder")
    except:
        e = '\tProblema al obtener todos los Elementos, método getNodeValues()'
        raise Exception(e)
    try:
        estructura.addNode_byValue(nodo)
        end_test = estructura.getNodeValues("Preorder")
        state_val, end_val, comment = validar_bst_anadir(init_test, end_test, nodo) 
    except:
        e = '\tProblema al añadir el elemento "'+str(nodo)+'", método addNode_byValue()'
        raise Exception(e)
    
    #out.clear_output()
    dis = displayBST(estructura)
    print('Añadir llave ', str(nodo))
    print(state_val, comment)
    print("BST Preorden", end_test)
    print('Size BST', estructura.size())
    print('Height BST', estructura.height())
    print('minKey BST', estructura.minKey())

    info = {"Añadir llave": nodo,
            'state': state_val,
            'comment': comment,
            'BST Preorden': end_test,
            'Size BST': estructura.size(),
            'Height BST': estructura.height(),
            'minKey BST': estructura.minKey(),
            'Se esperaba BST Preorden': None,
            'Se obtuvo BST Preorden': None}

    if state_val != VALIDATION_STATES[1]:
        print('Se esperaba BST Preorden:', end_val)
        print('Se obtuvo BST Preorden  :', end_test)
        info['Se esperaba BST Preorden'] = end_val
        info['Se obtuvo BST Preorden'] = end_test
    
    return dis, estructura, info

def eliminarNodoBST(estructura, nodo):
    """
    Elimina un nodo al BST

    Args:
        estructura: BST
        nodo: valor del nodo
    Returns:
        -
    Raises:
        Exception
    """
    
    try:
        init_test = estructura.getNodeValues("Preorder")
    except:
        e = '\tProblema al obtener las llaves en Preorden, función getNodeValues()'
        raise Exception(e)
    try:
        ans = estructura.deleteNode_byValue(nodo)  # funcion de prueba
    except:
        e = '\tProblema al eliminar el elemento "'+str(nodo)+'", función deleteNode_byValue()'
        raise Exception(e)

    end_test = estructura.getNodeValues("Preorder")
    state_val, end_val, comment = validar_bst_eliminar(init_test, end_test, nodo, ans) 

    #out.clear_output()
    dis = displayBST(estructura)
    print('Eliminar llave', nodo, 'resultado', ans)
    print(state_val, comment)
    print("BST Preorden", end_test)
    print('Size BST', estructura.size())
    print('Height BST', estructura.height())
    print('minKey BST', estructura.minKey())

    info = {"Eliminar llave": nodo,
            'state': state_val,
            'comment': comment,
            'BST Preorden': end_test,
            'Size BST': estructura.size(),
            'Height BST': estructura.height(),
            'minKey BST': estructura.minKey(),
            'Se esperaba BST Preorden': None,
            'Se obtuvo BST Preorden': None}

    if state_val != VALIDATION_STATES[1]: # Si no fue exitoso, mostrar los resultados esperados y obtenidos
        print('Se esperaba BST Preorden:', end_val)
        print('Se obtuvo BST Preorden  :', end_test)
        info['Se esperaba BST Preorden'] = end_val
        info['Se obtuvo BST Preorden'] = end_test
    
    return dis, estructura, info

def encontrarNodoBST(estructura, nodo):
    """
    Encuentra un nodo en la estrcutura

    Args:
        estructura: BST
        nodo: valor del nodo
    Returns:
        -
    Raises:
        Exception
    """
    try:
        ans = estructura.isNodeValue(nodo)
        nodos = estructura.getNodeValues("Preorder")
        state_val, end_ans, end_val, comment = validar_bst_encontrar(nodos, nodo, ans) 
    except:
        e = '\tProblema al buscar la llave"' + str(nodo) + '", función isNodeValue()'
        raise Exception(e)

    #out.clear_output()
    lista = list()
    lista.append(nodo)
    if ans:
        dis = displayBST(estructura, lista)
    else:    
        dis = displayBST(estructura)
        
    print('Buscar elemento', nodo, 'resultado', ans)
    print(state_val, comment)

    info = {"Buscar elemento": nodo,
            "Resultado": ans, 
            'state': state_val,
            'comment': comment,
            'Se esperaba BST resultado': None,
            'Se obtuvo BST resultado': None,
            'Se esperaba BST Preorden': None,
            'Se obtuvo BST Preorden': None}

    if state_val != VALIDATION_STATES[1]: # Si no fue exitoso, mostrar los resultados esperados y obtenidos
        print('Se esperaba BST resultado', end_ans, 'Preorden:', end_val)
        print('Se obtuvo BST resultado  ', ans, 'Preorden:', nodos)
        info["Se esperaba BST resultado"] = end_ans
        info['Se obtuvo BST resultado'] = ans
        info['Se esperaba BST Preorden'] = end_val
        info['Se obtuvo BST Preorden'] = nodos

    return dis,estructura,info
    
def findAdjacentNodoBST(estructura, nodo):
    """
    Encuentra los adyacentes de un nodo en el BST

    Args:
        estructura: arbol BST
        nodo: valor del nodo
    Returns:
        -
    Raises:
        Exception
    """
    try:
        init_test = estructura.getNodeValues()
    except:
        e = '\tProblema al obtener todos las llaves, funcion getNodeValues()'
        raise Exception(e)
    try:
        existe, listaAdj = estructura.findAdjacentNode(nodo)
        print("intermedio", init_test, existe, listaAdj, nodo)
        state_val, existe_val, listaAdj_val, comment = validar_bst_adyacentes(init_test, existe, listaAdj, nodo) 
    except:
        e = '\tProblema al buscar los adyacentes del elemento "' + str(nodo) + '" , función findAdjacentNode()'
        raise Exception(e)
    
    #out.clear_output()
    dis = displayBST(estructura, listaAdj)
    print('Encontrar Adyacentes', nodo, 'resultado', existe, 'adyacentes', listaAdj)
    print(state_val, comment)


    info = {"Encontrar Adyacentes": nodo,
            "Resultado": existe, 
            "Adyacentes": listaAdj,
            'state': state_val,
            'comment': comment,
            'Se esperaba BST resultado': None,
            'Se obtuvo BST resultado': None,
            'Adyacentes obtenidos': None,
            'Adyacentes esperados': None}
    
    if state_val != VALIDATION_STATES[1]: # Si no fue exitoso, mostrar los resultados esperados y obtenidos
        print('Se esperaba resultado', existe_val, 'Adyacentes:', listaAdj_val)
        print('Se obtuvo resultado  ', existe, 'Adyacentes:', listaAdj)
        info["Se esperaba BST resultado"] = existe_val
        info['Se obtuvo BST resultado'] = existe
        info['Adyacentes obtenidos'] = listaAdj
        info['Adyacentes esperados'] = listaAdj_val
    
    return dis, estructura, info

def listarNodosBST(estructura, orden):
    """
    Lista todos los nodos del BST en el orden especificado

    Args:
        estructura: BST
        orden: orden en el cual se dan los nodos ('Preorder','Inorder', 'Postorder')
    Returns:
        -
    Raises:
        Exception
    """
    try:
        init_test = estructura.getNodeValues('Preorder')
    except:
        e = '\tProblema al obtener todas las llaves, función getNodeValues()'
        raise Exception(e)
    try:
        nodos = estructura.getNodeValues(orden)
        state_val, nodos_val, comment = validar_bst_darNodos(init_test, nodos, orden) 
    except:
        e = '\tProblema al listar todas las llaves, función getNodeValues()'
        raise Exception(e)
    
    #out.clear_output()
    dis = displayBST(estructura)
    print('Listar todas las llaves', orden)
    print(state_val, comment)
    print(nodos)
    print('Size BST', estructura.size())
    print('Height BST', estructura.height())
    print('minKey BST', estructura.minKey())
    
    info = {"Listar todas las llaves": orden,
            'state': state_val,
            'comment': comment,
            'Size BST': estructura.size(),
            'Nodes': nodos,
            'Height BST': estructura.height(),
            'minKey BST': estructura.minKey(),
            'Se esperaba': None,
            'Se obtuvo': None
            }

    if state_val != VALIDATION_STATES[1]: # Si no fue exitoso, mostrar los resultados esperados y obtenidos
        print('Se esperaba:', nodos_val)
        print('Se obtuvo:  ', nodos)
        info["Se esperaba"] = nodos_val
        info["Se obtuvo"] = nodos
    
    return dis, estructura, info


#Metodos enlace RBT
def crearRBT(init, file, data={}):
    """
    Crea un arbol RBT

    Args:
        init: Vacia, Random, Estática, Archivo
        file: Estructura de datos externa
        data: JSON con la información de la inicializacion de la estructura

    Returns:
        La estructura de datos creada
    Raises:
        Exception
    """
    try:
        print('Crear RBT')
        estructura = file.RBT()
    except Exception as e:
        print('Error')
        #e = "\tProblema al crear el arbol BST, método bst()"
        print(e)
        raise Exception(e + "\tProblema al crear el arbol BST, método bst()")
    long = 0
    nodos = list()
    if init == 'Random':
        long = random.randint(5,10)
        nodos = create_n_random(long)
        for i in nodos:
            try:
                estructura.addNode_byValue(i)
            except:
                e = '\tProblema al añadir el elemento "'+str(i)+'", método addNode_byValue()'
                raise Exception(e)
    elif init == 'Estática' or init == 'Archivo':
        try:
            nodos = data["valores"]
        except:
            raise Exception("El formato del archivo ingresado no es válido")
        for i in nodos:
            try:
                estructura.addNode_byValue(i)
            except:
                e = '\tProblema al añadir el elemento "'+str(i)+'", método addNode_byValue()'
                raise Exception(e)
    dis = displayRBT(estructura) 

    
    try:
        st_nodos = estructura.getNodeValues("Preorder")
    except:
        e = '\tProblema al obtener las llaves, método getNodeValues()'
        raise Exception(e)
    try:
        nodos_color = estructura.getNodeValues("Preorder_with_color")
    except:
        e = '\tProblema al obtener las llaves, método getNodeValues() el realizar el recorrido preorden con color'
        raise Exception(e)

    state_val, comment, end_val= validar_rbt_crear(nodos, st_nodos, nodos_color)
    
    print('Crear RBT ' + init + ':')
    print(state_val)    
    print(comment)
    #print('Altura del arbol: ', str(omap.height(estructura.estructura)))

    info = {"Total llaves": str(len(nodos_color)),
            'Crear RBT': init,
            'state': state_val,
            'comment': comment,
            'RBT Preorden': nodos_color,
            'Size RBT': estructura.size(),
            'Height RBT': estructura.height(),
            'minKey RBT': estructura.minKey(),
            'Se esperaba RBT Preorden': None,
            'Se obtuvo RBT Preorden': None}
    
    if state_val != VALIDATION_STATES[1]: # Si no fue exitoso, mostrar los resultados esperados y obtenidos
        info['Se esperaba RBT Preorden'] = end_val
        info['Se obtuvo RBT Preorden'] = nodos_color

    return dis, estructura, info

def anadirNodoRBT(estructura, nodo):
    """
    Añade un nodo al RBT

    Args:
        estructura: arbol RBT
        nodo: valor del nodo
    Returns:
        -
    Raises:
        Exception
    """
    try:
        init_test = estructura.getNodeValues("Preorder")
    except:
        e = '\tProblema al obtener las llaves, método getNodeValues()'
        raise Exception(e)
    try:
        estructura.addNode_byValue(nodo) # Ejecutar funcion de Prueba
        print('Get node values')
        end_test = estructura.getNodeValues("Preorder")
        print('Get node values post')
        print(end_test)
        state_val, end_val, comment = validar_rbt_anadir(init_test, end_test, nodo) 
    except:
        e = '\tProblema al añadir el elemento "'+str(nodo)+'", método addNode_byValue()'
        raise Exception(e)
    
    dis = displayRBT(estructura)
    print('Añadir elemento')
    
    print(state_val + ':', comment)

    print("Llaves: ", end_test)
    print('Altura del arbol: ', str(estructura.size()))

    info = {"Añadir elemento": nodo,
            'state': state_val,
            'comment': comment,
            'Altura del arbol': str(estructura.size()),
            'Se esperaba': None,
            'Se obtuvo': None}

    if state_val != VALIDATION_STATES[1]:  # Resultado No exitoso
        print('Se esperaba:', end_val)
        print('Se obtuvo:  ', end_test)
        info['Se esperaba'] = end_val
        info['Se obtuvo'] = end_test
    

    info = {"Añadir llave": nodo,
            'state': state_val,
            'comment': comment,
            'RBT Preorden': end_test,
            'Size RBT': estructura.size(),
            'Height RBT': estructura.height(),
            'minKey RBT': estructura.minKey(),
            'Se esperaba RBT Preorden': None,
            'Se obtuvo RBT Preorden': None}

    if state_val != VALIDATION_STATES[1]:
        print('Se esperaba RBT Preorden:', end_val)
        print('Se obtuvo RBT Preorden  :', end_test)
        info['Se esperaba RBT Preorden'] = end_val
        info['Se obtuvo RBT Preorden'] = end_test

    
    return dis,estructura,info

def eliminarNodoRBT(estructura, nodo):
    """
    Elimina un nodo al BST

    Args:
        estructura: BST
        nodo: valor del nodo
    Returns:
        -
    Raises:
        Exception
    """
    try:
        init_test = estructura.getNodeValues("Preorder")
    except:
        e = '\tProblema al obtener todos los elementos, método getNodeValues()'
        raise Exception(e)
    try:
        ans = estructura.deleteNode_byValue(nodo)
        end_test = estructura.getNodeValues("Preorder")
        state_val, end_val, comment = validar_rbt_eliminar(init_test, end_test, nodo, ans) 
    except:
        e = '\tProblema al eliminar el elemento "'+str(nodo)+'", método deleteNode_byValue()'
    
    
    dis = displayRBT(estructura)
    print('Eliminar elemento')
    
    print(state_val + ':', comment)

    nodos = estructura.getNodeValues()
    print("Vertices: ", nodos)
    print('Altura del arbol: ', str(estructura.size()))

    info = {"Eliminar Llave": nodo,
            'state': state_val,
            'comment': comment,
            'RBT Preorden': end_test,
            'Size RBT': estructura.size(),
            'Height RBT': estructura.height(),
            'minKey RBT': estructura.minKey(),
            'Se esperaba RBT Preorden': None,
            'Se obtuvo RBT Preorden': None}

    if state_val != VALIDATION_STATES[1]:
        print('Se esperaba RBT Preorden:', end_val)
        print('Se obtuvo RBT Preorden  :', end_test)
        info['Se esperaba RBT Preorden'] = end_val
        info['Se obtuvo RBT Preorden'] = end_test
    
    return dis, estructura, info

def encontrarNodoRBT(estructura, nodo):
    """
    Encuentra un nodo en la estrcutura

    Args:
        estructura: BST
        nodo: valor del nodo
    Returns:
        -
    Raises:
        Exception
    """
    try:
        ans = estructura.isNodeValue(nodo)
        nodos = estructura.getNodeValues("Preorder")
        state_val, ans_val, comment = validar_rbt_encontrar(nodos, nodo, ans) 
    except:
        e = '\tProblema al buscar el elemento "' + str(nodo) + '", método isNodeValue()'
        raise Exception(e)


    lista = list()
    lista.append(nodo)
    if ans_val:
        dis =displayRBT(estructura, lista)
    else:    
        dis = displayRBT(estructura)

    print('Buscar Elemento')
    print(state_val, comment)

    info = {"Buscar Elemento": nodo,
            'state': state_val,
            'comment': comment,
            "Vertices":nodos,
            'Altura del arbol':  (str(estructura.size()))}

    info = {"Buscar Elemento": nodo,
            'state': state_val,
            'comment': comment,
            'RBT Preorden': nodos,
            'Size RBT': estructura.size(),
            'Height RBT': estructura.height(),
            'minKey RBT': estructura.minKey()}
        
    return dis, estructura, info


    
def findAdjacentNodoRBT(estructura, nodo):
    """
    Encuentra los adyacentes de un nodo en el bst

    Args:
        estructura: lista enlazada
        nodo: valor del nodo
    Returns:
        -
    Raises:
        Exception
    """
    try:
        init_test = estructura.getNodeValues()
    except:
        e = '\tProblema al obtener todos los elementos, método getNodeValues()'
        raise Exception(e)
    try:
        listaAdj = estructura.findAdjacentNode(nodo)
        state_val, listaAdj_val, comment, exists = validar_rbt_adyacentes(init_test, listaAdj, nodo) 
    except:
        e = '\tProblema al buscar los adyacentes del elemento "' + str(nodo) + '" , método findAdjacentNode()'
        raise Exception(e)
    
    dis = displayRBT(estructura, listaAdj)
    
    if not exists:
        print('Encontrar Adyacentes\n\tEl elemento "'+str(nodo)+ '" no existe en el bst')
    else:
        print('Encontrar Adyacentes')
        print(state_val, comment)
    
    nodos = estructura.getNodeValues()
    print("Nodos: ", nodos)
    print('Altura del arbol: ', str(estructura.size()))
    
    info = {"Encontrar Adyacentes": nodo, 
            "Adyacentes": listaAdj,
            'state': state_val,
            'comment': comment,
            'Adyacentes obtenidos': None,
            'Adyacentes esperados': None}
    
    if state_val != VALIDATION_STATES[1]: # Si no fue exitoso, mostrar los resultados esperados y obtenidos
        info['Adyacentes obtenidos'] = listaAdj
        info['Adyacentes esperados'] = listaAdj_val
    
    return dis, estructura, info
    

def listarNodosRBT(estructura, orden):
    """
    Lista todos los nodos del BST en el orden especificado

    Args:
        estructura: lista enlazada
        orden: orden en el cual se dan los nodos (preorden,inorden, postorden)
    Returns:
        -
    Raises:
        Exception
    """
    try:
        #init_test = estructura.getNodeValues()
        x = 1
    except:
        e = '\tProblema al obtener todos los elementos, método getNodeValues()'
        raise Exception(e)
    try:
        nodos = estructura.getNodeValues(orden)
        #state_val, nodos_val, comment = validar(init_test, nodos, orden) 
    except:
        e = '\tProblema al listar todos los elementos, método getNodeValues()'
        raise Exception(e)
    
    dis = displayRBT(estructura)
    print('Listar todos los vertices')
    print(nodos)
    print('Altura del arbol: ', str(estructura.size()))
    #print(state_val, comment)

    info = {"Listar todas las llaves": orden,
            'state': "SUCCESFUL",
            'comment': "No hay validación",
            'Size RBT': estructura.size(),
            'Nodes': nodos,
            'Height RBT': estructura.height(),
            'minKey RBT': estructura.minKey(),
            'Se esperaba': None,
            'Se obtuvo': None
            }

    """if state_val != VALIDATION_STATES[1]: # Si no fue exitoso, mostrar los resultados esperados y obtenidos
        print('Se esperaba:', nodos_val)
        print('Se obtuvo:  ', nodos)
        info["Se esperaba"] = nodos_val
        info["Se obtuvo"] = nodos"""
    
    return dis, estructura, info
