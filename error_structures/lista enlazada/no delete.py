import config
from DISClib.ADT import list as lt

class listaEnlazada():
    '''
    Clase que representa una Lista Enlazada
    '''
    def __init__(self, type):
        '''
        Inicializacion de la lista enlazada. Crea una lista enlazada vacia del tipo especificado
        
        Args:
            type: 1 si la lista es sencilla, 2 si la lista es doble

        Returns:
            -
            
        '''
        self.type =1
        if type == 1: 
            self.estructura = lt.newList(datastructure='SINGLE_LINKED', cmpfunction=defaultfunction)
        elif type == 2:
            self.estructura = lt.newList(datastructure='DOUBLE_LINKED', cmpfunction=defaultfunction)
    
    def addNode_byValue(self, infoNodo):
        '''
        Añade un nodo a la lista enlazada, el nodo se añade al final de la lista.
        Si el nodo ya se encuentra en la lista, se añade una nueva instancia
        
        Args:
            infoNodo: Información del nodo para añadir a la lista
        
        Returns:
            -
            
        '''
        lt.addLast(self.estructura, infoNodo)
    
    def deleteNode_byValue(self, infoNodo):
        '''
        Elimina un nodo de la lista enlazada.
            Si el nodo no existe se retorna False
            
            Si hay mas de un nodo con el valor indicado, solo se elimina una instancia.
        
        Args:
            infoNodo: Información del nodo que se va a eliminar
        
        Returns:
            False si el nodo no pertenece a la lista, True si el nodo se elimina de la lista
            
        '''
        return False
    
    def getNodeValues(self):
        '''
        Da todos los elementos de la lista en el orden que se tienen, iniciando por el primero
        
        Args:
            -
        
        Returns:
            Lista (python) con todos los valores de los nodos, en el orden del primero al ultimo

        '''
        lst = list()
        iter = lt.iterator(self.estructura)
        for i in iter:
            lst.append(i)
        return lst
    
    def isNodeValue(self, infoNodo):
        '''
        Informa si un nodo pertenece o no a la lista enlazada
        
        Args:
            infoNodo: Valor del nodo que se busca
        
        Returns:
            True si el nodo pertenece a la lista enlazada, False si no pertenece
            
        '''
        if lt.isPresent(self.estructura, infoNodo) != 0:
            return True
        else:
            return False
    
    def findAdjacentNode(self, infoNodo):
        '''
        Devuelve los valores de los nodos que son adyacentes a un nodo dado. En el caso de la lista enlazada sencilla, 
        el adyacente de un nodo es el siguiente, y en el caso de una lista enlazada doble, los adyacentes son
        el siguiente y el anterior
        
        Args:
            infoNodo: Información del nodo del que se buscan los adyacentes
        
        Returns:
            Lista (python) con los valores de los nodos adyacentes al nodo dado. Si no tiene adyacentes se retorna una lista vacia
            
        '''
        lst = list()
        pos = lt.isPresent(self.estructura, infoNodo)
        size = lt.size(self.estructura)
        if pos > 0:
            if self.type == 2 and pos-1 > 0:
                lst.append(lt.getElement(self.estructura, pos-1))
            if pos+1 <= size:
                lst.append(lt.getElement(self.estructura, pos+1))
        return lst

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