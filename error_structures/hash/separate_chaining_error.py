import config
from DISClib.DataStructures import chaininghashtable as lt

class SeparateChaining():
    '''
    Clase que representa una tabla hash linear probing
    '''
    def __init__(self):
        '''
        Inicializacion de la tabla hash linear probing. Crea una tabla hash linear probing vacia

        Returns:
            -
            
        '''

        self.estructura = lt.newMap(1, 109345121, 1.0 , self.compareFunc , None)
    
    def compareFunc(self, element, info):

        key = info["key"]
        if(element == key):
            return 0
        elif(element>key):
            return 1
        return -1

    def addNode_byValue(self, key, value):
        '''
        Añade un nodo a la tabla hash linear probing, el nodo se añade al final de la lista.
        Si el nodo ya se encuentra en la lista, se añade una nueva instancia
        
        Args:
            infoNodo: Información del nodo para añadir a la lista
        
        Returns:
            -
            
        '''

        self.estructura = lt.put(self.estructura, key, value)
        self.estructura = lt.put(self.estructura, int(key + 1), value)
    
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

        self.estructura = lt.remove(self.estructura, int(key-1))
    
    def getNodeValues(self):
        '''
        Da todos los elementos de la tabla de hash en el orden que se tienen
        
        Args:
            -
        
        Returns:
            Lista (python) con todos los valores de los nodos, en el orden del primero al ultimo

        '''

        tabla = self.estructura["table"]["elements"]
        resp = []
        for elem in tabla:
            actual = elem["first"]
            
            conc = ""

            while actual != None:
                conc += str(actual["info"]["key"]) + '\\n'
                actual = actual["next"]
            
            resp.append(conc)

        return resp
    
    def isNodeValue(self, key):
        '''
        Informa si un nodo pertenece o no a la tabla hash linear probing
        
        Args:
            infoNodo: Valor del nodo que se busca
        
        Returns:
            True si el nodo pertenece a la tabla de hash, False si no pertenece
            
        '''

        return lt.contains(self.estructura, key)