import config
from DISClib.DataStructures import probehashtable as lp


class LinearProbing():
    '''
    Clase que representa una tabla hash linear probing
    '''

    def __init__(self, numelements=3):
        '''
        Inicializacion de la tabla hash linear probing. Crea una tabla hash linear probing vacia

        Returns:
            -

        '''
        self.estructura = lp.newMap(numelements, 109345121, 0.7, self.compareFunc, None)

    def compareFunc(self, element, info):
        key = info["key"]
        if(element == key):
            return 0
        elif(element>key):
            return 1
        return -1

    def size(self):
        '''
        NEW Function
        Retorna el tamaNo (numero de tuplas) de la tabla hash
        Returns:
            TamaNo (numero de tuplas) de la tabla hash
        '''
        return lp.size(self.estructura)

    def capacity(self):
        '''
        NEW Function
        Retorna la capacidad de la tabla hash
        Returns:
            Capacidad de la tabla hash
        '''
        return lp.capacity(self.estructura)
    

    '''
    def hash_function(self, key):
        return hash(key) % self.size
    '''
    
    def addNode_byValue(self, key, value):
        '''
        Si la key No existe, agregar una tupla (key, value) a la tabla hash LP en una posicion disponible
        Si la key Ya existe, se reemplaza el value asociado a la key

        Args:
            key: llave
            value: valor

        Returns:
            -

        '''

        self.estructura = lp.put(self.estructura, key, value)

    def addNode_byPosition(self, key, value, pos):
        '''
        NEW FUNCTION
        Agregar una tupla (key, value) a la tabla hash LP en una posicion dada

        Args:
            key: llave
            value: valor
            pos: posicion donde debe quedar la tupla (key, value). 1 <= pos <= lp.capacity()

        Returns:
            -

        '''
        self.estructura = lp.putByPosition(self.estructura, key, value, pos)
        # Caso Especial
        # self.estructura = lp.putByPosition(self.estructura, '__EMPTY__', '__EMPTY__', pos)

    def deleteNode_byValue(self, key):
        '''
        Elimina una tupla (key, value) de la tabla hash linear probing.
        Si la key existe y se puede eliminar se retorna True. 
        Si la key NO existe, No se puede eliminar y se retorna False


        Args:
            key: llave a eliminar

        Returns:
           True si la key se encontro y se elimino, False si la key NO se encontro.
        '''
        if lp.contains(self.estructura, key):
            self.estructura = lp.remove(self.estructura, key)
            return True
        else:
            return False

    def getNodeValues(self):
        '''
        Retornar todos los valores que aparecen como key en la tabla de hash en el orden que se tienen (incluye valores None y '__EMPTY__')

        Args:
            -

        Returns:
            Lista (python) con todas las llaves de la tabla hash, en el orden de aparicion

        '''

        tabla = self.estructura["table"]["elements"]

        resp = list()
        for elem in tabla:
            resp.append(elem["key"])

        return resp

    def getNodeValuesVal(self):
        '''
        Retornar solo valores validos que aparecen como key de la tabla de hash en el orden que se tienen (NO incluye valores None y '__EMPTY__')

        Args:
            -

        Returns:
            Lista (python) con todos los valores de los nodos, en el orden de aparicion

        '''

        tabla = self.estructura["table"]["elements"]
       # print(tabla)
        resp = list()
        for elem in tabla:
            if elem["key"] != "None" and elem["key"] != None and elem["key"] != "__EMPTY__":
                resp.append(elem["key"])

        return resp

    def isNodeValue(self, key):
        '''
        Informa si una llave pertenece o no a la tabla hash LP

        Args:
            key: llave que se busca

        Returns:
            True si la llave pertenece a la tabla de hash, False si no pertenece

        '''

        return lp.contains(self.estructura, key)
