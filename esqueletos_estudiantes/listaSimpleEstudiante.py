import config

class NodoLista:
    '''
    Funciones para crear, consultar y modificar un nodo de la lista.
    Un nodo se define por los datos info (elemento) y el next (conexion al proximo nodo de la lista)
    '''
    def __init__(self, infoNodo):
        '''
        Crea un nodo de la lista con su elemento (infoNodo) y SIN conexion al nodo siguiente (next).
        Args:
            infoNodo: elemento de informacion que va contener el nodo

        Uso: Para crear/obtener un nodo nuevo, hay que usar la funcion NodoLista(elemento)
        
        Ejemplo de uso en las funciones de la Lista:
            nodo = NodoLista(5)
        '''
        self.info = infoNodo   # self.info contiene el elemento (informacion) del nodo
        self.next = None       # self.next contiene la referencia al proximo nodo

    def getInfo(self):
        '''
        Retorna el elemento del nodo self
        Args:
            -
        Ejemplo de uso en las funciones de la Lista:
            elemento = nodo.getInfo()
        '''
        return self.info

    def setInfo(self, infoNodo):
        '''
        Modifica el elemento del nodo self
        Args:
            infoNodo: elemento de informacion que va contener el nodo

        Ejemplo de uso en las funciones de la Lista:
            nodo.setInfo(10)
        '''
        self.info = infoNodo

    def getNext(self):
        '''
        Retorna la referencia al siguiente nodo del nodo self

        Ejemplo de uso en las funciones de la Lista:
            proximo = nodo.getNext()
        '''
        return self.next

    def setNext(self, nodoNext):
        '''
        Modifica la referencia al siguiente nodo del nodo self
        Args:
            referencia al nuevo nodo siguiente del nodo self

        Ejemplo de uso en las funciones de la Lista:
            nodo.setNext(nodoSiguiente)
        '''
        self.next = nodoNext

class listaEnlazada():
    '''
    Clase que representa una Lista Enlazada que inicia en el primer nodo (first).
    '''

    def __init__(self, type):
        '''
        Inicializacion de la lista enlazada. Crea una lista enlazada vacia

        Args:
            type: 1 si la lista es sencilla

        Returns:
            -

        '''
        #Modelo de datos de la Estructura de Datos Lista Enlazada
        self.type = 1
        self.estructura = {'first': None, 'last': None, 'size': 0 }  
             # self.estructura es la variable que contendra la informacion de la lista
             # inicialmente vacia
             # self.estructura se puede modificar/actualizar en cada funcion de la Estructura de Datos                                                                     
             # self.estructura['first'] es la referencia al primer nodo de la lista
             # self.estructura['last'] es la referencia al ultimo nodo de la lista
             # self.estructura['size'] tiene el numero de elementos de la lista

    def size(self):
        '''
        Retorna el numero de elementos en el arreglo
        Returns:
            Numero el numero de elementos en el arreglo
        '''
        #TODO consultar el dato self.estructura
        return 0

    def addNode_byValue(self, infoNodo):
        '''
        Añade un NUEVO nodo al FINAL lista enlazada

        Args:
            infoNodo: Información del nodo para añadir a la lista

        Returns:
            -

        '''
        #TODO actualizar el dato self.estructura
        nodo = NodoLista(infoNodo)    # creacion de un nuevo nodo usando la funcion de NodoLista

    def addNode_byValueFirst(self, infoNodo):
        '''
        Añade un NUEVO nodo al PRINCIPIO de la lista enlazada.

        Args:
            infoNodo: Información del nodo para añadir a la lista

        Returns:
            -

        '''
        #TODO actualizar el dato self.estructura
        nodo = NodoLista(infoNodo)    # creacion de un nuevo nodo usando la funcion de NodoLista

    def deleteNode_byValue(self, infoNodo):
        '''
        Elimina un nodo de la lista enlazada.
            Si hay mas de un nodo con el elemento indicado, SOLO se elimina la primera ocurrencia.

        Args:
            infoNodo: Información del nodo que se va a eliminar

        Returns:
            True si el nodo se encontro y se elimino, False si el nodo NO se encontro.

        '''
        #TODO actualizar el dato self.estructura

        return False

    def getNodeValues(self):
        '''
        Retorna una (nueva) lista Python con los elementos de la lista en el orden del primero al ultimo

        Args:
            -

        Returns:
            Lista (python) con todos los elementos de los nodos, en el orden del primero al ultimo

        '''
        #TODO consulta del dato self.estructura
        lst = list()
        
        return lst

    def isNodeValue(self, infoNodo):
        '''
        Informa si un nodo pertenece o no a la lista enlazada

        Args:
            infoNodo: Valor del nodo que se busca

        Returns:
            True si el nodo pertenece a la lista enlazada, False si no pertenece

        '''
        #TODO consultar el dato self.estructura

        return False

    def findAdjacentNode(self, infoNodo):
        '''
        Devuelve el elemento del nodo adyacente al nodo que contiene infoNodo. 
        Para la lista enlazada sencilla, el adyacente de un nodo es la informacion de su nodo siguiente (si existe)

        Args:
            infoNodo: Información del nodo al que se le busca su adyacente 

        Returns:
            Lista (python) con el elemento del nodo adyacente al nodo dado. 
            Si el elemento NO esta en la lista o Si NO tiene adyacente se retorna una lista vacia.

        '''
        #TODO consultar el dato self.estructura
        lst = list()

        return lst


def comparefunction(elem_1, elem_2):
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
    elem1C = elem_1
    elem2C = elem_2

    if type(elem_1) != type(elem_2):
        elem1C = str(elem_1)
        elem2C = str(elem_2)
    if elem1C > elem2C:
        return 1
    elif elem1C < elem2C:
        return -1
    return 0
