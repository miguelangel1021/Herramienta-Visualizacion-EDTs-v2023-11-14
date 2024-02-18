import config


class Arreglo():
    '''
    Clase que representa un arreglo
    '''

    def __init__(self):
        '''
        Inicializacion del arreglo. Crea un arreglo vacio

        Returns:
            -

        '''
        self.estructura = list()
        self.type = 5

    def addNode_byValue(self, infoElemento):
        '''
        Añade un elemento al arreglo, el elemento se añade al final de la lista.
        Si el elemento ya se encuentra en la lista, se añade una nueva instancia

        Args:
            infoElemento: Información del elemento para añadir a la lista

        Returns:
            -

        '''
        self.estructura.append(infoElemento)

    def addNode_byValueFirst(self, infoElemento):
        '''
        Añade un elemento al arreglo, el elemento se añade al final de la lista.
        Si el elemento ya se encuentra en la lista, se añade una nueva instancia

        Args:
            infoElemento: Información del elemento para añadir al arreglo

        Returns:
            -

        '''
        self.estructura.insert(0, infoElemento)

    def deleteNode_byValue(self, infoElemento):
        '''
        Elimina un elemento al arreglo.
            Si el elemento no existe se retorna False

            Si hay mas de un elemento con el valor indicado, solo se elimina una instancia.

        Args:
            infoElemento: Información del elemento que se va a eliminar

        Returns:
            False si el elemento no pertenece al arreglo, True si el elemento aparece en el arreglo

        '''
        for i in range(len(self.estructura)):
            if self.estructura[i] == infoElemento:
                del self.estructura[i]
                return True

        return False

    def getNodeValues(self):
        '''
        Da todos los elementos de la lista en el orden que se tienen

        Args:
            -

        Returns:
            Lista (python) con todos los valores de los elementos, en el orden del primero al ultimo

        '''
        lst = list()
        for i in self.estructura:
            lst.append(i)
        return lst

    def isNodeValue(self, infoElemento):
        '''
        Informa si un elemento pertenece o no al arreglo

        Args:
            infoElemento: Valor del elemento que se busca

        Returns:
            True si el elemento pertenece a la lista enlazada, False si no pertenece

        '''
        for elem in self.estructura:
            if elem == infoElemento:
                return True

        return False
    
    def findAdjacentNode(self, infoElemento):
        '''
        Devuelve los valores de los elementos que son adyacentes a un elemento dado.
        
        Args:
            infoElemento: Información del elemento del que se buscan los adyacentes
        
        Returns:
            Lista (python) con los valores de los elementos adyacentes al elemento dado. Si no tiene adyacentes se retorna una lista vacia
            
        '''
        lst = list()

        for i in range(len(self.estructura)):
            if self.estructura[i] == infoElemento:
                if i != 0:
                    lst.append(self.estructura[i-1])
                if i != len(self.estructura)-1:
                    lst.append(self.estructura[i+1])
                break
        return lst

 