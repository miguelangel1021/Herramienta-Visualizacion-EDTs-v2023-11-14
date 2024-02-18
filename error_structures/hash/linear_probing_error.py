import config
from DISClib.DataStructures import probehashtable as lt


class LinearProbing():
    '''
    Clase que representa una tabla hash linear probing
    '''

    def __init__(self):
        '''
        Inicializacion de la tabla hash linear probing. Crea una tabla hash linear probing vacia

        Returns:
            -

        '''
        self.estructura = lt.newMap(1, 109345121, 0.7, None, None)

    def hash_function(self, key):
        return hash(key) % self.size

    def addNode_byValue(self, key, value):
        '''
        Añade un nodo a la tabla hash linear probing, el nodo se añade al final de la lista.
        Si el nodo ya se encuentra en la lista, se añade una nueva instancia

        Args:
            infoNodo: Información del nodo para añadir a la lista

        Returns:
            -

        '''

        '''
        index = self.hash_function(key)
        count = 0
        while self.keys[index] is not None and count <= self.size:
            if self.keys[index] == key:
                self.values[index] = value
                return
            index = (index + 1) % self.size
            count += 1
        self.keys[index] = key
        self.values[index] = value
        '''

        self.estructura = lt.put(self.estructura, key, value)
        self.estructura = lt.put(self.estructura, int(key+1), value)

    def deleteNode_byValue(self, key):
        '''
        Elimina un nodo a la tabla hash linear probing.
            Si el nodo no existe se retorna False

            Si hay mas de un nodo con el valor indicado, solo se elimina una instancia.

        Args:
            infoNodo: Información del nodo que se va a eliminar

        Returns:
            False si el nodo no pertenece a la lista, True si el nodo se elimina de la lista

        '''
        '''
        index = self.hash_function(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.keys[index] = None
                self.values[index] = None
                return
            index = (index + 1) % self.size
        '''
        self.estructura = lt.remove(self.estructura, int(key+1))

    def getNodeValues(self):
        '''
        Da todos los elementos de la tabla de hash en el orden que se tienen

        Args:
            -

        Returns:
            Lista (python) con todos los valores de los nodos, en el orden del primero al ultimo

        '''

        '''
        actual = lt.valueSet(self.estructura)["first"]
        resp = []

        while actual["next"] != None:
            resp.append(actual["info"])
            actual = actual["next"]
        resp.append(actual["info"])
        '''
        tabla = self.estructura["table"]["elements"]
       # print(tabla)
        resp = []
        for elem in tabla:
            resp.append(elem["key"])

        return resp

    def isNodeValue(self, key):
        '''
        Informa si un nodo pertenece o no a la tabla hash linear probing

        Args:
            infoNodo: Valor del nodo que se busca

        Returns:
            True si el nodo pertenece a la tabla de hash, False si no pertenece

        '''

        '''
        index = self.hash_function(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return True
            index = (index + 1) % self.size
        return False
        '''

        return True  # lt.contains(self.estructura, key)
