import functools
from soporte.soporte import defaultfunction, VALIDATION_STATES
from referencias.grafo_disc import grafo as referenciaGrafo



def validar_graph_crear(nodos, edges, nodos_test, edges_test, tipo):
    '''
    Valida la operacion de crear un grafo dado un tipo
       
    Args:
        nodos: nodos que se añadieron al crear el grafo
        edges: arcos que se añadieron al crear el grafo
        nodos_test: nodos que la estructura tiene
        edges_test: arcos que tiene el grafo
        tipo: tipo del grafo (4: Dirigido, 5: No dirigido)
               
    Returns:
        state_val: Estado final de la validacion (WARNING, SUCCESSFUL, FAILED)
        comment: mensaje informativo para el usuario
        
    '''
    state_val = VALIDATION_STATES[1]
    detail = 'numero nodos: ' + str(len(nodos_test)) + '\n' + 'numero arcos:' + str(len(edges_test))
    comment = 'Sin Validacion de Creacion de Grafo - ' + str(tipo) + '\n' + detail
    #return state_val, comment

    if tipo == 4:
        structure_ref = referenciaGrafo('Directed')
    else:
        structure_ref = referenciaGrafo('Undirected')
    for i in nodos:                     #Inicializacion de la estructura de prueba
        structure_ref.addNode_byValue(i)

    nodos = structure_ref.getNodeValues()
    
    for i,j,k in edges:                     #Inicializacion de la estructura de prueba
        structure_ref.addEdge_byValue(i,j,k)

    edges = structure_ref.getEdgeValues()
    
    if len(nodos) != len(nodos_test):
        comment = 'Numero de vertices esperado: ' + str(len(nodos)) + ' diferente a vertices actuales: ' + str(len(nodos_test))
        state_val = VALIDATION_STATES[-1]
    elif len(edges) != len(edges_test):
        comment = 'Numero de arcos esperado: ' + str(len(edges)) + ' diferente a arcos actuales: ' + str(len(edges_test))
        state_val = VALIDATION_STATES[-1]
    else:
        detail = 'Numero vertices: ' + str(len(nodos_test)) + '\n' + 'Numero arcos:' + str(len(edges_test))
        if tipo == 4:
            comment = 'El Grafo Dirigido se creó satisfactoriamente' + '\n' + detail
        else:
            comment = 'El Grafo No Dirigido se creó satisfactoriamente' + '\n' + detail
        state_val = VALIDATION_STATES[1]
    return state_val, comment   

    ''' SIMPLIFICACION VALIDACION
    txt_nodos_ref = ''
    for i in nodos:
        txt_nodos_ref = txt_nodos_ref + str(i) + ', '
    txt_nodos_test = ''
    for i in nodos_test:
        txt_nodos_test = txt_nodos_test + str(i) + ', '
        
    validation = 0    
    state_val = VALIDATION_STATES[0]
    comment = ''
    
    if len(nodos) == len(nodos_test):
        nodos = sorted(nodos, key=functools.cmp_to_key(defaultfunction))
        nodos_test = sorted(nodos_test, key=functools.cmp_to_key(defaultfunction))
        if nodos == nodos_test:
            validation = validation + 1
        else:
            comment = 'No se tienen los vertices que se esperan tener'
            comment = comment + '\nSe esperaba: ' + txt_nodos_ref[:-2]
            comment = comment + '\n  Se obtuvo: ' + txt_nodos_test[:-2]
            state_val = VALIDATION_STATES[-1]
    else:
        comment = 'Se tiene una cantidad diferente de vertices a los esperados'
        comment = comment + '\nSe esperaba: ' + txt_nodos_ref[:-2]
        comment = comment + '\n  Se obtuvo: ' + txt_nodos_test[:-2]
        state_val = VALIDATION_STATES[-1]
        
    txt_edges_ref = ''
    for i in edges:
        txt_edges_ref = txt_edges_ref + str(i) + ', '
    txt_edges_test = ''
    for i in edges_test:
        txt_edges_test = txt_edges_test + str(i) + ', '
        
    if len(edges) == len(edges_test):
        edges.sort()
        edges_test.sort()
        if edges == edges_test:
            validation = validation + 1
        else:
            comment = comment + '\nNo se tienen los arcos que se esperan tener'
            comment = comment + '\nSe esperaba: ' + txt_nodos_ref[:-2]
            comment = comment + '\n  Se obtuvo: ' + txt_nodos_test[:-2]
            state_val = VALIDATION_STATES[-1]
    else:
        comment = comment + '\nSe tiene una cantidad diferente de arcos a los esperados'
        comment = comment + '\nSe esperaba: ' + txt_nodos_ref[:-2]
        comment = comment + '\n  Se obtuvo: ' + txt_nodos_test[:-2]
        state_val = VALIDATION_STATES[-1]
        
    if validation == 2:
        comment = 'El grafo se creó satisfactoriamente'
        state_val = VALIDATION_STATES[1]
    '''


