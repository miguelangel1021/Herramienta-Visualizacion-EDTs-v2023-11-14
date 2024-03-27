from graphviz import Digraph, Graph
from soporte.soporte import createTuples
#from IPython.display import display, clear_output, SVG, HTML
from flask import Flask, send_file
from io import BytesIO


def displayGraph(estructura, tipo, label, nodosX=list(), edgesX=list(), nodeY=None):
    '''
    Grafica en el Canvas el grafo que entra por parametro, del tipo dado, y resalta los nodos
    que se encuentren en la lista nodosX, resalta los arcos que se encuentren en la lista de edgesX,
    y si hay un valor para nodeY lo resalta de un color diferente
       
    Args:
        estructura: estructura de datos que debe ser un grafo
        tipo: tipo de la estructura (4: Dirigido, 2: No Dirigido)
        label: indica si se muestran o no los pesos de los arcos
        nodosX: lista de valores de nodos que se resaltan (pintan en otro color)
        edgesX: lista de valores de arcos (tuplas) que se resaltan (pintan en otro color)
        nodeY: nodo que se resalta en un color diferente a los anteriores
    
    Returns:
        -
    '''
    nodes = estructura.getNodeValues()
    edges = estructura.getEdgeValues()
    edgesAux = estructura.getEdgeValues()
    for i,j,k in edges:
        if j not in nodes:
            edgesAux.remove((i,j,k))    
    edges = edgesAux
    if tipo == 4:
        dot = Digraph()
    else:
        dot = Graph()
    
    dot.graph_attr = {
        'rankdir': 'TB',
        'center': 'true',
        'size':'14,5',
        'ratio':'auto',
        'layout': 'neato',
        'mode': 'sgd',
    }
    
    for i in nodes:
        if i in nodosX:
            dot.node(name=i, label=i, shape='circle',color='red')
        elif i == nodeY:
            dot.node(name=i, label=i, shape='circle',color='blue')
        else:
            dot.node(name=i, label=i, shape='circle',color='black')
    if tipo == 4:
        for i,j,k in edges:
            if (i,j) in edgesX:
                if label:
                    dot.edge(i, j, label=str(round(k,2)), color='red', fontsize='8.0')
                else:
                    dot.edge(i, j, color='red')
            else:
                if label:
                    dot.edge(i, j, label=str(round(k,2)), color='black', fontsize='8.0')
                else:
                    dot.edge(i, j, color='black')
    else:
        tuples = list()
        for i,j,k in edges:
            inv = (j, i)
            if inv not in tuples:
                if (i,j) in edgesX or inv in edgesX:
                    if label:
                        dot.edge(i, j, label=str(round(k,2)), color='red', fontsize='8.0')
                    else:
                        dot.edge(i, j, color='red')
                else:
                    if label:
                        dot.edge(i, j, label=str(round(k,2)), color='black', fontsize='8.0')
                    else:
                        dot.edge(i, j, color='black')
            tuples.append((i, j))
    #display(dot)
            
    image_bytes = dot.pipe(format='svg')
    #devuelve la imagen en bytes
    return image_bytes 