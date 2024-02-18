import config

class bst():
    '''
    Clase que representa un arbol BST 
    '''

    def __init__(self, key=None, value=None):
        '''
        Inicializacion de un arbol BST con su nodo raiz.
        Todo nodo tiene la siguiente estructura:
            self.estructura = {'key', 'value', 'left', 'right'}
        donde
            self.estructura['key']: llave del nodo
            self.estructura['value']: valor/informacion del nodo
            self.estructura['left']: raiz del sub-arbol de la izquierda (elementos menores)
            self.estructura['right']: raiz del sub-arbol de la derecha (elementos mayores)
        Caso Especial:
            Permite crear la raiz de un arbol vacio. En este caso el valor de self.estructura['key'] debe ser None.

        Args:
            key: key del nodo
            value: value del nodo

        Returns:
            -

        Posibles usos:
            nodo = bst()       # crea un arbol BST vacio con un unico nodo que tiene None en nodo.estructura['key']
            nodo = bst(key, value)  # crea un arbol BST con un unico nodo con key y value
            nodo = bst(80, 80)  # crea un arbol BST con un unico nodo con llave y valor 80
        '''
        self.estructura = {'key': key, 'value': value, 'left': None, 'right': None}

    def size(self):
        '''
        NEW FUNCTION
        Calcular el peso (size) de un BST
        El peso se define como el total de nodos (llaves) que tiene un BST
        Caso Especial: Si el arbol esta vacio, su peso (size) es 0

        Returns:
            El peso (size) de un BST
        '''
        # Solucion RECURSIVA
        # Funcion de ejemplo donde se aplica RECURSION
        if self.estructura['key'] is None: # caso Especial
            return 0
        size_left = 0
        if self.estructura['left'] is not None: # caso Recursivo
            size_left = self.estructura['left'].size()
        size_right = 0
        if self.estructura['right'] is not None: # caso Recursivo
            size_right = self.estructura['right'].size()
        return 1 + size_left + size_right

    def height(self):
        '''
        NEW FUNCTION
        Calcular la altura (height) de un BST
        La altura se define como el numero de enlaces de la rama mas larga.
        Caso Especial: La altura de un arbol BST vacio es -1

        Returns:
            La altura (height) de un BST
        '''
        # Solucion RECURSIVA
        # Funcion de ejemplo donde se aplica RECURSION
        if self.estructura['key'] is None: # caso Especial
            return -1
        if self.estructura['left'] is None: # caso Especial
            height_left = -1
        else: # caso Recursivo
            height_left = self.estructura['left'].height()
        if self.estructura['right'] is None: # caso Especial
            height_right = -1
        else: # caso Recursivo
            height_right = self.estructura['right'].height()
        return 1 + max(height_left, height_right)

    def minKey(self):
        '''
        NEW FUNCTION
        Retorna la llave minima de un arbol BST
        La llave minima se encuentra lo mas a la izquierda posible del BST.
        Caso Especial: Si el arbol esta vacio, la llave minima es el valor None

        Returns:
            La llave minima de un sub-arbol BST
        '''
        if self.estructura['key'] is None: # Caso Especial
            return None
        #TODO Considerar los casos:
        # Caso 1: self.estructura['left'] es None (No hay sub-arbol izquierdo)
        # Caso 2: self.estructura['left'] es diferente de None (Si hay sub-arbol izquierdo)
        # Solucion RECURSIVA

        return None

    def addNode_byValue(self, key):
        '''
        Añade un nodo con una key al arbol BST. El nodo se añade en la posicion correcta de acuerdo 
        al valor de la key.
        Caso Especial:
            1. Si self.estructura['key'] es None, la nueva key debe reemplazar este valor None
            2. Si self.estructura['key'] tiene el valor de la key, NO hay que hacer nada porque la key ya existe en el arbol

        Args:
            key: la llave del nuevo nodo

        Returns:
            -

        '''
        if self.estructura['key'] is None:  #Caso Especial 1 en que la raiz esta vacia
            self.estructura['key'] = key
        #TODO Considerar los casos:
        # Caso 1: self.estructura['key'] tiene la key que se quiere agregar. NO se hace nada. Caso Especial 2.
        # Caso 2: self.estructura['key'] tiene una key mayor a la key que se quiere agregar
        # Caso 3: self.estructura['key'] tiene una key menor a la key que se quiere agregar
        # Solucion RECURSIVA


    def deleteNode_byValue(self, key):
        '''
        Elimina el nodo del arbol con el valor de la key y se reacomodan los nodos de ser necesario
        Caso Especial:
            Al eliminar el ultimo nodo de un arbol, hay que dejar el arbol vacio.
            Eso se logra colocando el valor None en self.estructura['key']

        Args:
            key: key del nodo a eliminar del arbol

        Returns:
            True si el nodo se elimina del arbol. False si el nodo no existe o no se eliminó del arbol

        '''
        if self.isNodeValue(key): # La key existe en el BST
            # Usar la funcion recursiva deleteNode_Recursive(self, key)
            raiz = self.deleteNode_Recursive(key)  #TODO completar esta función
            if raiz is None: # Caso Especial
                self.estructura['key'] = None
                self.estructura['value'] = None
                self.estructura['left'] = None
                self.estructura['right'] = None
            else:
                self.estructura = raiz.estructura
            return not self.isNodeValue(key)
        else:
            return False

    def deleteNode_Recursive(self, key):
        '''
        Elimina el nodo del arbol que tiene la key y se reacomodan los nodo de ser necesario
        Caso especial: Si la llave a eliminar tiene sus dos hijos, la llave a eliminar se reemplaza por la llave menor de sus llaves mayores

        Args:
            key: key del nodo que se elimina del arbol

        Returns:
            La raiz del arbol BST que NO contiene el nodo con key
        '''
        if self.estructura['key'] is None:  # caso raiz del arbol vacio (sin llave)
            return self
        #TODO Considerar los casos:
        # Caso 1: self.estructura['key'] tiene una key mayor a la key que se quiere eliminar
        # Caso 2: self.estructura['key'] tiene una key menor a la key que se quiere eliminar
        # Caso 3: self.estructura['key'] tiene la key que se quiere eliminar. Incluye el Caso Especial.
        # Solucion RECURSIVA
        
        return None

    def getNodeValues(self, order='Preorder'):
        '''
        Se listan todos los valores de los nodos del arbol en un orden especifico

        Args:
            order: orden en el que se listan los nodos ('Preorder', 'Inorder', 'Postorder')

        Returns:
            Lista (python) con todos los valores del arbol en el orden indicado

        '''
        lst = list()
        if self.estructura['key'] is not None: # caso raiz del arbol NO vacio
            if order == 'Preorder':
                # Definir la funcion recursiva getKeysPreorder(lst) para obtener las llaves en Preorder
                self.getKeysPreorder(lst)
            elif order == 'Inorder':
                # Definir la funcion recursiva getKeysInorder(lst) para obtener las llaves en Inorder
                self.getKeysInorder(lst)
            if order == 'Postorder':
                # Definir la funcion recursiva getKeysPreorder(lst) para obtener las llaves en Postorder
                self.getKeysPostorder(lst)
        return lst

    def getKeysPreorder(self, lst):
        '''
        Realizar el recorrido en Preorder del arbol BST.
        Las llaves del recorrido deben agregarse a la lista lst 

        Args:
            lst: lista donde quedan las llaves del arbol BST en recorrido Preorder
        '''
        #TODO Aplicar recorrido en Preorder a la raiz self.estructura
        # Solucion RECURSIVA

    def getKeysInorder(self, lst):
        '''
        Realizar el recorrido en Inorder del arbol BST.
        Las llaves del recorrido deben agregarse a la lista lst 

        Args:
            lst: lista donde quedan las llaves del arbol BST en recorrido Inorder
        '''
        #TODO Aplicar recorrido en Inorder a la raiz self.estructura
        # Solucion RECURSIVA

    def getKeysPostorder(self, lst):
        '''
        Realizar el recorrido en Postorder del arbol BST. 
        Las llaves del recorrido deben agregarse a la lista lst 

        Args:
            lst: lista donde quedan las llaves del arbol BST en recorrido Postorder
        '''
        #TODO Aplicar recorrido en Postorder a la raiz self.estructura
        # Solucion RECURSIVA

    def isNodeValue(self, key):
        '''
        Informa si una key pertenece o no al arbol

        Args:
            key: key de consulta en el arbol

        Returns:
            True si existe la key en el arbol, False si no pertenece

        '''
        if self.estructura['key'] is None: # caso raiz del arbol vacio (sin llave)
            return False
        #TODO Considerar los casos:
        # Caso 1: self.estructura['key'] tiene la key que se esta buscando. Retornar True
        # Caso 2: self.estructura['key'] tiene una key mayor a la key que se esta buscando.
        # Caso 3: self.estructura['key'] tiene una key menor a la key que se esta buscando.
        # Solucion RECURSIVA

        return False

    def findAdjacentNode(self, key):
        '''
        Devuelve las keys que son adyacentes a un nodo dado. 
        Las keys adyacentes son las keys de sus hijos self.estructura['left'] y self.estructura['right']

        Args:
            infoNodo: Información del nodo del que se buscan los adyacentes

        Returns:
            Valor True/False que corresponde si la key existe o no en el arbol
            Lista (python) con los valores de los nodos adyacentes al nodo dado (si existe).
            Si la key No existe o la Key no tiene adyacentes se retorna una lista vacia

        '''
        lst = list()
        existe = False
        if self.estructura['key'] is None: #Caso Especial en que la raiz esta vacia
            return existe, lst
        #TODO Considerar los casos:
        # Caso 1: self.estructura['key'] tiene la key que se esta buscando.
        # Revisar si tiene adyacentes hijo izquierdo (self.estructura['left']) e hijo derecho (self.estructura['right']) para agregar sus llaves a la lista lst
        # Caso 2: self.estructura['key'] tiene una key mayor a la key que se esta buscando.
        # Caso 3: self.estructura['key'] tiene una key menor a la key que se esta buscando.
        # Solucion RECURSIVA

        return existe, lst

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