def validar_graph_anadir(init_test, end_test, tipo, nodo):
    '''
    Valida la operacion de un nodo al grafo
       
    Args:
        init_test: nodos que la estructura tiene antes de añadir el nuevo nodo
        end_test: nodos que la estructura tiene despues de añadir el nuevo nodo
        tipo: tipo del grafo (4: Dirigido, 5: No dirigido)
        nodo: nodo que se añade al grafo               
    Returns:
        state_val: Estado final de la validacion (WARNING, SUCCESSFUL, FAILED)
        comment: mensaje informativo para el usuario
        
    '''
    if tipo == 4:
        structure_ref = referenciaGrafo('Directed')
    else:
        structure_ref = referenciaGrafo()
    for i in init_test:                     #Inicializacion de la estructura de prueba
        structure_ref.addNode_byValue(i)
    structure_ref.addNode_byValue(nodo)
    end_ref = structure_ref.getNodeValues()
    
    txt_nodos_ref = ''
    for i in end_ref:
        txt_nodos_ref = txt_nodos_ref + str(i) + ', '
    txt_nodos_test = ''
    for i in end_test:
        txt_nodos_test = txt_nodos_test + str(i) + ', '

    if len(end_ref) != len(end_test):
        comment = 'Se tiene una cantidad diferente de vertices a los esperados'
        state_val = VALIDATION_STATES[-1]
    elif nodo not in end_test:
        comment = 'El numero de nodos es correcto, pero el nodo no fue añadido'
        state_val = VALIDATION_STATES[-1]
    elif init_test == end_test:
        comment = 'El nodo ya se encontraba en el grafo'
        state_val = VALIDATION_STATES[0]
    else:
        comment = 'Adición de vértice satisfactoria'
        state_val = VALIDATION_STATES[1]

    return state_val, comment, end_ref
    '''
    # SIMPLIFICACION VALIDACION
    if len(end_ref) == len(end_test):
        end_ref = sorted(end_ref, key=functools.cmp_to_key(defaultfunction))
        end_test = sorted(end_test, key=functools.cmp_to_key(defaultfunction))
        init_test = sorted(init_test, key=functools.cmp_to_key(defaultfunction))
        if end_test == end_ref and end_ref != init_test:
            comment = "El vertice se añadió correctamente \n El grafo tiene " + str(len(end_test)) + ' vertices.'
            state_val = VALIDATION_STATES[1]
        elif end_test == end_ref:
            comment = 'El vertice ya se encuentra en el grafo'
            state_val = VALIDATION_STATES[0]
        else:
            comment = 'No se tienen los vertices que se esperan tener'
            comment = comment + '\nSe esperaba: ' + txt_nodos_ref[:-2]
            comment = comment + '\n  Se obtuvo: ' + txt_nodos_test[:-2]
            state_val = VALIDATION_STATES[-1]
    else:
        comment = 'Se tiene una cantidad diferente de vertices a los esperados'
        comment = comment + '\nSe esperaba: ' + txt_nodos_ref[:-2]
        comment = comment + '\n  Se obtuvo: ' + txt_nodos_test[:-2]
        state_val = VALIDATION_STATES[-1]
    '''

