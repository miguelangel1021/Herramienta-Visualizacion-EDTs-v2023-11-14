import random
from soporte.soporte import create_n_random,create_n_randomEdges,VALIDATION_STATES, checkAlgoritmGraph, getNodesGivenEdges
from .metodosValidacion import validar_graph_adj,validar_graph_anadir,validar_graph_anadirEdge,validar_graph_crear,validar_graph_eliminar,validar_graph_encontrar,validar_graph_todos,validarRecorridosGrafo
from .metodosGraficos import displayGraph


def crearGraph(init, tipo, file=None, data={},labels=False):
    """
    Crea un grafo

    Args:
        init: tipo de inicializacion de la estructura
        tipo: Dirigido(4) o no Dirigido(5)
        file: estructura de datos externa
        data: JSON con información de inicializacion
        labels: si se muestran o no los labels de los pesos
    Returns:
        La estructura creada
    Raises:
        Exception
    """
    
    if tipo == 4: txt = 'Dirigido - ' + init
    else: txt = 'No Dirigido - ' + init
    
    txtNodos = ''
    txtEdges = ''
    try:
        if tipo == 4:
            estructura = file.grafo(type='Directed')
        else:
            estructura = file.grafo(type='Undirected')
    except:
        e = "\tProblema al crear grafo, método graph()"
        raise Exception(e)
    long = 0
    nodos = list()
    edges = list()
    if init == 'Random':
        long = random.randint(10,15)
        nodos = create_n_random(long)
        edges = create_n_randomEdges(nodos, tipo)
        
        txtNodos = 'Elementos ('+str(len(nodos))+'): '
        if tipo == 5:
            txtEdges = 'Arcos ('+str(len(edges))+'):\n'
        else:
            txtEdges = 'Arcos ('+str(len(edges))+'):\n'
        for i in nodos:
            try:
                estructura.addNode_byValue(str(i))
                txtNodos = txtNodos + str(i) + ', '
            except:
                e = '\tProblema al añadir el elemento "'+str(i)+'", método addNode_byValue()'
                raise Exception(e)
        for i,j,k in edges:
            try:
                estructura.addEdge_byValue(str(i),str(j),k)
                if tipo == 5:
                    arco = '(' + str(i) + ' <-> ' + str(j) + ', ' + str(round(k,2))+ ')'
                else:
                    arco = '(' + str(i) + ' -> ' + str(j) + ', ' + str(round(k,2))+ ')'
                txtEdges = txtEdges + '\t' + arco + '\n'
            except:
                e = '\tProblema al añadir el arco "('+str(i)+ '->'+ str(j)+','+str(k) + ')", método addEdge_byValue()'
                raise Exception(e)
        
    elif init == 'Estática' or init == 'Archivo':
        try:
            nodos = data["nodos"]
            edges = data["edges"]
            txtNodos = 'Elementos ('+str(len(nodos))+'): '
            if tipo == 5:
                txtEdges = 'Arcos ('+str(len(edges))+'):\n'
            else:
                txtEdges = 'Arcos ('+str(len(edges))+'):\n'
                
            for i in nodos:
                try:
                    estructura.addNode_byValue(str(i))
                    txtNodos = txtNodos + str(i) + ', '
                except:
                    e = '\tProblema al añadir el elemento "'+str(i)+'", método addNode_byValue()'
                    raise Exception(e)
            for edge in edges:
                try:
                    estructura.addEdge_byValue(str(edge[0]),str(edge[1]),edge[2])
                    if tipo == 5:
                        arco = '(' + str(edge[0]) + ' <-> ' + str(edge[1]) + ', ' + str(edge[2])+ ')'
                    else:
                        arco = '(' + str(edge[0]) + ' -> ' + str(edge[1]) + ', ' + str(edge[2])+ ')'
                    txtEdges = txtEdges + '\t' + arco + '\n'
                except:
                    e = '\tProblema al añadir el arco "('+str(edge[0])+ '->'+ str(edge[1])+','+str(edge[2]) + ')", método addEdge_byValue()'
                    raise Exception(e)
        except:
            raise Exception("El formato del archivo ingresado no es válido")
          
    print('Num Nodes:', estructura.sizeNodes())
    print('Num Edges:', estructura.sizeEdges())

    try:
        st_nodos = estructura.getNodeValues()
    except:
        e = '\tProblema al obtener todos los vertices, método getNodeValues()'
        raise Exception(e)
    try:
        st_edges = estructura.getEdgeValues()
    except:
        e = '\tProblema al obtener todos los arcos, método getEdgeValues()'
        raise Exception(e)    
    
    state_val, comment = validar_graph_crear(nodos, edges, st_nodos, st_edges, tipo)
    
    dis = displayGraph(estructura, tipo, label=labels)
     
    print('Crear Grafo', txt)
    #print(txtNodos[:-2])
    print(st_nodos)
    #print(txtEdges)
    print(st_edges)
    print(state_val, comment)

    info = {'Operación': 'Crear Grafo' + txt,
            'Numero de nodos' : estructura.sizeNodes(),
            'Nodos': st_nodos,
            'Numero de Arcos': estructura.sizeEdges(),
            'Arcos': st_edges,
            'state': state_val,
            'comment': comment
    }


    return dis, estructura, info

