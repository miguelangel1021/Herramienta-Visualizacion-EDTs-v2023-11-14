import math
import config

class SeparateChaining():
    '''
    Clase que representa una Tabla Hash Separate Chaining.
    '''

    def __init__(self, numelements=5):
        '''
        Inicializacion de la tabla hash Separate Chaining. Crea una tabla hash Separate Chaining vacia

        Returns:
            -

        '''
        '''
        Modelo de datos de la Estructura de Datos tabla hash Separate Chaining:
        self.estructura = {'table', 'm', 'n', 'currentfactor', 'limitfactor'}
        self.estructura['table'] arreglo que almacena los buckets.
        Cada bucket self.estructura['table'][i] es una lista Python con las tuplas [key, value] que coinciden en la posicion i. 
        self.estructura['m'] tamaño del arreglo (capacidad)
        self.estructura['n'] numero de tuplas [key, value] presentes en los buckets
        self.estructura['currentfactor'] factor de carga actual
        self.estructura['currentfactor'] se calcula como self.estructura['n'] / self.estructura['m']
        self.estructura['limitfactor'] factor de carga maximo permitido
        '''
        maxfactor = 2.0
        capacidad = self.nextPrime(numelements//maxfactor)     # calculo de la capacidad de la tabla segun el factor de carga
        self.estructura = {'table': [], 'm': capacidad, 'n': 0, 'currentfactor': 0.0, 'limitfactor':maxfactor}
        for i in range(capacidad):
            bucket = list()     # lista para guardar las tuplas [key, value] que coinciden en una posicion de la tabla hash
            self.estructura['table'].append(bucket)   # Cada posicion de la tabla tiene su bucket (lista vacia inicialmente)


    def size(self):
        '''
        NEW Function
        Retorna el tamaNo (numero de tuplas  [key, value]) de la tabla hash
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
        Agregar una tupla [key, value] en la tabla de hash en la posicion adecuada.
        Si la key No existe, agregar una tupla [key, value] a la tabla hash SC en la posicion indicada
        Si la key Ya existe, se reemplaza el value asociado a la key
        Nota: Si se agrega la nueva tupla, hay que actualizar el factor de carga self.estructura['currentfactor']

        Args:
            key: llave a agregar
            value: valor asociado a la llave

        Returns:
            -

        '''
        tupla = [key, value]      #nueva tupla
        h = self.hashValue(key)   # posicion del bucket para la tupla
        bucket = self.estructura['table'][h]    # bucket donde debe guardarse la tupla [key, value]

        #TODO completar la funcion (ubicar la tupla dentro del bucket considerando los dos casos posibles)
        #Si se agrega la nueva tupla hay que actualizar el factor de carga self.estructura['currentfactor']
        #El factor de carga es la division del numero de tuplas entre el tamaNo de la tabla

        
        #TODO verificar valor de factor de carga actual
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
        Elimina una tupla [key, value] de la tabla hash separate chaining.
        Si la key existe y se puede eliminar se retorna True. 
        Si la key NO existe, No se puede eliminar y se retorna False
        Nota: Si se elimina la tupla, hay que actualizar el factor de carga self.estructura['currentfactor']

        Args:
            key: llave a eliminar

        Returns:
           True si la key se encontro y se elimino, False si la key NO se encontro.

        '''
        h = self.hashValue(key)   # posicion del bucket
        bucket = self.estructura['table'][h]    # bucket donde debe buscarse y eliminarse la tupla [key, value]
        
        #TODO completar la funcion considerando los dos casos posibles
        #Si se elimina la tupla hay que actualizar el factor de carga self.estructura['currentfactor']
        #El factor de carga es la division del numero de tuplas entre el tamaNo de la tabla

    def getNodeValues(self):
        '''
        Da todas las llaves de la tabla de hash agrupadas por buckets (en el orden de aparicion)
        Nota: Cada bucket, agrega sus llaves a una lista como valor string separadas por la cadena '\\n'

        Args:
            -

        Returns:
            Lista (python) con todos los buckets de la tabla hash en el orden de aparicion.
            Cada bucket con sus llaves como string separadas por la cadena '\\n'. 

        '''
        resp = list()
        for i in range(self.estructura['m']):
            bucket = self.estructura['table'][i]    # bucket de la posicion i

            keysBucket = ""
            for tupla in bucket:
                #Cada llave se debe agregar a la lista como valor string y seguido por la cadena '\\n'
                keysBucket += str(tupla[0]) + '\\n'
            
            resp.append(keysBucket)
        
        return resp

    def getNodeValuesVal(self):
        '''
        Retornar los keys de la tabla de hash en el orden que se tienen
        Nota: Cada llave se debe agregar a la lista con su valor original

        Args:
            -

        Returns:
            Lista (python) con todas las llaves de la tabla hash, en el orden de aparicion

        '''
        resp = list()
        for i in range(self.estructura['m']):
            bucket = self.estructura['table'][i]    # bucket de la posicion i
            #TODO completar la funcion
            #Cada llave se debe agregar a la lista con su valor original

        return resp

    def isNodeValue(self, key):
        '''
        Informa si una llave pertenece o no a la tabla hash SC

        Args:
            key: llave que se busca

        Returns:
            True si la llave pertenece a la tabla de hash, False si no pertenece

        '''
        h = self.hashValue(key)   # posicion del bucket
        bucket = self.estructura['table'][h]    # bucket donde debe buscarse la tupla con [key, value]
        #TODO completar la funcion considerando los dos casos posibles. Retornat valor boolean.

    def rehash(self):
        '''
        Aplicar el rehash a la tabla definida en self.estructura
        El nuevo tamaño es el proximo primo mayor al doble de la tabla original
        Reubicar las tuplas [key, value] de la tabla original en la nueva tabla 
        La nueva tabla debe quedar en self.estructura

        Returns:
            -
        '''
        m_nuevo = 2*self.estructura['limitfactor']*self.estructura['m']
        nueva_tabla = SeparateChaining(numelements=m_nuevo)
        #TODO completar (reubicar las tuplas [key, value] que estan en la tabla original self.estructura a la nueva_tabla)

        # pasar los datos de la nueva tabla a self.estructura
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