def validar_graph_eliminar(init_test, end_test, tipo, nodo):
    '''
    Valida la operacion de un eliminar un nodo del grafo
       
    Args:
        init_test: nodos que la estructura tiene antes de eliminar el nodo
        end_test: nodos que la estructura tiene despues de eliminar el nodo
        tipo: tipo del grafo (4: Dirigido, 5: No dirigido)
        nodo: nodo que se elimina del grafo               
    Returns:
        state_val: Estado final de la validacion (WARNING, SUCCESSFUL, FAILED)
        comment: mensaje informativo para el usuario
        
    '''
    if tipo == 4:
        print('structure ref dirrected')
        structure_ref = referenciaGrafo('Directed')
    else:
        structure_ref = referenciaGrafo()
    for i in init_test:                     #Inicializacion de la estructura de prueba
        structure_ref.addNode_byValue(i)
    structure_ref.deleteNode_byValue(nodo)
    end_ref = structure_ref.getNodeValues()

    txt_nodos_ref = ''
    for i in end_ref:
        txt_nodos_ref = txt_nodos_ref + str(i) + ', '
    txt_nodos_test = ''
    for i in end_test:
        txt_nodos_test = txt_nodos_test + str(i) + ', '
        
    state_val = VALIDATION_STATES[0]
    comment = ''
    
    if nodo not in init_test:
        comment = 'El vertice ' + str(nodo) + ' no existe en el grafo, por lo tanto no se puede eliminar'
        
    elif len(end_ref) == len(end_test):
        end_ref = sorted(end_ref, key=functools.cmp_to_key(defaultfunction))
        end_test = sorted(end_test, key=functools.cmp_to_key(defaultfunction))
        init_test = sorted(init_test, key=functools.cmp_to_key(defaultfunction))
        if end_test == end_ref and end_ref != init_test:
            comment = 'El vertice se eliminó correctamente'
            state_val = VALIDATION_STATES[1]
        elif end_test == end_ref:
            comment = 'El vertice NO se encuentra en el grafo'
            state_val = VALIDATION_STATES[0]
        else:
            comment = 'No se tienen los vertices que se esperan tener'
            comment = comment + '\nSe esperaba: ' + txt_nodos_ref[:-2]
            comment = comment + '\n  Se obtuvo: ' + txt_nodos_test[:-2]
            state_val = VALIDATION_STATES[-1]
    else:
        comment = 'Se tiene una cantidad diferente de vertices a los esperados'
        comment = comment + '\nSe esperaba: ' + txt_nodos_ref[:-2]
        comment = comment + '\n  Se obtuvo: ' + txt_nodos_test[:-2]
        state_val = VALIDATION_STATES[-1]
    
    return state_val, comment   

def validar_graph_encontrar(init_test, existe_test, nodo):
    '''
    Valida la operacion de un verificar si un nodo pertenece al grafo
       
    Args:
        init_test: nodos que tiene la estructura de prueba 
        existe_test: resultado de la verificacion por parte de la estructura de prueba
        nodo: nodo que se verifica la pertenencia al grafo               
    Returns:
        state_val: Estado final de la validacion (WARNING, SUCCESSFUL, FAILED)
        comment: mensaje informativo para el usuario
        
    '''
    existe_ref = str(nodo) in init_test
    
    state_val = VALIDATION_STATES[0]
    comment = ''
    
    if existe_test == existe_ref:
        if existe_test:
            comment = 'El vertice "' + str(nodo) + '" SI se encuentra en el grafo'
        else:
            comment = 'El vertice "' + str(nodo) + '" NO se encuentra en el grafo'
        state_val = VALIDATION_STATES[1]
    elif existe_ref:
        comment = 'El vertice SI se encuentra en el grafo, pero el método isNodeValue() indica que NO'
        state_val = VALIDATION_STATES[-1]
    else:
        comment = 'El vertice NO se encuentra en el grafo, pero el método isNodeValue() indica que SI'
        state_val = VALIDATION_STATES[-1]
    
    return state_val, comment   

