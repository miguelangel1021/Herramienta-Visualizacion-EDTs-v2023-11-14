import random
import string




VALIDATION_STATES = {0:'WARNING', 1:'SUCCESSFUL', -1:'FAILED'} # Estados resultantes del proceso de validacion
colorPointer = 'grey'   # Color para apuntadores
colorRight = 'blue'     # Color para conexiones a la derecha
colorLeft = 'green'     # Color para conexiones a la izquierda
colorHigh = 'red'       # Color para resaltar un elemento
col = "black"           # Color por defecto
colorHighRBT = 'blue' # Color para resaltar un elemento RBT

def checkAlgoritmGraph(type, recorrido):
    '''
    Verifica si un algoritmo de grafos se puede aplicar sobre el grafo actual 

    Args:
        type: tipo del grafo actual: 4 (dirigido) 5(no dirigido)
        recorrido: Nombre del recorrido/algoritmo que se va a ejecutar
    
    Returns:
        True si el recorrido se puede aplicar al tipo de grafo actual.
        False de lo contrario
    '''
    both = ['Bellman-Ford', 'DepthFirstSearch', 'BreadhtFirstSearch', 'DepthFirstOrder', 'Dijkstra','KosarajuSCC']
    result = False
    comment = ''
    if recorrido in both:
        result = True
    elif recorrido == 'PrimMST':
        result = type == 5 or type == 7
        comment = 'ERROR: ' + recorrido + ' solo se puede aplicar a Grafos No Dirigidos'
    elif recorrido == 'KosarajuSCC' or recorrido == 'DirectedCycle':
        result = type == 4
        comment = 'ERROR: ' + recorrido + ' solo se puede aplicar a Grafos Dirigidos'
    return result, comment   

def getNodesGivenEdges(edges):
    '''
    Dado una lista de conexiones, retorna una lista con los nodos que se encuentran en las conexiones

    Args:
        edges: Lista de conexiones. 
        Cada conexión es una tupla: (nodo_origen, nodo_destino, peso)
    
    Returns:
        Lista de los valores de los nodos que se encuentran en las conexiones
    '''
    nodes = list()
    for i in edges:
        if i[0] not in nodes:
            nodes.append(i[0])
        if i[1] not in nodes:
            nodes.append(i[1])
    return nodes

def defaultfunction(elem_1, elem_2):
    '''
    Función de comparación entre dos elementos. Si son del mismo tipo de dato se comparan directamente, 
    de lo contrario se transforman ambos elementos a String y se realiza la comparación
    
    Args:
        elem_1: Elemento 1. 
        elem_2: Elemento 2.
    
    Returns:
        -1: Si el elemento 1 es menor al elemento 2
         0: Si el elemento 1 es igual al elemento 2
         1: Si el elemento 1 es mayor al elemento 2
    '''
    if type(elem_1) != type(elem_2):
        elem_1 = str(elem_1)
        elem_2 = str(elem_2)
    if elem_1 > elem_2:
        return 1
    elif elem_1 < elem_2:
        return -1
    return 0

def create_n_random(n):
    '''
    Crea una lista de numeros aleatorios sin repetición de longitud n.
       
    Args:
        n: tamaño de la lista
    
    Returns:
        Lista de n numeros aleatorios sin repeticion
    '''
    nodos = list()
    for i in range(n*n):
        num = random.randint(1,50)
        if num not in nodos:
            nodos.append(num)
        if len(nodos) == n:
            break
    return nodos 

def createTuples(nodos, tipo):
    '''
    Crea una lista de tuplas (id, elemento) creando las instancias adicionales (apuntadores)
    que se tienen en una lista enlazada dependiendo del tipo
       
    Args:
        nodos: elementos de la lista enlazada
        tipo: tipo de lista enlazada. (1: sencilla, 2: doble)
    
    Returns:
        Lista de tuplas de los elementos de nodos con ids unicos
    '''
    tuples = list()
    if tipo == 1:
        ids = range(0,len(nodos)+2)
        tuples.append((ids[0],'First'))
        for i in range(1,len(ids)-1):
            tuples.append((ids[i],nodos[i-1]))
        if len(nodos) > 0:
            tuples.append((ids[len(nodos)+1],'None'))
    else:
        ids = range(0,len(nodos)+3)
        tuples.append((ids[0],'First'))
        if len(nodos) > 0:
            tuples.append((ids[1],'None'))
            for i in range(2,len(ids)-1):
                tuples.append((ids[i],nodos[i-2]))
            tuples.append((ids[len(nodos)+2],'None'))
    return tuples

def get_random_string():
    '''
    Crea una String random de tamaño 20
       
    Args:
    
    Returns:
        String random de 20 caracteres
    '''
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(20))
    return result_str

def create_n_randomEdges(nodos, tipo = 4):
    '''
    Dado una lista de valores de nodos, se crean x conexiones entre ellos, donde
    n es un numero aleatorio entre 10 y la cantidad de nodos. 
       
    Args:
        nodos: lista de los elementos de los nodos de un grafo
        tipo: tipo de grafo (4: Dirigido, 5: No Dirigido)
    
    Returns:
        Lista de tuplas (nodo_origen, nodo_destino, costo)
    '''
    edges = list()
    edgesAux = list()
    ln = random.randint(10, len(nodos))
    for i in range(ln):
        a = random.choice(nodos)
        b = random.choice(nodos)
        while a == b:
            b = random.choice(nodos)
        if (a,b) not in edgesAux:
            if tipo != 4:
                if (b,a) not in edgesAux:
                    num = random.random() + random.randint(1,50)
                    edges.append((a,b,num))
                    edgesAux.append((a,b))
            else:
                num = random.random() + random.randint(1,50)
                edges.append((a,b,num))
                edgesAux.append((a,b))
    return edges

def validarEstructura(valid, tipo):
    '''
    Verifica si el tipo de una estructura de datos se enuentra entre las validas (valid) 
       
    Args:
        valid: lista de tipos de estructuras validas
        tipo: tipo de una estructura
    
    Returns:
        state: True si el tipo se encuentra en la lista de tipos validos, False de los contrario
        comment: Mensaje de error informando cual es la estructura del tipo ingresado
    '''
    if tipo in valid:
        state = True
        comment = ''
    else:
        state = False
        if tipo == 1:
            actual = 'Lista Encadenada Sencilla'
        elif tipo == 2:
            actual = 'Lista Encadenada Doble'
        elif tipo == 3:
            actual = 'Arbol BST'
        elif tipo == 4:
            actual = 'Grafo Dirigido'
        elif tipo == 5:
            actual = 'Arreglo'
        elif tipo == 6:
            actual = 'Tabla Hash LP'
        elif tipo == 8:
            actual = 'Arbol RBT'
        else:
            actual = 'Grafo NO Dirigido'
        comment = 'ERROR: La estructura actual es ' + actual
    return state, comment