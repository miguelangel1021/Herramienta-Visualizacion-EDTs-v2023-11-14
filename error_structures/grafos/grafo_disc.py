from DISClib.ADT import graph as g
from DISClib.ADT import list as lt
from DISClib.DataStructures import edge as e
from DISClib.ADT import stack
from DISClib.Algorithms.Graphs import bellmanford as bf
from DISClib.Algorithms.Graphs import bfs
from DISClib.Algorithms.Graphs import cycles as c
from DISClib.Algorithms.Graphs import dfs
from DISClib.Algorithms.Graphs import dfo
from DISClib.Algorithms.Graphs import prim
from DISClib.Algorithms.Graphs import scc
from DISClib.Algorithms.Graphs import dijsktra as djk
from DISClib.ADT import queue as q


class grafo():
    '''
    Clase que representa una Grafo

    Por facilidad del uso de esta clase en el Proyecto, todos los valores de los nodos se
    tomarán como Strings. Pero se puede poder user la implementación con cualquier tipo
    de dato 

    '''

    def __init__(self, type='Undirected'):
        '''
        Inicializacion del grafo. Crea una grafo vacio del tipo especificado

        Args:
            type: Directed o Undirected
        Returns:
            -

        '''
        if type == 'Directed':
            self.estructura = g.newGraph(size=10, directed=True)
        else:
            self.estructura = g.newGraph(size=10)

    def addNode_byValue(self, infoNodo):
        '''
        Añade un nodo al grafo dado su valor, el nodo se añade al grafo.
        Si el nodo ya existe no se añade

        Args:
            infoNodo: Información del nodo para añadir a la lista

        Returns:
            -

        '''
        infoNodo = str(infoNodo)
        if not g.containsVertex(self.estructura, infoNodo):
            self.estructura = g.insertVertex(self.estructura, infoNodo)

    def addEdge_byValue(self, infoNodo_1, infoNodo_2, weight=0):
        '''
        Añade un arco al grafo dado valor del nodo origen, nodo destino y peso.
        El arco se añade al grafo.

        Args:
            infoNodo_1: Información del nodo origen
            infoNodo_2: Información del nodo destino

        Returns:
            -

        Raises:
            Exception si alguno de los nodos no pertenece al grafo
        '''
        infoNodo_1 = str(infoNodo_1)
        infoNodo_2 = str(infoNodo_2)
        self.estructura = g.addEdge(
            self.estructura, infoNodo_1, infoNodo_2, weight)

    def deleteNode_byValue(self, infoNodo):
        '''
        Elimina un nodo del grafo dado valor.

        Args:
            infoNodo: Información del nodo que se va a eliminar

        Returns:
            -

        '''
        infoNodo = str(infoNodo)
        self.estructura = g.removeVertex(self.estructura, infoNodo)

    def getEdgeValues(self):
        '''
        Devuelve los valores de todos los arcos del grafo

        Args:
            -

        Returns:
            Lista (python) de tuplas de la forma (nodo_origen, nodo_destino, peso)

        '''
        lst = list()
        iter = lt.iterator(g.edges(self.estructura))
        aux = ()
        for i in iter:
            aux = (i['vertexA'], i['vertexB'], i['weight'])
            lst.append(aux)
        return lst

    def getNodeValues(self):
        '''
        Devuelve los valores de todos los nodos del grafo

        Args:
            -

        Returns:
            Lista (python) de los valores de los nodos del grafo

        '''
        lst = list()
        iter = lt.iterator(g.vertices(self.estructura))
        for i in iter:
            lst.append(i)
        return lst

    def isNodeValue(self, infoNodo):
        '''
        Informa si un nodo pertenece o no al grafo

        Args:
            infoNodo: Valor del nodo que se busca

        Returns:
            True si el nodo pertenece al grafo, False si no pertenece

        '''
        infoNodo = str(infoNodo)
        return g.containsVertex(self.estructura, infoNodo)

    def findAdjacentNode(self, infoNodo):
        '''
        Devuelve los valores de los nodos que son adyacentes al nodo del valor dado

        Args:
            infoNodo: Valor del nodo del que se buscan los adyacentes

        Returns:
            Lista (python) con los valores de los nodos adyacentes al nodo dado. Si no tiene adyacentes se retorna una lista vacia

        '''
        return []

    def algorithms(self, algoritmo, infoNodo=None):
        '''
        Función que ejecuta un algoritmo dado en el grafo

        Args:
            algoritmo: Nombre del algoritmo que se va a ejecutar: Bellman-Ford, BreadhtFirstSearch, DirectedCycle,  
            DepthFirstSearch, DepthFirstOrder, PrimMST, KosarajuSCC, Dijkstra

        Returns:
            Dependiendo del algoritmo:
                DepthFirstSearch, BreadhtFirstSearch, DepthFirstOrder': retornan una lista (python) de los valores de los nodos

                DirectedCycle: retorna una lista (python) con tuplas de arcos de la forma (nodo_origen, nodo_destino)

                Dijkstra, Bellman-Ford: retorna una lista de diccionarios (python) con keys: node, path, cost
                    - node: valor del nodo
                    - cost: costo de ir del nodo infoNodo a node
                    - path: lista (python) de tuplas de arcos de la forma (nodo_origen, nodo_destino) que indican el camino para ir de infoNodo a node

                KosarajuSCC: retorna un diccionario donde cada llave indica una componente fuertemente conectada, y cada valor es una lista (python) de los
                    valores de los nodos que pertenecen a dicha componente

                PrimMST: retorna una tupla (edges, weight) donde edges es una lista (python) de arcos en forma tuplas (nodo_origen, nodo_destino)
                        y weight es el costo total de los arcos mencionados

        '''
        if infoNodo != None:
            infoNodo = str(infoNodo)
        table = list()
        if algoritmo == 'Bellman-Ford':
            search = bf.BellmanFord(self.estructura, infoNodo)
            for i in self.getNodeValues():
                costo = bf.distTo(search, i)
                path = list()
                if bf.hasPathTo(search, i):
                    iter = lt.iterator(bf.pathTo(search, i))
                    for j in iter:
                        path.append((j['vertexA'], j['vertexB']))
                else:
                    costo = 'inf'
                my_dict = {'node': i, 'cost': costo, 'path': path}
                table.append(my_dict)

        if algoritmo == 'BreadhtFirstSearch':
            search = bfs.BreadhtFisrtSearch(self.estructura, infoNodo)
            for i in self.getNodeValues():
                if bfs.hasPathTo(search, i):
                    table.append(i)

        if algoritmo == "DirectedCycle":
            search = c.DirectedCycle(self.estructura)
            if c.hasCycle(search):
                pathRta = c.cycle(search)
                while not stack.isEmpty(pathRta):
                    edge = stack.pop(pathRta)
                    table.append((edge['vertexA'], edge['vertexB']))

        if algoritmo == 'DepthFirstSearch':
            search = dfs.DepthFirstSearch(self.estructura, infoNodo)
            for i in self.getNodeValues():
                if dfs.hasPathTo(search, i):
                    table.append(i)

        if algoritmo == 'DepthFirstOrder':
            search = dfo.DepthFirstOrder(self.estructura)
            while not stack.isEmpty(search['reversepost']):
                top = stack.pop(search['reversepost'])
                table.append(top)

        if algoritmo == 'PrimMST':
            search = prim.PrimMST(self.estructura, infoNodo)
            weight = prim.weightMST(self.estructura, search)
            path = search['mst']
            while not q.isEmpty(path):
                edge = q.dequeue(path)
                table.append((edge['vertexA'], edge['vertexB']))
            return table, weight

        if algoritmo == 'KosarajuSCC':
            sc = scc.KosarajuSCC(self.estructura)
            elements = sc['idscc']['table']['elements']
            table = dict()
            for i in elements:
                if i['value'] != None:
                    try:
                        lista = table[i['value']]
                        lista.append(i['key'])
                        table[i['value']] = lista
                    except:
                        table[i['value']] = [i['key']]

        if algoritmo == 'Dijkstra':
            search = djk.Dijkstra(self.estructura, str(3))
            for i in self.getNodeValues():
                if djk.hasPathTo(search, i):
                    path = djk.pathTo(search, i)
                    aux = dict()
                    pathList = list()
                    while not stack.isEmpty(path):
                        edge = stack.pop(path)
                        pathList.append((edge['vertexA'], edge['vertexB']))
                    aux['node'] = i
                    aux['path'] = pathList
                    aux['cost'] = djk.distTo(search, i)
                    table.append(aux)
        return table