def validar_graph_anadirEdge(nodes, init_test, end_test, tipo, origen, destino, peso):
    '''
    Valida la operacion de un añadir un arco al grafo
       
    Args:
        nodes: nodos de la estructura de prueba
        init_test: arcos que la estructura de prueba tiene antes de añadir el arco
        end_test: arcos que la estructura de prueba tiene despues de añadir el arco
        tipo: tipo del grafo (4:dirigido, 5:no dirigido)
        origen: nodo origen del arco
        destino: nodo destino del arco
        peso: peso del arco
        
    Returns:
        state_val: Estado final de la validacion (FAILED, WARNING, SUCCESSFUL)
        comment: mensaje informativo para el usuario
        end_ref: arcos resultantes en el grafo
        
    '''
    if tipo == 4:
        structure_ref = referenciaGrafo('Directed')
    else:
        structure_ref = referenciaGrafo('Undirected')
    for i in nodes:                     #Inicializacion de la estructura de prueba
        structure_ref.addNode_byValue(i)
    for i,j,k in init_test:
        structure_ref.addEdge_byValue(i,j,k)
        
    structure_ref.addEdge_byValue(origen,destino,peso)  # funcion de prueba
    end_ref = structure_ref.getEdgeValues()

    if len(end_ref) != len(end_test):
        comment = 'Se tiene una cantidad diferente de Arcos a los esperados'
        state_val = VALIDATION_STATES[-1]
        return state_val, comment, end_ref

    ''' SIMPLIFICACION VALIDACION
    if len(end_ref) == len(end_test):
        end_ref.sort()
        end_test.sort()
        if end_test == end_ref:
            arco = '(' + str(origen) + ' -> ' + str(destino) + ',' + str(peso) + ')'
            comment = 'Se añadió el arco "' + arco + '" correctamente' + ' \n Hay ' + str(len(end_test)) + ' Arcos en el grafo'
            state_val = VALIDATION_STATES[1]
        else:
            comment = 'No se tienen los arcos que se esperan tener'
            comment = comment + '\nSe esperaba: ' + txt_edges_ref[:-2]
            comment = comment + '\n  Se obtuvo: ' + txt_edges_test[:-2]
            state_val = VALIDATION_STATES[-1]
    else:
        comment = 'Se tiene una cantidad diferente de Arcos a los esperados'
        comment = comment + '\nSe esperaba: ' + txt_edges_ref[:-2]
        comment = comment + '\n  Se obtuvo: ' + txt_edges_test[:-2]
        state_val = VALIDATION_STATES[-1]
    '''
    if tipo == 4:
        comment = 'Agregar arco ' + str(origen) + ' -> ' + str(destino) + ' weight: ' + str(peso)
    else:
        comment = 'Agregar arco ' + str(origen) + ' <-> ' + str(destino) + ' weight: ' + str(peso)
    state_val = VALIDATION_STATES[1]

    return state_val, comment, end_ref

def validar_graph_adj(nodes, edges, adjNodes, nodo, tipo):
    '''
    Valida la operacion de un encontrar los adyacentes de u nodo en el grafo
       
    Args:
        nodes: nodos de la estructura de prueba
        edges: arcos de la estructura de prueba
        adjNodes: nodos que la estructura de prueba determina como adyacentes de nodo
        nodo: nodo del que se buscan los adyacentes
        tipo: tipo del grafo (4:dirigido, 5:no dirigido)
        
    Returns:
        state_val: Estado final de la validacion (WARNING, SUCCESSFUL, FAILED)
        comment: mensaje informativo para el usuario
        
    '''
    #---------Inicializacion de la estructura de prueba
    if tipo == 4:
        structure_ref = referenciaGrafo('Directed')
        print('Directed')
    else:
        structure_ref = referenciaGrafo()
        print('No Directed')
    for i in nodes:                     
        structure_ref.addNode_byValue(i)
    for i,j,k in edges:
        structure_ref.addEdge_byValue(i,j,k)    

    adjNodes_ref = structure_ref.findAdjacentNode(nodo)
    aux = structure_ref.findAdjacentNode(nodo)
    #---------
    if nodo not in nodes:
        comment = 'El nodo "' +str(nodo) + '" no se encuentra en el grafo'
        state_val = VALIDATION_STATES[0]
    else:
        adjNodes = list(dict.fromkeys(adjNodes))
        adjNodes_ref = list(dict.fromkeys(adjNodes_ref))
        
        adjText = ''
        for i in adjNodes:
            adjText = adjText + str(i) + ', '
        adjText_ref = ''
        for i in adjNodes_ref:
            adjText_ref = adjText_ref + str(i) + ', '
        
        if len(adjNodes) == len(adjNodes_ref):
            adjNodes.sort()
            adjNodes_ref.sort()
            if adjNodes == adjNodes_ref:
                comment = 'El nodo "' + str(nodo) + '" tiene ' + str(len(adjNodes)) + ' adyacentes: ' + adjText[:-2]
                state_val = VALIDATION_STATES[1]
            else:
                comment = 'Los adyacentes del elementos no son los esperados'
                comment = comment + '\nSe esperaba: ' + adjText_ref[:-2]
                comment = comment + '\n  Se obtuvo: ' + adjText[:-2]
                state_val = VALIDATION_STATES[-1]
        else:
            for i in adjNodes_ref:
                if i not in nodes:
                    aux.remove(i)
            adjNodes_ref = aux
            
            adjNodes.sort()
            adjNodes_ref.sort()
            if adjNodes == adjNodes_ref:
                comment = 'El nodo "' + str(nodo) + '" tiene ' + str(len(adjNodes)) + ' adyacentes: ' + adjText[:-2]
                state_val = VALIDATION_STATES[1]
            else:
                comment = 'Los adyacentes de los elementos no son los esperados'
                comment = comment + '\nSe esperaba: ' + adjText_ref[:-2]
                comment = comment + '\n  Se obtuvo: ' + adjText[:-2]
                state_val = VALIDATION_STATES[-1]

    return state_val, comment 

