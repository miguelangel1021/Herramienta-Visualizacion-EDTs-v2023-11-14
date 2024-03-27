from DISClib.ADT import orderedmap as omap
from DISClib.ADT import list as lt
from DISClib.Algorithms.Trees import traversal as tr
from graphviz import Digraph, Graph
from soporte.soporte import defaultfunction,get_random_string,colorHigh,colorLeft,colorPointer,colorRight
from io import BytesIO

class BST_grafico():
    '''
    Clase auxiliar para graficar un arbol BST, usando la libreria graphviz
    adaptada de https://www.evamariakiss.de/apps/bstlearner_v1.php
    '''
    def __init__(self):
        self.estructura = omap.newMap(omaptype = 'BST', comparefunction = defaultfunction)

    def addNode_byValue(self, infoNodo):    
        self.estructura = omap.put(self.estructura, infoNodo, infoNodo)

    def getNodeValues(self):
        lst = list()
        if not omap.isEmpty(self.estructura):
            iter = lt.iterator(tr.preorder(self.estructura))
            for i in iter:
                lst.append(i)
        return lst

    def visualize(self, lst = []):
        tree = self.getNodeValues()
        if len(tree) > 0:
            tree = omap.get(self.estructura, tree[0])
            # Recursively add nodes and edges
            def add_nodes_edges(tree, dot=None):
                col = "black"
                # Create Graphviz Digraph 
                if dot is None:
                    dot = Digraph()
                    dot.graph_attr = {
                        'rankdir': 'TB',
                        'center': 'true',
                        'size':'14,5',
                        'ratio':'auto'
                    }
                    dot.node(name='root', label='root', color = 'white', shape="circle", fixedsize="True", width="0.4")
                    if (lst != [] and tree['value'] in lst):
                        dot.node(name=str(tree['value']), label=str(tree['value']), color = colorHigh, shape="circle", fixedsize="True", width="0.4")
                    else:
                        dot.node(name=str(tree['value']), label=str(tree['value']), color = col, shape="circle", fixedsize="True", width="0.4")
                    dot.edge('root', str(tree['value']), color=colorPointer)      
                
                # Add nodes recursively
                if tree['left'] != None:
                    if (lst != [] and tree['left']['value'] in lst):
                        col = "red"  
                    dot.node(name=str(tree['left']['value']), label=str(tree['left']['value']),
                            color = col, shape="circle", fixedsize="True", width="0.4")
                    col = "black"
                    dot.edge(str(tree['value']), str(tree['left']['value']),color=colorLeft)
                    dot = add_nodes_edges(tree['left'], dot=dot)
                else:
                    aux = get_random_string()
                    dot.node(name=aux, label='',
                            color = 'white', shape="circle", fixedsize="True", width="0.4")
                    dot.edge(str(tree['value']), aux,color=colorLeft)
                    #dot = add_nodes_edges(tree['left'], dot=dot)
                                
                if tree['right'] != None:
                    if (lst != [] and tree['right']['value'] in lst): 
                        col = "red" 
                    dot.node(name=str(tree['right']['value']), label=str(tree['right']['value']), 
                            color = col, shape="circle", fixedsize="True", width="0.4")
                    col = "black"
                    dot.edge(str(tree['value']), str(tree['right']['value']), color=colorRight)
                    dot = add_nodes_edges(tree['right'], dot=dot)            
                else:
                    aux = get_random_string()
                    dot.node(name=aux, label='',
                    color = 'white', shape="circle", fixedsize="True", width="0.4")
                    dot.edge(str(tree['value']), aux,color=colorRight)
                    #dot = add_nodes_edges(tree['left'], dot=dot)
                return dot        
            return add_nodes_edges(tree)                   

        else:
            dot = Digraph()
            dot.node(name='root', label='root', color = 'white', shape="circle", fixedsize="True", width="0.4")
            dot.node(name='-1', label='', shape="square", color='white')
            dot.edge('root', str(-1), color=colorPointer)
            return dot