def anadirNodoGraph(estructura, tipo, label, nodo):
    """
    Añade un nodo al grafo

    Args:
        estructura: grafo
        tipo: Dirigido(4) o no Dirigido(5)
        label: si se muestran o no los labels de los pesos
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
        estructura.addNode_byValue(nodo)   # Funcion a Probar
        end_test = estructura.getNodeValues()
        state_val, comment, end_ref = validar_graph_anadir(init_test, end_test, tipo, nodo) 
    except:
        e = '\tProblema al añadir el elemento "'+str(nodo)+'", método addNode_byValue()'
        raise Exception(e)
    
    
    dis = displayGraph(estructura, tipo, label, nodosX=[nodo])
    print('Añadir Vertice')
    print(state_val, comment)

    info = {'Operación': 'Añadir Vertice',
            'Nodo': str(nodo),
            'state': state_val,
            'comment': comment,
            'Numero de vertices esperados': None,
            'Numero de vertices obtenidos': None,
            'Vertices esperados': None,
            'Vertices obtenidos': None}
    
    if state_val != VALIDATION_STATES[1]:
        print("Se esperaba ", len(end_ref), " vértices")
        print("Se tienen ", len(end_test), " vértices")
        print("Se esperaba ", end_ref)
        print("Se tienen ", end_test)
        info['Numero de vertices esperados'] = len(end_ref)
        info['Numero de vertices obtenidos'] = len(end_test)
        info['Vertices esperados'] = end_ref
        info['Vertices obtenidos'] = end_test
    
    return dis, estructura, info


def eliminarNodoGraph(estructura, tipo, label, nodo):
    """
    Elimina un nodo del grafo

    Args:
        estructura: grafo
        tipo: Dirigido(4) o no Dirigido(5)
        label: si se muestran o no los labels de los pesos
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
        estructura.deleteNode_byValue(nodo)
        end_test = estructura.getNodeValues()
        state_val, comment = validar_graph_eliminar(init_test, end_test, tipo, nodo) 
    except:
        e = '\tProblema al eliminar el elemento "'+str(nodo)+'", método deleteNode_byValue()'
        raise Exception(e)
    
    
    dis = displayGraph(estructura, tipo, label)
    print(state_val, comment)

    info = {'Operación': 'Eliminar vertice',
            'Nodo': str(nodo),
            'state': state_val,
            'comment': comment}
    
    return dis, estructura, info

    
def existeNodoGraph(estructura, tipo, label, nodo):
    """
    Verifica la existencia de un nodo en el grafo

    Args:
        estructura: grafo
        tipo: Dirigido(4) o no Dirigido(5)
        label: si se muestran o no los labels de los pesos
        nodo: valor del nodo
    Returns:
        -
    Raises:
        Exception
    """
    try:
        init_test = estructura.getNodeValues()
    except:
        e = '\tProblema al obtener todos los Elementos, método getNodeValues()'
        raise Exception(e)
    try:
        existe_test = estructura.isNodeValue(nodo)
        state_val, comment = validar_graph_encontrar(init_test, existe_test, nodo) 
    except:
        e = '\tProblema al verificar si existe el Elemento "'+str(nodo)+'", método isNodeValue()'
        raise Exception(e)
    
    
    dis = displayGraph(estructura, tipo, label, nodosX=[nodo])
    print('Buscar elemento')
    print(state_val, comment)

    info = {'Operación': 'Buscar elemento',
            'Nodo': str(nodo),
            'state': state_val,
            'comment': comment}
    
    return dis, estructura, info
    