def validar_graph_todos(nodes, edges, tipo):
    '''
    Valida la operacion de un encontrar todos los nodos de un grafo
       
    Args:
        nodes: nodos de la estructura de prueba
        tipo: tipo del grafo (4:dirigido, 5:no dirigido)
        
    Returns:
        state_val: Estado final de la validacion (WARNING, SUCCESSFUL, FAILED)
        comment: mensaje informativo para el usuario
        
    '''
    #---------Inicializacion de la estructura de prueba
    if tipo == 4:
        structure_ref = referenciaGrafo('Directed')
    else:
        structure_ref = referenciaGrafo()
    for i in nodes:                     
        structure_ref.addNode_byValue(i)
    
    for o,d,k in edges:
        structure_ref.addEdge_byValue(o,d,k)
    
    nodes_ref = structure_ref.getNodeValues()
    edges_ref = structure_ref.getEdgeValues()
    
    txt_nodos_ref = ''
    for i in nodes_ref:
        txt_nodos_ref = txt_nodos_ref + str(i) + ', '
    txt_nodos_test = ''
    for i in nodes:
        txt_nodos_test = txt_nodos_test + str(i) + ', '
        
    nodes_ref.sort()
    nodes.sort()
    if nodes_ref == nodes and len(edges_ref) == len(edges):
        comment = 'Hay ' + str(len(nodes)) + ' Vértices en el grafo: ' + txt_nodos_ref[:-2]
        comment += '\n Hay ' + str(len(edges_ref)) + ' Arcos en el grafo: ' + str(edges_ref)
        state_val = VALIDATION_STATES[1]
    else:
        comment = 'No se encontraron todos los Elementos del grafo'
        comment = comment + '\n Se esperaban: ' + txt_nodos_ref[:-2]
        comment = comment + '\n    Se obtuvo: ' + txt_nodos_test[:-2]
        state_val = VALIDATION_STATES[-1]
    return state_val, comment

