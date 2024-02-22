from graphviz import Digraph, Graph
from soporte.soporte import createTuples
#from IPython.display import display, clear_output, SVG, HTML
from flask import Flask, send_file
from io import BytesIO




VALIDATION_STATES = {0:'WARNING', 1:'SUCCESSFUL', -1:'FAILED'} # Estados resultantes del proceso de validacion
colorPointer = 'grey'   # Color para apuntadores
colorRight = 'blue'     # Color para conexiones a la derecha
colorLeft = 'green'     # Color para conexiones a la izquierda
colorHigh = 'red'       # Color para resaltar un elemento
col = "black"           # Color por defecto


def displayList(estructura, tipo, nodosX=list()):
    '''
    Grafica en el Canvas la lista que entra por parametro, del tipo dado, y resalta los nodos
    que se encuentren en la lista nodosX
       
    Args:
        estructura: estructura de datos que debe ser una lista enlazada
        tipo: tipo de la estructura (1: Sencilla, 2: doble)
        nodosX: lista de valores de nodos que se resaltan (pintan en otro color)
    
    Returns:
        -
    '''
    try:
        nodos = estructura.getNodeValues()
    except:
        e = '\tProblema en el método getNodeValues()'
        raise Exception(e)
    
    dot = Digraph()
    
    dot.graph_attr = {
        'rankdir': 'LR',
        'center': 'true',
        'size':'14,5',
        'ratio':'fill'
    }
    
    tuples = createTuples(nodos, tipo)
    
    for i,j in tuples:
        if j == 'First' or j == 'None':
            dot.node(name=str(i), label=str(j), shape="square", color='white')
        elif j in nodosX:
            dot.node(name=str(i), label=str(j), shape="square", color=colorHigh)
        else:
            dot.node(name=str(i), label=str(j), shape="square")
    if len(nodos) == 0:
        dot.node(name='-1', label='', shape="square", color='white')
        dot.edge(str(tuples[0][0]), str('-1'), color=colorPointer)
    else:
        for i in range(1,len(tuples)):
            if tuples[i-1][1] == 'First' and tuples[i][1] != 'None':
                dot.edge(str(tuples[i-1][0]), str(tuples[i][0]), color=colorPointer)
            elif tuples[i-1][1] == 'First' and tuples[i][1] == 'None':
                dot.edge(str(tuples[i-1][0]), str(tuples[i+1][0]), color=colorPointer)
            elif tuples[i-1][1] != 'None':
                dot.edge(str(tuples[i-1][0]), str(tuples[i][0]), color=colorRight)
        if tipo == 2:
            for i in range(1, len(tuples)-1):
                if tuples[i][1] != 'None':
                    dot.edge(str(tuples[i][0]), str(tuples[i-1][0]), color = colorLeft)
    
        """   if tipo == 2:
        dot2 = Digraph()
        dot2.graph_attr = {
            'rankdir': 'DT'
        }
        dot2.node(name='Colores', label='', color = 'black', shape="none", height="0.2", width = '0.01', fontsize='8.0')
        dot2.node(name='indicativoLeft', label='', color = 'black', shape="none", height="0.2", width = '0.01', fontsize='8.0')
        dot2.edge('indicativoLeft', 'Colores', color=colorLeft, minlen = '0.01', label='before', fontsize='8.0')

        dot3 = Digraph()
        dot3.node(name='Colores2', label='', color = 'black', shape="none", height="0.01", width = '0.01', fontsize='8.0')
        dot3.node(name='indicativoRight', label='', color = 'black', shape="none", height="0.01", width = '0.01', fontsize='8.0')
        dot3.edge('indicativoRight', 'Colores2', color=colorRight, minlen = '0.01', label='next', fontsize='8.0')

        #dot2.subgraph(dot3)
        #display(dot2)
        #display(dot)
        image_bytes = dot.pipe(format='svg')

        # Devolver la imagen como una respuesta HTTP
        return send_file(BytesIO(image_bytes), mimetype='image/svg+xml')"""
    #else:
    #display(dot)
    image_bytes = dot.pipe(format='svg')

        # Devolver la imagen como una respuesta HTTP
    return send_file(BytesIO(image_bytes), mimetype='image/svg+xml')