def anadirArcoGraph(estructura, tipo, label, origen, destino, peso):
    """
    Añade un arco al grafo

    Args:
        estructura: grafo
        tipo: Dirigido(4) o no Dirigido(5)
        label: si se muestran o no los labels de los pesos
        origen: valor del nodo origen
        destino: valor del nodo destino
        peso: peso del arco entre origen y destino
    Returns:
        -
    Raises:
        Exception
    """
    try:
        nodes = estructura.getNodeValues()
    except Exception as e:
        detail = '\tProblema al obtener los vertices iniciales, método getNodeValues()'
        raise Exception(detail + '\n' + e)
    try:
        init_test = estructura.getEdgeValues()         
    except Exception as e:
        detail = '\tProblema al obtener los arcos iniciales, método getEdgeValues()'
        raise Exception(detail + '\n' + e)

    comment = 'La funcion addEdge_byValue(...) agrego arco.'
    state_val = VALIDATION_STATES[1]

    pre_condition = True
    if (origen not in nodes):
        comment = "NO existe vertice origen " + str(origen) + " en el grafo"
        state_val = VALIDATION_STATES[-1]
        pre_condition = False

    if pre_condition and (destino not in nodes):
        comment = "NO existe vertice destino " + str(destino) + " en el grafo"
        state_val = VALIDATION_STATES[-1]
        pre_condition = False

    if pre_condition:
        if tipo == 5:
            for eds in init_test:
                if ((eds[0] == origen and eds[1] == destino) or (eds[0] == destino and eds[1] == origen)):
                    comment = 'NO se pueden añadir arcos paralelos'
                    state_val = VALIDATION_STATES[-1]
                    pre_condition = False
        else:
            for eds in init_test:
                if ((eds[0] == origen and eds[1] == destino)):
                    comment = 'NO se pueden añadir arcos paralelos'
                    state_val = VALIDATION_STATES[-1]
                    pre_condition = False

    if pre_condition:
        try:
            estructura.addEdge_byValue(origen,destino,peso)   # funcion de prueba
        except:
            #arco = '(' + str(origen) + ' -> ' + str(destino) + ',' + str(peso) + ')'
            #e = '\tProblema al añadir el arco "'+arco+'", método addEdge_byValue()\n\tVerificar la existencia de los vertices'
            comment = 'NO se pudo agregar arco. Falla funcion addEdge_byValue(...)'
            state_val = VALIDATION_STATES[-1]
            pre_condition = False

    if pre_condition:
        try:
            end_test = estructura.getEdgeValues()         
        except Exception as e:
            detail = '\tProblema al obtener los arcos finales, método getEdgeValues()'
            raise Exception(detail + '\n' + e)

    if pre_condition and tipo == 4:
        encontro_orig_dest = False
        for edge in end_test:
            if (edge[0] == origen) and (edge[1] == destino):
                encontro_orig_dest = True
                break
            
        if not encontro_orig_dest:
            comment = 'NO se agregó el arco de ' + str(origen) + ' -> ' + str(destino)
            state_val = VALIDATION_STATES[-1]
            pre_condition = False
            
    if pre_condition and tipo == 5:
        encontro_orig_dest = False
        encontro_dest_orig = False
        pre_comment = 'NO Existe el arco ' + str(origen) + ' -> ' + str(destino) + '\n'
        pre_comment += 'NO Existe el arco ' + str(destino) + ' -> ' + str(origen) + '\n'

        for edge in end_test:
            if (not encontro_orig_dest) and (edge[0] == origen) and (edge[1] == destino):
                pre_comment = 'Existe el arco ' + str(origen) + ' -> ' + str(destino) + '\n'
                encontro_orig_dest = True
                break
            if (not encontro_dest_orig) and (edge[0] == destino) and (edge[1] == origen):
                pre_comment = 'Existe el arco ' + str(destino) + ' -> ' + str(origen) + '\n'
                encontro_dest_orig = True
                break

        if not encontro_orig_dest:
            encontro_orig_dest = estructura.isEdgeValue(origen, destino)
            if not encontro_orig_dest:
                comment = pre_comment + 'La funcion isEdgeValue(...) NO reporta el arco de ' + str(origen) + ' -> ' + str(destino) + ' en grafo No Dirigido'
                state_val = VALIDATION_STATES[-1]
                pre_condition = False

        if pre_condition and (not encontro_dest_orig):
            encontro_dest_orig = estructura.isEdgeValue(destino, origen)
            if not encontro_dest_orig:
                comment = pre_comment + 'La funcion isEdgeValue(...) NO reporta el arco de ' + str(destino) + ' -> ' + str(origen) + ' en grafo No Dirigido'
                state_val = VALIDATION_STATES[-1]
                pre_condition = False

    if pre_condition:
        state_val, comment, end_val = validar_graph_anadirEdge(nodes, init_test, end_test, tipo, origen, destino, peso) 

    
    dis = displayGraph(estructura, tipo, label, edgesX=[(origen,destino)])
    print('Añadir Arco')
    print(state_val, comment)

    info = {'Operación': 'Añadir Arco',
            'Arco': str(origen) + ' -> ' + str(destino),
            'state': state_val,
            'comment': comment,
            'Numero arcos esperados':None,
            'Numero arcos obtenidos': None,
            'Arcos esperados': None,
            'Arcos obtenidos': None}



    if pre_condition and state_val != VALIDATION_STATES[1]:
        print('Numero arcos esperados: ', len(end_val), 'Numero arcos obtenidos: ', len(end_test))
        print('Se esperaba:', end_val)
        print('Se obtuvo:  ', end_test)
        info['Numero arcos esperados'] = len(end_val)
        info['Numero arcos obtenidos'] = len(end_test)
        info['Arcos esperados'] = end_val
        info['Arcos obtenidos'] = end_test
    
    return dis, estructura, info

