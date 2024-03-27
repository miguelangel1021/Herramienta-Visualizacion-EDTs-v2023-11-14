from DISClib.ADT import orderedmap as omap
from DISClib.ADT import list as lt
from DISClib.Algorithms.Trees import traversal as tr

from graphviz import Digraph

import random
import string


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


class RBT():
    '''
    Clase que representa un arbol RBT
    '''

    def __init__(self):
        '''
        Inicializacion del arbol BST. Crea un arbol BST vacio con la funcion de comparacion por
        defecto especificada en este archivo 

        Args:
            -

        Returns:
            -

        '''
        self.estructura = omap.newMap(omaptype='RBT', comparefunction=defaultfunction)

    def addNode_byValue(self, infoNodo):
        '''
        Añade un nodo al arbol, el nodo se añade en la posicion correcta de acuerdo al orden 
        del RBT. Si el nodo ya pertence al arbol, no se añade

        Args:
            infoNodo: Información del nodo para añadir al RBT

        Returns:
            -

        '''
        self.estructura = omap.put(self.estructura, infoNodo, infoNodo)

    def addNode_byPosition(self, infoNodo, color):
        '''
        Añade un nodo al arbol, el nodo se añade en la posicion correcta (NO requiere balanceo).
        El nodo llega con el color apropiado en el RBT. 
        Si el nodo ya pertence al arbol, no se añade

        Args:
            infoNodo: Información del nodo para añadir al RBT
            color: Color del nodo en el RBT
        Returns:
            -

        '''
        self.estructura = omap.put_by_position(self.estructura, infoNodo, infoNodo, color)

    def deleteNode_byValue(self, infoNodo):
        '''
        Elimina un nodo del arbol, el nodo se elimina del arbol y se reacomodan los vertices de ser necesario

        Args:
            infoNodo: Información del nodo que se elimina del arbol

        Returns:
            True si el nodo se elimina del arbol. False si el nodo no existe o no se eliminó del arbol

        '''
        exists = omap.contains(self.estructura, infoNodo)
        print(exists)
        if exists == False:
            return False
        else:
            self.estructura = omap.remove(self.estructura, infoNodo)
            return True

    def getNodeValues(self, order='Preorder'):
        '''
        Se listan todos las llaves del RBT en un orden especifico

        Args:
            order: orden en el que se listan los nodos (Preorder, Inorder, Postorder, Preorder_with_color)

        Returns:
            Lista (python) con todos los valores del arbol en el orden indicado

        '''
        #print('Archivo Ref')

        lst = list()
        try:
            if not omap.isEmpty(self.estructura):
                if order == 'Inorder':
                    iter = lt.iterator(tr.inorder(self.estructura))
                elif order == 'Preorder':
                    iter = lt.iterator(tr.preorder(self.estructura))
                elif order == 'Postorder':
                    iter = lt.iterator(tr.postorder(self.estructura))
                elif order == 'Preorder_with_color': # NEW traversal
                    iter = lt.iterator(tr.preorder_with_color(self.estructura))
                for i in iter:
                    lst.append(i)
            return lst
        except Exception as e:
            print(e)

    def isNodeValue(self, infoNodo):
        '''
        Informa si un nodo pertenece o no al arbol

        Args:
            infoNodo: Valor del nodo que se busca

        Returns:
            True si el nodo pertenece al arbol, False si no pertenece

        '''
        return omap.contains(self.estructura, infoNodo)

    def findAdjacentNode(self, infoNodo):
        '''
        Devuelve los valores de los nodos que son adyacentes a un nodo dado. Los nodos adyacentes
        son los que se alcanzan con las conexiones de izquierda y derecha

        Args:
            infoNodo: Información del nodo del que se buscan los adyacentes

        Returns:
            Existe o no el nodo de busqueda
            Lista (python) con los valores de los nodos adyacentes al nodo dado. Si no tiene adyacentes se retorna una lista vacia

        '''

        node = omap.get(self.estructura, infoNodo)
        lst = list()
        existe = node != None
        if existe:
            left = node['left']
            if left != None:
                lst.append(left['key'])
            right = node['right']
            if right != None:
                lst.append(right['key'])
        return existe, lst
    
    def size(self):
        
        return omap.size(self.estructura)
    
    def height(self):

        return omap.height(self.estructura)
    
    def minKey(self):

        return omap.minKey(self.estructura)