def displayBST(estructura, nodosX = []):
    '''
    Grafica en el Canvas el arbol BST que entra por parametro y resalta los nodos
    que se encuentren en la lista nodosX
       
    Args:
        estructura: estructura de datos que debe ser una lista enlazada
        nodosX: lista de valores de nodos que se resaltan (pintan en otro color)
    
    Returns:
        -
    '''
    try:
        nodos = estructura.getNodeValues('Preorder')
    except:
        e = '\tProblema en el método getNodeValues()'
        raise Exception(e)
    
    bst = BST_grafico()
    for i in nodos:
        bst.addNode_byValue(i)
    dot = bst.visualize(nodosX)
    
    dot2 = Digraph()
    dot2.graph_attr = {
        'rankdir': 'DT'
    }
    dot2.node(name='Colores', label='', color = 'black', shape="none", height="0.2", width = '0.01', fontsize='8.0')
    dot2.node(name='indicativoLeft', label='', color = 'black', shape="none", height="0.2", width = '0.01', fontsize='8.0')
    dot2.edge('indicativoLeft', 'Colores', color=colorLeft, minlen = '0.01', label='left', fontsize='8.0')

    dot3 = Digraph()
    dot3.node(name='Colores2', label='', color = 'black', shape="none", height="0.01", width = '0.01', fontsize='8.0')
    dot3.node(name='indicativoRight', label='', color = 'black', shape="none", height="0.01", width = '0.01', fontsize='8.0')
    dot3.edge('indicativoRight', 'Colores2', color=colorRight, minlen = '0.01', label='right', fontsize='8.0')

    dot2.subgraph(dot3)
    #display(dot2)
    #display(dot)

    image_bytes = dot.pipe(format='svg')
    return image_bytes


#Metodos Graficos RBT
class RBT_grafico():
    '''
    Clase auxiliar para graficar un arbol RBT, usando la libreria graphviz
    adaptada de https://www.evamariakiss.de/apps/bstlearner_v1.php
    '''

    def __init__(self):
        self.estructura = omap.newMap(
            omaptype='RBT', comparefunction=defaultfunction)

    def addNode_byValue(self, infoNodo):
        self.estructura = omap.put(self.estructura, infoNodo, infoNodo)

    def addNode_byPosition(self, infoNodo, color):
        '''
        NEW FUNCTION
        Se agrega elemento en su posicion adecuada (sin necesidad de balancear) 
        y con su color respectivo.
        '''
        self.estructura = omap.put_by_position(self.estructura, infoNodo, infoNodo, color)

    def getNodeValues(self):
        lst = list()
        if not omap.isEmpty(self.estructura):
            iter = lt.iterator(tr.preorder(self.estructura))
            for i in iter:
                lst.append(i)
        return lst

    def visualize(self, lst=[]):
        tree = self.getNodeValues()
        if len(tree) > 0:
            tree = omap.get(self.estructura, tree[0])
            # Recursively add nodes and edges

            def add_nodes_edges(tree, dot=None):
                col = "black"
                # Create Graphviz Digraph
                if dot is None:
                    dot = Digraph()
                    dot.graph_attr = {
                        'rankdir': 'TB',
                        'center': 'true',
                        'size': '14,5',
                        'ratio': 'auto'
                    }
                    dot.node(name='root', label='root', color='white',
                             shape="circle", fixedsize="True", width="0.4")
                    if (lst != [] and tree['value'] in lst):
                        dot.node(name=str(tree['value']), label=str(tree['value']), color=colorHigh, shape="circle",
                                 fixedsize="True", width="0.4", style="filled", fillcolor=returnColor(tree), fontcolor="white")
                    else:
                        dot.node(name=str(tree['value']), label=str(tree['value']), color=col, shape="circle",
                                 fixedsize="True", width="0.4", style="filled", fillcolor=returnColor(tree), fontcolor="white")
                    dot.edge('root', str(tree['value']), color=colorPointer)

                # Add nodes recursively
                if tree['left'] != None:
                    col = "black"
                    if (lst != [] and tree['left']['value'] in lst):
                        col = "red"
                    dot.node(name=str(tree['left']['value']), label=str(tree['left']['value']),
                             color=col, shape="circle", fixedsize="True", width="0.4", style="filled", fillcolor=returnColor(tree["left"]), fontcolor="white")
                    #col = "black"
                    dot.edge(str(tree['value']), str(
                        tree['left']['value']), color=returnColor(tree["left"]))
                    dot = add_nodes_edges(tree['left'], dot=dot)
                else:
                    aux = get_random_string()
                    dot.node(name=aux, label='',
                             color='white', shape="circle", fixedsize="True", width="0.4")
                    dot.edge(str(tree['value']), aux, color=col)
                    #dot = add_nodes_edges(tree['left'], dot=dot)

                if tree['right'] != None:
                    col = "black"
                    if (lst != [] and tree['right']['value'] in lst):
                        col = "red"
                    dot.node(name=str(tree['right']['value']), label=str(tree['right']['value']),
                             color=col, shape="circle", fixedsize="True", width="0.4", style="filled", fillcolor=returnColor(tree["right"]), fontcolor="white")
                    #col = "black"
                    dot.edge(str(tree['value']), str(
                        tree['right']['value']), color=returnColor(tree["right"]))
                    dot = add_nodes_edges(tree['right'], dot=dot)
                else:
                    aux = get_random_string()
                    dot.node(name=aux, label='',
                             color='white', shape="circle", fixedsize="True", width="0.4")
                    dot.edge(str(tree['value']), aux, color=col)
                    #dot = add_nodes_edges(tree['left'], dot=dot)
                return dot
            return add_nodes_edges(tree)

        else:
            dot = Digraph()
            dot.node(name='root', label='root', color='white',
                     shape="circle", fixedsize="True", width="0.4")
            dot.node(name='-1', label='', shape="square", color='white')
            dot.edge('root', str(-1), color=colorPointer)
            return dot