def adyacentesNodoGraph(estructura, tipo, label, nodo):
    """
    Encuentra los adyacentes de un nodo en el grafo

    Args:
        estructura: grafo
        tipo: Dirigido(4) o no Dirigido(5)
        label: si se muestran o no los labels de los pesos
        nodo: valor del nodo
    Returns:
        -
    Raises:
        Exception
    """
    try:
        nodes = estructura.getNodeValues()
    except:
        e = '\tProblema al obtener todos los elementos, método getNodeValues()'
        raise Exception(e)
    try:
        edges = estructura.getEdgeValues()
    except:
        e = '\tProblema al obtener todos los arcos, método getEdgeValues()'
        raise Exception(e)
    try:
        adjNodes = estructura.findAdjacentNode(nodo)
        state_val, comment = validar_graph_adj(nodes, edges, adjNodes, nodo, tipo) 
    except:
        e = '\tProblema al encontrar los adyacentes del elemento "'+str(nodo)+'", método findAdjacentNode()'
        raise Exception(e)
    
    paintEdges = list()
    for i in adjNodes:
        paintEdges.append((nodo,i))
    
    
    dis =displayGraph(estructura, tipo, label, nodosX=adjNodes, edgesX=paintEdges, nodeY = nodo)
    print('Adyacentes elemento')
    print(state_val, comment)

    info = {'Operación': 'Adyacentes elemento',
            'state': state_val,
            'comment': comment}
    
    return dis, estructura, info

def encontrarNodosGraph(estructura, tipo, label):
    """
    Encuentra todos los nodos del grafo

    Args:
        estructura: grafo
        tipo: Dirigido(4) o no Dirigido(5)
        label: si se muestran o no los labels de los pesos
    Returns:
        -
    Raises:
        Exception
    """
    try:
        nodes = estructura.getNodeValues()
        edges = estructura.getEdgeValues()
    except:
        e = '\tProblema al obtener todos los elemento, método getNodeValues() o método getEdgeValues()'
        raise Exception(e)

    state_val, comment = validar_graph_todos(nodes, edges, tipo)

    
    dis = displayGraph(estructura, tipo, label)
    print('Encontrar todos los elemento:', state_val)
    print(comment)

    info = {'Operación': 'Encontrar todos los elementos',
            'state': state_val,
            'comment': comment}
    
    return dis, estructura, info