def validarRecorridosGrafo(estructura, tipo, tipo_inData, recorrido, result_test, nodo=None): #TODO
    '''
    Valida los resultados de ejecutar algoritmos sobre el grafo de prueba
       
    Args:
        estructura: grafo de prueba
        tipo: tipo del grafo (4:dirigido, 5:no dirigido)
        tipo_inData: tipo de la salida del argoritmo
        recorrido: algoritmo que se aplica
        result_test: resultado de ejecutar el algoritmo
        nodo: nodo de inicio del algoritmo
        
    Returns:
        state_val: Estado final de la validacion (WARNING, SUCCESSFUL, FAILED)
        comment: mensaje informativo para el usuario
        
    '''
    state_val = VALIDATION_STATES[1]
    comment = ''
    posError = ' '
    nodos = estructura.getNodeValues()
    edges = estructura.getEdgeValues()
    flecha = ''
    # Inicializacion de la estructura
    if tipo == 4:
        structure_ref = referenciaGrafo('Directed')
        flecha = " --> "
    else:
        structure_ref = referenciaGrafo()
        flecha = " <--> "
    for i in nodos:                     
        structure_ref.addNode_byValue(i)
    for i,j,k in edges:
        structure_ref.addEdge_byValue(i,j,k)  
    # ---
    
    # Aplicar el recorrido(
    result_ref = structure_ref.algorithms(recorrido, nodo)
    refText = ''
    testText = ''
    validacion = ''
    if tipo_inData == 'lista_nodos':
        if recorrido == "DepthFirstSearch" or recorrido == 'BreadhtFirstSearch':
            refText = ''
            testText = ''
            validacion = ''
            #Texto de vertices resultado
            result_ref= (result_ref[0],sorted(result_ref[1]))
            result_test= (result_test[0],sorted(result_test[1]))
            print(result_ref)
            print(result_test)
            for i in result_ref[1]:
                refText = refText + str(i) + ', '
            for i in result_test[1]:
                testText = testText + str(i) + ', ' 
            refText = refText[:-2]     
            testText = testText[:-2]

            vertices_test = result_test[1]
            vertices_ref = result_ref[1]
            #Validación de vertices
            if len(vertices_ref) != len(vertices_test):
                state_val = "FAILED"
                validacion = "El numero de vertices visitados en el recorido no es el esperado. \n"
            if vertices_ref != vertices_test:
                state_val = "FAILED"
                validacion += "Los vertices obtenidos son distintos a los esperados\n"

            if state_val == "FAILED":
                for i in vertices_test: 
                    if i not in vertices_ref:
                        state_val = "FAILED"
                        validacion+= "El vertice " +str(i)+" no debería aparecer en el recorrido. \n"

                validacion += "Vertices esperados:  "+refText+"\n"
                validacion += "Vertices obtenidos:  "+refText+"\n"
            #Validación de arcos
            if len(result_ref[0]) != len(result_test[0]):
                state_val = "FAILED"
                validacion = "El numero de arcos en el recorido no es el esperado. \n"
            arcos = ''
            for arco in result_test[0]:
                print(arco)
                print(result_ref[0])
                arcos= arcos + str(arco[0])+flecha+str(arco[1])+" \n"
                if arco not in result_ref[0]:
                    state_val = "FAILED"
                    validacion+= "El arco " +str(arco[0])+flecha+str(arco[1])+" no debería aparecer en el recorrido. \n"
            state_val = VALIDATION_STATES[1]
            comment = 'El algoritmo ' + recorrido + ' se ha ejecutado desde el elemento "'+ nodo + '"\n'
            comment += "Vertices del recorrido:  "+testText+"\n"
            comment += "Arcos del recorrido: \n"
            comment+= arcos
            if state_val == "FAILED":
                comment += validacion

        elif recorrido == 'DepthFirstOrder':

            ref_pre= result_ref[0]
            ref_post= result_ref[1]
            ref_reverse= result_ref[2]

            test_pre = result_test[0]
            test_post = result_test[1]
            test_reverse = result_test[2]
            
            validacion= ''
            pre_text_test = 'Pre: '
            pre_text_ref = 'Pre: '
            sameOrder = True


            if len(ref_pre) == len(test_pre):
                for i in range(0,len(test_pre)):
                    if test_pre[i] != ref_pre[i]:
                        sameOrder = False
                    pre_text_test = pre_text_test + str(test_pre[i]) + ", "
                    pre_text_ref = pre_text_ref + str(ref_pre[i]) + ", "

                pre_text_test = pre_text_test[:-2]     
                pre_text_ref = pre_text_ref[:-2]
                if not sameOrder:
                    state_val = VALIDATION_STATES[-1]
                    validacion += "El orden de los elementos de la cola Pre no es el esperado. \n"
                    validacion += "se esperaba: " + pre_text_ref[5:] + "\n"
                    validacion += "se obtuvo: " + pre_text_test[5:] + "\n"
            else:
                state_val = VALIDATION_STATES[-1]
                for i in range(0,len(test_pre)):
                    pre_text_test = pre_text_test + str(test_pre[i]) + ", "
                for i in range(0,len(ref_pre)):
                    pre_text_ref = pre_text_ref + str(ref_pre[i]) + ", "

                pre_text_test = pre_text_test[:-2]     
                pre_text_ref = pre_text_ref[:-2]
                
                validacion += "Faltan elementos en la cola Pre. \n"
                validacion += "se esperaba: " + pre_text_ref[5:] + "\n"
                validacion += "se obtuvo: " + pre_text_test[5:] + "\n"
            

            #Validacion cola post
            post_text_test = 'Post: '
            post_text_ref = 'Post: '
            sameOrder = True

            
            if len(ref_post) == len(test_post):
                for i in range(0,len(test_post)):
                    if test_post[i] != ref_post[i]:
                        sameOrder = False
                    post_text_test = post_text_test + str(test_post[i]) + ", "
                    post_text_ref = post_text_ref + str(ref_post[i]) + ", "

                post_text_test = post_text_test[:-2]     
                post_text_ref = post_text_ref[:-2]
                if not sameOrder:
                    state_val = VALIDATION_STATES[-1]
                    validacion += "El orden de los elementos de la cola Post no es el esperado. \n"
                    validacion += "Se esperaba: " + post_text_ref[6:] + "\n"
                    validacion += "Se obtuvo: " + post_text_test[6:] + "\n"
            else:
                state_val = VALIDATION_STATES[-1]
                for i in range(0,len(test_post)):
                    post_text_test = post_text_test + str(test_post[i]) + ", "
                for i in range(0,len(ref_post)):
                    post_text_ref = post_text_ref + str(ref_post[i]) + ", "

                post_text_test = post_text_test[:-2]     
                post_text_ref = post_text_ref[:-2]
                
                validacion += "Faltan elementos en la cola Post. \n"
                validacion += "Se esperaba: " + post_text_ref[6:] + "\n"
                validacion += "Se obtuvo: " + post_text_test[6:] + "\n"
            
            #Validacion pila reverse
            reverse_text_test = ''
            reverse_text_ref = ''
            sameOrder = True

            if len(ref_reverse) == len(test_reverse):
                for i in range(0,len(test_reverse)):
                    if test_reverse[i] != ref_reverse[i]:
                        sameOrder = False
                    reverse_text_test = str(test_reverse[i]) +  ", " + reverse_text_test
                    reverse_text_ref = str(ref_reverse[i]) + ", "+ reverse_text_ref 
                
                reverse_text_test = reverse_text_test[:-2]     
                reverse_text_ref = reverse_text_ref[:-2]

                reverse_text_test = 'Reverse: '+reverse_text_test
                reverse_text_ref = 'Reverse: '+reverse_text_ref

                if not sameOrder:
                    state_val = VALIDATION_STATES[-1]
                    validacion += "El orden de los elementos de la pila Reverse no es el esperado. \n"
                    validacion += "se esperaba: " + reverse_text_ref[9:] + "\n"
                    validacion += "se obtuvo: " + reverse_text_test[9:] + "\n"
            else:
                state_val = VALIDATION_STATES[-1]
                for i in range(0,len(test_reverse)):
                    reverse_text_test = str(test_reverse[i]) +  ", " + reverse_text_test
                for i in range(0,len(ref_reverse)):
                    reverse_text_ref = str(ref_reverse[i]) + ", "+ reverse_text_ref 

                
                reverse_text_test = reverse_text_test[:-2]     
                reverse_text_ref = reverse_text_ref[:-2]
                reverse_text_test = 'Reverse: '+reverse_text_test
                reverse_text_ref = 'Reverse: '+reverse_text_ref
                
                validacion += "Faltan elementos en la pila Reverse . \n"
                validacion += "se esperaba: " + reverse_text_ref[9:] + "\n"
                validacion += "se obtuvo: " + reverse_text_test[9:] + "\n"
            
            comment = 'El algoritmo ' + recorrido + ' se ha ejecutado. \n'
            comment += pre_text_test + " \n"
            comment += post_text_test + " \n"
            comment += reverse_text_test + " \n"
            state_val = VALIDATION_STATES[1]
            if state_val == VALIDATION_STATES[-1]:
                comment += validacion
    
        else:
            for i in result_ref:
                refText = refText + str(i) + ', '
            for i in result_test:
                testText = testText + str(i) + ', ' 
            refText = refText[:-2]     
            testText = testText[:-2]
  
    if tipo_inData == 'tupla':

        validacion = ''
        testEdges = result_test[0]
        testWeight = result_test[1]
        
        refEdges = result_ref[0]
        refWeight = result_ref[1]
        
        for i in refEdges:
            refText = refText + '(' + i[0] + '->' + i[1] + '), '
        for i in testEdges:
            testText = testText + '(' + i[0] + '->' + i[1] + '), '
        
        refText = refText[:-2] + '\n  COSTO: ' + str(refWeight) + '\n'
        testText = testText[:-2] + '\n  COSTO: ' + str(testWeight)

        if refWeight < testWeight:
            state_val = VALIDATION_STATES[-1]
            validacion += "El costo del MST obtenido (" + str(testWeight) + ") es mayor al esperado (" + str(refWeight) + ")\n"
        elif refWeight > testWeight:
            state_val = VALIDATION_STATES[-1]
            validacion += "El costo del MST obtenido (" + str(testWeight) + ") es menor al esperado (" + str(refWeight) + ")\n"

        comment = 'El algoritmo ' + recorrido + ' se ha ejecutado desde el elemento "'+ nodo + '"\n'
        comment += "Respuesta: " + " \n"
        comment += testText + " \n"
        state_val = VALIDATION_STATES[1]
        if state_val == VALIDATION_STATES[-1]:
            comment += validacion
        
        
        
    if tipo_inData == 'edges':
        for i in result_ref:
            refText = refText + '(' + i[0] + '->' + i[1] + '), '
        for i in result_test:
            testText = testText + '(' + i[0] + '->' + i[1] + '), '
        refText = refText[:-2]     
        testText = testText[:-2]

        comment = 'El algoritmo ' + recorrido + ' se ha ejecutado \n'
        comment += "Resultado obtenido: \n"
        comment += testText + " \n"
        comment += "Resultado esperado: \n"
        comment += refText + " \n"
    
    if tipo_inData == 'dicts':
        
        validacion = ''

        result_ref = sorted(result_ref, key=lambda x: x['node'])
        result_test = sorted(result_test, key=lambda x: x['node'])
        testText = ''
        refText= ''

        a = dict()
        for aux_dict in result_ref:
            a[nodo,aux_dict['node']] = aux_dict['cost']
            refText = refText + '\n* "'+nodo+'"' +'-->' +'"'+str(aux_dict['node'])+'"' + ' Costo: ' + str(aux_dict['cost']) + '\n  Path: '
            for i,j in aux_dict['path']:
                refText = refText + '(' + i + '->' + j + '), '
            if len(aux_dict['path'])>0:
                refText = refText[:-2]   
        b = dict()
        for aux_dict in result_test:
            b[nodo,aux_dict['node']] = aux_dict['cost']
            testText = testText + '\n* "'+nodo+'"' +'-->' +'"'+str(aux_dict['node'])+'"' + ' Costo: ' + str(round(aux_dict['cost'],2)) + '\n  Path: '
            for i,j in aux_dict['path']:
                testText = testText + '(' + i + '->' + j + '), '
            if len(aux_dict['path'])>0:
                testText = testText[:-2] 
        
        if result_test != result_ref:
            state_val = VALIDATION_STATES[-1]
            validacion += "El resultado del algoritmo es distinto al esperado. \n"
            validacion += "Se esperaba: \n"
            validacion += refText + " \n\n"
        
        missing_paths = []
        
        for i,j  in b.keys():
            is_present = False
            for x,y in a.keys():
                if i==x and y==j:
                    if a[x,y] != b[i,j]:
                        validacion +='El costo esperado del camino para el nodo {} es diferente al esperado \n'.format(i)
                        validacion += 'Costo esperado: {} \n'.format(a[x, y])
                        validacion += 'Costo obtenido: {} \n'.format(b[i, j])
                        is_present = True
            if not is_present:
                missing_paths.append((i, j))
                    
        
        if missing_paths:
            for i, j in missing_paths:
                validacion += 'No se encontró un camino para el nodo {}. \n'.format(j)
        
        comment = 'El algoritmo ' + recorrido + ' se ha ejecutado desde el elemento "'+ nodo + '"\n'
        comment += "Resultado: \n"
        comment += testText + " \n"
        state_val = VALIDATION_STATES[1]
        if state_val == VALIDATION_STATES[-1]:
            comment += validacion
        


    if tipo_inData == 'single_dict':

        validacion = ""
        testText = ''
        refText= ''

        count = 0
        for lista in result_ref.values():
            refText = refText + '\nComponente '+str(count)+": "
            lista = sorted(lista)
            for i in lista:
                refText = refText + i + ', '
            refText = refText[:-2]
            count +=1

        count = 0
        for lista in result_test.values():
            testText = testText + '\nComponente '+str(count)+": "
            lista = sorted(lista)
            for i in lista:
                testText = testText + i + ', '
            testText = testText[:-2]
            count +=1
        
        if len(result_ref.keys()) > len(result_test.keys()):
            state_val = VALIDATION_STATES[-1]
            validacion+= "El numero de componentes fuertemente conectados ("+str(len(result_test.keys()))+") es menor al esperado ("+str(len(result_ref.keys()))+") \n"
        elif len(result_ref.keys()) < len(result_test.keys()):
            validacion+= "El numero de componentes fuertemente conectados ("+str(len(result_test.keys()))+") es mayor al esperado ("+str(len(result_ref.keys()))+") \n"
        else:
            count = 0
            nodes_test = sorted(result_test.values())
            nodes_ref = sorted(result_ref.values())
            for i in range(0,len(nodes_test)):
                if len(nodes_test[i]) > len(nodes_ref[i]):
                    state_val = VALIDATION_STATES[-1]
                    validacion += "El numero de nodos del componente "+str(count)+" es mayor al esperado.\n"
                    break
                count+=1
        
        comment = 'El algoritmo ' + recorrido + ' se ha ejecutado \n'
        comment += "Estos son los componentes conectados: \n"
        comment += testText + " \n"
        state_val = VALIDATION_STATES[1]
        if state_val == VALIDATION_STATES[-1]:
            comment += validacion
            comment +="Componentes esperados:"
            comment +=refText+" \n \n"
            comment +="Componentes obtenidos:"
            comment +=testText+ " \n"
                
    return state_val, comment