def returnColor(node):
    if node["color"] == 0:
        return "red"
    return "black"


def displayRBT(estructura, nodosX=[]):
    '''
    Grafica en el Canvas el arbol RBT que entra por parametro y resalta los nodos
    que se encuentren en la lista nodosX

    Args:
        estructura: estructura de datos que debe ser un RBT
        nodosX: lista de valores de nodos que se resaltan (pintan en otro color)

    Returns:
        -
    '''
    try:
        nodos = estructura.getNodeValues('Preorder_with_color')
    except:
        e = '\tProblema en el método getNodeValues()'
        raise Exception(e)

    rbt = RBT_grafico()
    for i in nodos:
        # agregar cada llave en su posicion correcta (sin necesidad de balanceo) y color respectivo
        rbt.addNode_byPosition(i[0], i[1])  
    dot = rbt.visualize(nodosX)

    dot2 = Digraph()
    dot2.graph_attr = {
        'rankdir': 'DT'
    }
    dot2.node(name='Colores', label='', color='black', shape="none",
              height="0.2", width='0.01', fontsize='8.0')
    dot2.node(name='indicativoLeft', label='', color='black',
              shape="none", height="0.2", width='0.01', fontsize='8.0')
    dot2.edge('indicativoLeft', 'Colores', color=colorLeft,
              minlen='0.01', label='left', fontsize='8.0')

    dot3 = Digraph()
    dot3.node(name='Colores2', label='', color='black', shape="none",
              height="0.01", width='0.01', fontsize='8.0')
    dot3.node(name='indicativoRight', label='', color='black',
              shape="none", height="0.01", width='0.01', fontsize='8.0')
    dot3.edge('indicativoRight', 'Colores2', color=colorRight,
              minlen='0.01', label='right', fontsize='8.0')

    dot2.subgraph(dot3)
    #display(dot2)
    image_bytes = dot.pipe(format='svg')
    return image_bytes