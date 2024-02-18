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
        self.type = type
        if type == 1:
            self.estructura = lt.newList(
                datastructure='SINGLE_LINKED', cmpfunction=defaultfunction) 
        elif type == 2:
            self.estructura = lt.newList(
                datastructure='DOUBLE_LINKED', cmpfunction=defaultfunction)

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

    def addNode_byValueFirst(self, infoNodo):
        '''
        Añade un nodo a la lista enlazada, el nodo se añade al final de la lista.
        Si el nodo ya se encuentra en la lista, se añade una nueva instancia

        Args:
            infoNodo: Información del nodo para añadir a la lista

        Returns:
            -

        '''
        lt.addFirst(self.estructura, infoNodo)

    def deleteNode_byValue(self, infoNodo):
        '''
        Elimina un nodo de la lista enlazada.
            Si el nodo no existe (No se puede eliminar) se retorna False
            Si el nodo existe (se puede eliminar) y se elimina se retorna True

            Si hay mas de un nodo con el valor indicado, solo se elimina una instancia.

        Args:
            infoNodo: Información del nodo que se va a eliminar

        Returns:
            True si el elemento aparece en la lista y se elimina
            False si el elemento no pertenece a la lista y No se puede eliminar

        '''
        pos = -1
        items = self.getNodeValues()
        for i in range(len(items)):
            if defaultfunction(items[i], infoNodo) == 0:
                pos = i
                break
        if pos != -1:
            pos = pos + 1
            lt.deleteElement(self.estructura, pos)  # CORRECCION Agregar
            return True
        else:
            return False


        # if pos > 1:
        #     lt.deleteElement(self.estructura, pos)
        #     return True
        # elif pos == 1:
        #     lt.removeFirst(self.estructura)
        #     return True
        # else:
        #     return False

    def getNodeValues(self):
        '''
        Da todos los elementos de la lista en el orden que se tienen, iniciando por el primero

        Args:
            -

        Returns:
            Lista (python) con todos los valores de los nodos, en el orden del primero al ultimo

        '''
        lst = list()  
        actual = self.estructura['first']            # CORRECCION cambio de implementacion
        
        while actual is not None:
            lst.append(actual['info'])
            actual = actual['next']

        return lst

    def getNodeValuesReverse(self):
        '''
        Funcion solo aplica para listas doblemente enlazadas
        Retorna todos los elementos de la lista en el orden del ultimo al primero

        Args:
            -

        Returns:
            Lista (python) con todos los valores de los nodos, en el orden del ultimo al primero

        '''
        lst = list()
        actual = self.estructura['last']
        
        while actual is not None:
            lst.append(actual['info'])
            actual = actual['prev']

        return lst

    def isNodeValue(self, infoNodo):
        '''
        Informa si un nodo pertenece o no a la lista enlazada

        Args:
            infoNodo: Valor del nodo que se busca

        Returns:
            True si el nodo pertenece a la lista enlazada, False si no pertenece

        '''
        pos = -1
        items = self.getNodeValues()
        for i in range(len(items)):
            if defaultfunction(items[i], infoNodo) == 0:
                pos = i
                break
        if pos != -1:
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
        '''
        pos = -1
        items = self.getNodeValues()
        for i in range(len(items)):
            if defaultfunction(items[i], infoNodo) == 0:
                pos = i
                break

        if pos != -1:
            pos = pos + 1

            size = lt.size(self.estructura)
            if self.type == 2 and pos-1 > 0:   # CORRECCION Modificar
            #    if self.type == 2 and pos-1 > 0:   # CORRECCION Borrar
                lst.append(lt.getElement(self.estructura, pos-1))
            if pos+1 <= size:
                lst.append(lt.getElement(self.estructura, pos+1))
        '''

        previous = None
        actual = self.estructura['first']            # CORRECCION cambio de implementacion
        encontro = False

        while not encontro and actual is not None:
            if defaultfunction(actual['info'], infoNodo ) != 0:
                previous = actual
                actual = actual['next']
            else:
                encontro = True
        
        if encontro:
            if self.type == 2 and previous is not None:
                lst.append(previous['info'])
            if actual['next'] is not None:
                lst.append(actual['next']['info'])

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
