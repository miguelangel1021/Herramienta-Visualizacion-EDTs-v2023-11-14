import math
import config

class LinearProbing():
    '''
    Clase que representa una Tabla Hash Linear Probing.
    '''

    def __init__(self, numelements=3):
        '''
        Inicializacion de la tabla hash linear probing. Crea una tabla hash linear probing vacia

        Returns:
            -

        '''
        '''
        Modelo de datos de la Estructura de Datos tabla hash linear probing:
        self.estructura = {'keys', 'values', 'm', 'n', 'currentfactor', 'limitfactor'}
        self.estructura['keys'] arreglo que almacena las llaves.
        Cada key self.estructura['keys'][i] puede tener 3 valores: 
            None (posicion disponible y nunca ha sido ocupada)
            'EMPTY' (posicion disponible pero ocupada en algun momento), 
            una llave valida (posicion No disponible).
        self.estructura['values'] arreglo que almacena los valores correspondientes a las llaves
        self.estructura['m'] tamaño de la tabla
        self.estructura['n'] numero de tuplas (key, value) presentes en los arreglos
        self.estructura['currentfactor'] factor de carga actual
        self.estructura['currentfactor'] se calcula como self.estructura['n'] / self.estructura['m']
        self.estructura['limitfactor'] factor de carga maximo permitido
        '''
        maxfactor = 0.7
        capacidad = self.nextPrime(numelements//maxfactor)     # calculo de la capacidad de la tabla segun el factor de carga
        self.estructura = {'keys': [], 'values': [], 'm': capacidad, 'n': 0, 'currentfactor': 0.0, 'limitfactor':maxfactor}
        for i in range(capacidad):
            self.estructura['keys'].append(None)    # posicion inicialmente disponible y nunca ha sido ocupada
            self.estructura['values'].append(None)


    def size(self):
        '''
        NEW Function
        Retorna el tamaNo (numero de tuplas) de la tabla hash
        Returns:
            TamaNo (numero de tuplas) de la tabla hash
        '''
        return self.estructura['n']
    
    def capacity(self):
        '''
        NEW Function
        Retorna la capacidad de la tabla hash
        Returns:
            Capacidad de la tabla hash
        '''
        return self.estructura['m']
        
    def addNode_byValue(self, key, value):
        '''
        Si la key No existe, agregar una tupla (key, value) a la tabla hash LP en una posicion disponible
        Si la key Ya existe, se reemplaza el value asociado a la key
        Nota: Si se agrega la nueva tupla, hay que actualizar el factor de carga self.estructura['currentfactor']

        Args:
            key: llave a agregar
            value: valor asociado a la llave

        Returns:
            -

        '''
        h = self.hashValue(key)
        if self.estructura['keys'][h] is None:   #posicion disponible y Nunca ha sido ocupada
            self.estructura['keys'][h] = key
            self.estructura['values'][h] = value
            self.estructura['n'] += 1
            self.estructura['currentfactor'] = self.estructura['n'] / self.estructura['m']
        elif self.estructura['keys'][h] == 'EMPTY':   #posicion disponible pero ocupada en algun momento
            #TODO completar el caso.
            # Es posible que key aparezca mas adelante, se encuentre 'EMPTY' o se encuentra None (caso en el que No aparece key)
            pass
        elif self.estructura['keys'][h] == key:   #posicion ocupada por la misma llave que se quiere agregar
            #TODO completar el caso. Se mantiene el valor de key pero se reemplaza el value en la misma posicion de la key
            pass
        else:  #posicion ocupada por una llave diferente a la que se quiere agregar
            #TODO completar el caso.
            # Es posible que key aparezca mas adelante, se encuentre 'EMPTY' o se encuentra None (caso en el que No aparece key)
            pass

        if self.estructura['currentfactor'] >= self.estructura['limitfactor']: 
            # se excede el factor de carga limite
            self.rehash()


    def hashValue(self, key):
        '''
        Transformacion de la key en una posicion al interior de la tabla de hash
        '''
        h = hash(int(key))
        i = abs(h) % self.estructura['m']
        return i

    def deleteNode_byValue(self, key):
        '''
        Elimina una tupla (key, value) de la tabla hash linear probing.
        Si la key existe y se puede eliminar se retorna True. 
        Si la key NO existe, No se puede eliminar y se retorna False
        Nota: Si se elimina la tupla, hay que actualizar el factor de carga self.estructura['currentfactor']

        Args:
            key: llave a eliminar

        Returns:
           True si la key se encontro y se elimino, False si la key NO se encontro.

        '''
        h = self.hashValue(key)
        if self.estructura['keys'][h] is None:   #posicion disponible y Nunca ha sido ocupada
            return False
        elif self.estructura['keys'][h] == 'EMPTY':   #posicion disponible pero ocupada en algun momento
            #TODO completar el caso (la llave puede estar mas adelante, incluye el valor de return)
            return True
        elif self.estructura['keys'][h] == key:  # key encontrada
            self.estructura['keys'][h] = 'EMPTY'
            self.estructura['values'][h] = 'EMPTY'
            self.estructura['n'] -= 1
            self.estructura['currentfactor'] = self.estructura['n'] / self.estructura['m']
            return True
        else: #posicion ocupada por una llave diferente a la que se quiere eliminar
            #TODO completar el caso (la llave puede estar mas adelante)
            return True
    
    def getNodeValues(self):
        '''
        Da todas las llaves de la tabla de hash en el orden que se tienen

        Args:
            -

        Returns:
            Lista (python) con todas las llaves de la tabla hash, en el orden de aparicion

        '''
        resp = []
        for key in self.estructura['keys']:
            resp.append(key)

        return resp

    def getNodeValuesVal(self):
        '''
        Retornar solo valores validos que aparecen como key de la tabla de hash en el orden que se tienen (NO incluye valores None ni 'EMPTY')

        Args:
            -

        Returns:
            Lista (python) con todos los valores de la tabla hash, en el orden de aparicion

        '''
        resp = []
        for key in self.estructura['keys']:
            if key != None and key != 'EMPTY':
                resp.append(key)

        return resp

    def isNodeValue(self, key):
        '''
        Informa si una llave pertenece o no a la tabla hash LP

        Args:
            key: llave que se busca

        Returns:
            True si la llave pertenece a la tabla de hash, False si no pertenece

        '''
        h = self.hashValue(key)
        if self.estructura['keys'][h] is None:  #posicion disponible y Nunca ha sido ocupada
            return False
        elif self.estructura['keys'][h] == 'EMPTY':   #posicion disponible pero ocupada en algun momento
            #TODO completar el caso (la llave puede estar mas adelante)
            return False
        elif self.estructura['keys'][h] == key:  # la key esta en la posicion calculada por hashValue
            return True
        else:  #posicion ocupada por una llave diferente a la que se busca
            #TODO completar el caso (la llave puede estar mas adelante)
            return False

    def rehash(self):
        '''
        Aplicar el rehash a la tabla definida en self.estructura
        El nuevo tamaño es el proximo primo mayor al doble de la tabla original
        Reubicar las tuplas [key, value] de la tabla original en la nueva tabla 
        El contenido de la nueva tabla debe quedar en self.estructura

        Returns:
            -
        '''
        m_nuevo = 2*self.estructura['limitfactor']*self.estructura['m']
        nueva_tabla = LinearProbing(numelements=m_nuevo)
        #TODO completar (reubicar las tuplas (key, value) que estan en la tabla original self.estructura a la nueva_tabla
        

        #TODO pasar las tupla (key, value) de la tabla.estructura a self.estructura
        self.estructura = nueva_tabla.estructura

    
    # Function that returns True if n
    # is prime else returns False
    # This code is contributed by Sanjit_Prasad
    def isPrime(self, n):
        # Corner cases
        if(n <= 1):
            return False
        if(n <= 3):
            return True

        if(n % 2 == 0 or n % 3 == 0):
            return False

        for i in range(5, int(math.sqrt(n) + 1), 6):
            if(n % i == 0 or n % (i + 2) == 0):
                return False

        return True
    
    # Function to return the smallest
    # prime number greater than N
    # # This code is contributed by Sanjit_Prasad
    def nextPrime(self, N):
        # Base case
        if (N <= 1):
            return 2
        prime = int(N)
        found = False
        # Loop continuously until isPrime returns
        # True for a number greater than n
        while(not found):
            prime = prime + 1
            if(self.isPrime(prime) is True):
                found = True
        return int(prime)