def recorridosGraph(estructura, tipo, label, recorrido, nodo=None):    
    """
    Ejecuta un algoritmo dado en el grafo

    Args:
        estructura: grafo
        tipo: Dirigido(4) o no Dirigido(5)
        label: si se muestran o no los labels de los pesos
        recorrido: nombre del algoritmo que se va a ejecutar
        nodo: nodo de inicio del algoritmo

    Returns:
        -
    Raises:
        Exception
    """
    if nodo is not None:
        try:
            dis = displayGraph(estructura, tipo, label)
            existe = estructura.isNodeValue(nodo)
        except:
            e = '\tProblema al verificar la existencia del elemento '+ nodo +', en el metodo getNodeValues()'
            raise Exception(e)
        if not existe:
            e = '\tEl elemento "'+ nodo +'" no pertenece al grafo.'
            raise Exception(e)
    rt, cmm = checkAlgoritmGraph(tipo, recorrido)
    if not rt:
        dis = displayGraph(estructura, tipo, label)
        raise Exception(cmm)
    try:
        rtaRecorrido = estructura.algorithms(recorrido, nodo)
    except:
        e = '\tProblema al ejecutar el recorrido ' + recorrido + ', metodo algorithms()'
        raise Exception(e)

    state_val = ''
    comment = ''
    if recorrido == 'DepthFirstSearch' or recorrido == 'BreadhtFirstSearch' or recorrido == 'DepthFirstOrder':
        if recorrido == 'DepthFirstSearch':
            rut = rtaRecorrido[1]
            rut.remove(nodo)
            edges = rtaRecorrido[0]
            state_val, comment = validarRecorridosGrafo(estructura, tipo, 'lista_nodos', recorrido, rut, nodo)
   #         rtaRecorrido.remove(nodo)
            dis = displayGraph(estructura, tipo, label, nodosX=rut, nodeY=nodo,  edgesX=edges)
        elif  recorrido == 'BreadhtFirstSearch':
            rut = rtaRecorrido[1]
            rut.remove(nodo)
            edges = rtaRecorrido[0]
            state_val, comment = validarRecorridosGrafo(estructura, tipo, 'lista_nodos', recorrido, rut, nodo)
            dis = displayGraph(estructura, tipo, label, nodosX=rut, nodeY=nodo,edgesX=edges)
        else:
            state_val, comment = validarRecorridosGrafo(estructura, tipo, 'lista_nodos', recorrido, rtaRecorrido, nodo)
            dis = displayGraph(estructura, tipo, label)
            
    elif recorrido == 'DirectedCycle':
        nodes = getNodesGivenEdges(rtaRecorrido)
        state_val, comment = validarRecorridosGrafo(estructura, tipo, 'edges', recorrido, rtaRecorrido)
        dis = displayGraph(estructura, tipo, label, nodosX=nodes,edgesX=rtaRecorrido)  
        
    elif recorrido == 'Dijkstra' or recorrido == 'Bellman-Ford':
        state_val, comment = validarRecorridosGrafo(estructura, tipo, 'dicts', recorrido, rtaRecorrido, nodo)
        #print(rtaRecorrido[0])
        edgex = list()
        for i in rtaRecorrido:
            aux = i['path']
            for j in aux:
                if j not in edgex:
                    edgex.append(j)
        dis = displayGraph(estructura, tipo, label, edgesX= edgex, nodeY=nodo)
        
    elif recorrido == 'KosarajuSCC':
        state_val, comment = validarRecorridosGrafo(estructura, tipo, 'single_dict', recorrido, rtaRecorrido)
        dis = displayGraph(estructura, tipo, label)
        
    elif recorrido == 'PrimMST':
        state_val, comment = validarRecorridosGrafo(estructura, tipo, 'tupla', recorrido, rtaRecorrido, nodo)
        edges = rtaRecorrido[0]
        nodes = getNodesGivenEdges(edges)
        dis = displayGraph(estructura, tipo, label, nodosX=nodes,edgesX=edges)

    print('Algoritmo ' + recorrido + ':' , state_val)
    print(comment)
    print(state_val)

    info = {'Operacion': 'Recorrido',
            'Algoritmo': recorrido,
            'state': state_val,
            'comment': comment}
    
    return dis,estructura,info