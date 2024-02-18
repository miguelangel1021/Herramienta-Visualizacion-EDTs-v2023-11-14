import config
from DISClib.DataStructures import chaininghashtable as sc

class SeparateChaining():
    '''
    Clase que representa una tabla hash separate chaining
    '''
    def __init__(self, numelements=5):
        '''
        Inicializacion de la tabla hash separate chaining. Crea una tabla hash separate chaining vacia

        Returns:
            -            
        '''

        self.estructura = sc.newMap(numelements, 109345121, 2.0, self.compareFunc, None)
    
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
        return sc.size(self.estructura)

    def capacity(self):
        '''
        NEW Function
        Retorna la capacidad de la tabla hash
        Returns:
            Capacidad de la tabla hash
        '''
        return sc.capacity(self.estructura)

    def addNode_byValue(self, key, value):
        '''
        Si la key No existe, agregar una tupla (key, value) a la tabla hash SC en su bucket
        Si la key Ya existe, se reemplaza el value asociado a la key
        
        Args:
            key: llave
            value: valor
        
        Returns:
            -
        '''

        self.estructura = sc.put(self.estructura, key, value)
    
    def addNode_byPosition(self, key, value, pos):
        '''
        Agregar una tupla (key, value) a la tabla hash SC en una posicion dada

        Args:
            key: llave
            value: valor
            pos: posicion donde debe quedar la tupla (key, value). 1 <= pos <= lp.capacity()

        Returns:
            -

        '''
        self.estructura = sc.putByPosition(self.estructura, key, value, pos)

    def deleteNode_byValue(self, key):
        '''
        Elimina una tupla (key, value) de la tabla hash SC.
        Si la key existe y se puede eliminar se retorna True. 
        Si la key NO existe, No se puede eliminar y se retorna False


        Args:
            key: llave a eliminar
        
        Returns:
           True si la key se encontro y se elimino, False si la key NO se encontro.
        '''

        if sc.contains(self.estructura, key):
            self.estructura = sc.remove(self.estructura, key)
            return True
        else:
            return False

    def getNodeValues(self):
        '''
        Retornar todos los valores que aparecen como key en la tabla de hash en el orden que se tienen
        
        Args:
            -
        
        Returns:
            Lista (python) con todas las llaves de la tabla de hash, en el orden de aparicion

        '''

        tabla = self.estructura["table"]["elements"]
        resp = list()
        for elem in tabla:
            actual = elem["first"]
            
            conc = ""

            while actual != None:
                conc += str(actual["info"]["key"]) + '\\n'
                actual = actual["next"]
            
            resp.append(conc)

        return resp
    
    def getNodeValuesVal(self):
        '''
        Retornar todos los valores que aparecen como key en la tabla de hash en el orden que se tienen
        
        Args:
            -
        
        Returns:
            Lista (python) con todas las llaves de la tabla de hash, en el orden de aparicion

        '''

        tabla = self.estructura["table"]["elements"]
        resp = list()
        for elem in tabla:
            actual = elem["first"]
            
            conc = ""

            while actual != None:
                conc += str(actual["info"]["key"]) + '\\n'
                resp.append(actual["info"]["key"])
                actual = actual["next"]

        return resp

    def isNodeValue(self, key):
        '''
        Informa si un nodo pertenece o no a la tabla hash SC
        
        Args:
            key: llave que se busca
        
        Returns:
            True si el nodo pertenece a la tabla de hash, False si no pertenece
            
        '''

        return sc.contains(self.estructura, key)