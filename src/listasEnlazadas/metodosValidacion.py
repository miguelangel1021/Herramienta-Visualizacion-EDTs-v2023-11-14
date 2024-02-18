import functools
from soporte.soporte import defaultfunction
from referencias.lista_disc import listaEnlazada as referenciaLista



VALIDATION_STATES = {0:'WARNING', 1:'SUCCESSFUL', -1:'FAILED'} # Estados resultantes del proceso de validacion
colorPointer = 'grey'   # Color para apuntadores
colorRight = 'blue'     # Color para conexiones a la derecha
colorLeft = 'green'     # Color para conexiones a la izquierda
colorHigh = 'red'       # Color para resaltar un elemento
col = "black"           # Color por defecto


def validar_lista_crear(nodos, st_nodos, tipo):
    '''
    Valida la operacion de crear una lista enlazada
       
    Args:
        nodos: nodos que se añadieron al crear la lista enlazada
        st_nodos: nodos que la estructura tiene
        tipo: tipo de lista enlazada (1: sencilla, 2: doble)
               
    Returns:
        state_val: Estado final de la validacion (WARNING, SUCCESSFUL, FAILED)
        comment: mensaje informativo para el usuario
        
    '''
    txt_nodos = ''
    for i in nodos:
        txt_nodos = txt_nodos + str(i) + ', '
    
    txt_st = ''
    for i in st_nodos:
        txt_st = txt_st + str(i) + ', '
        
    if len(nodos) == len(st_nodos):
        if nodos == st_nodos:
            if len(nodos) != 0:
                comment = 'Elementos: ' + txt_nodos[:-2]
            else:
                comment = 'Elementos: []'
            state_val = VALIDATION_STATES[1]
        else:
            nodos = sorted(nodos, key=functools.cmp_to_key(defaultfunction))
            st_nodos = sorted(st_nodos, key=functools.cmp_to_key(defaultfunction))
            
            if nodos == st_nodos:
                comment = 'Se añadieron los elementos pero en un orden diferente'
                comment = comment + '\nSe esperaba: ' + txt_nodos[:-2]
                comment = comment + '\n  Se obtuvo: ' + txt_st[:-2]
                state_val = VALIDATION_STATES[0]
            else:
                comment = 'Se añadieron elementos diferentes a los indicados'
                comment = comment + '\nSe esperaba: ' + txt_nodos[:-2]
                comment = comment + '\n  Se obtuvo: ' + txt_st[:-2]
                state_val = VALIDATION_STATES[-1]
    else:
        comment = 'Se añadieron más elementos de los esperados'
        comment = comment + '\nSe esperaba: ' + txt_nodos[:-2]
        comment = comment + '\n  Se obtuvo: ' + txt_st[:-2]
        state_val = VALIDATION_STATES[-1]
        
    return state_val, comment

def validar_lista_anadir(init_test, end_test, nodo, tipo):
    '''
    Valida la operacion de añadir un elemento a la lista enlazada. 
    Se espera que el elemento se añada al final (contrato de los metodos de la estructura)
       
    Args:
        init_test: lista de elementos de la lista enlazada antes de ejecutar la operacion
        end_test: lista de elementos de la lista enlazada despues de ejecutar la operacion
        nodo: nodo que se añade a la lista enlazada
        tipo: tipo de lista enlazada (1: sencilla, 2: doble)
        
    Returns:
        state_val: Estado final de la validacion (WARNING, SUCCESSFUL, FAILED)
        end_val: lista de los elementos de la estructura de referencia al ejecutar la operacion en cuestion
        comment: mensaje informativo para el usuario
    '''
    structure_ref = referenciaLista(tipo)
    for i in init_test:                     #Inicializacion de la estructura de prueba
        structure_ref.addNode_byValue(i)
    structure_ref.addNode_byValue(nodo)     #Ejecutar Funcion de Prueba
    end_val = structure_ref.getNodeValues() #Resultado de validacion
    
    if len(end_test) == len(end_val): # Hay la cantidad esperada de elementos
        sameOrder = True
        for i in range(len(end_test)):
            if end_test[i] != end_val[i]:
                sameOrder = False
                break                       
        if sameOrder:
            comment = 'El elemento "'+ str(nodo) + '" se añadió Bien'
            state_val = VALIDATION_STATES[1]
        else:
            test = set(end_test)
            val = set(end_val)
            if test == val:
                comment = 'El elemento "'+ str(nodo) + '" se añadió satisfactoriamente, pero no en la posición esperada'
                state_val = VALIDATION_STATES[0]
            else:
                comment = 'El elemento "'+ str(nodo) + '" NO se añadió, hay un elemento adicional pero no corresponde al elemento esperado'
                state_val = VALIDATION_STATES[-1]
    elif len(end_test) == len(end_val) - 1: # no hay cambios en la cantidad de elementos
        sameOrder = True
        for i in range(len(end_test)):
            if end_test[i] != end_val[i]:
                sameOrder = False
                break
        if sameOrder:
            comment = 'No se añadió el elemento "' + str(nodo) + '"'
            state_val = VALIDATION_STATES[-1]
        else:
            comment = 'El elemento "'+ str(nodo) + '" pudo haberse añadido, pero reemplazó a un elemento de la lista'
            state_val = VALIDATION_STATES[-1]
    elif len(end_test) < len(init_test): # Se eliminaron elementos
        comment = 'Se eliminaron elementos de la lista, hay menos de los que habian antes de ejecutar la operación de añadir'
        state_val = VALIDATION_STATES[-1]
    else:   # Hay mas elementos de los esperados
        cant = len(end_test) - len(end_val)
        comment = 'Hay '+ str(cant) + ' elementos más de los esperados'
        state_val = VALIDATION_STATES[-1]
    
    return state_val, end_val, comment

def validar_enlaces_anteriores(init_test, end_test, end_test_reverse, operacion, nodo, tipo):
    '''
    CORRECCION Nueva funcion para lista doblemente encadenada
    Valida el contenido de los elementos de atras hacia adelante
    Args:
        init_test: lista de elementos de la lista enlazada antes de ejecutar la operacion
        end_test: lista de elementos de la lista enlazada despues de ejecutar la operacion hacia adelante
        end_test_reverse: lista de elementos de la lista enlazada despues de ejecutar la operacion hacia atras
    '''
    num_elementos_adelante = len(end_test)
    num_elementos_atras = len(end_test_reverse)

    state_val = VALIDATION_STATES[1]
    comment = 'OK recorridos hacia adelante y hacia atras \n'
      
    structure_ref = referenciaLista(tipo)
    for i in init_test:            #Inicializacion de la estructura de prueba
        structure_ref.addNode_byValue(i)

    if operacion == 'addNodeLast':
        structure_ref.addNode_byValue(nodo)     #Ejecutar Funcion de Referencia agregar al final
    elif operacion == 'addNodeFirst':
        structure_ref.addNode_byValueFirst(nodo)     #Ejecutar Funcion de Referencia agregar al principio
    elif operacion == 'deleteNode':
        structure_ref.deleteNode_byValue(nodo)  #Ejecutar Funcion de Referencia eliminar nodo

    end_val = structure_ref.getNodeValues()                   #Resultado de validacion hacia adelante
    end_val_anteriores = structure_ref.getNodeValuesReverse() #Resultado de validacion hacia atras

    if num_elementos_adelante != num_elementos_atras:
        state_val = VALIDATION_STATES[-1]
        comment = 'Problema enlaces al interior de la lista resultante.\n'
        # comment += str(estructura.estructura) + '\n'            # contenido de la lista a probar (estudiante)
        comment += 'Diferencia en numero de elementos: ' + str(num_elementos_adelante) + ' elementos recorriendo hacia adelante y ' + str(num_elementos_atras) + ' recorriendo hacia atras\n'
        # comment += 'Recorrido elementos del primero al ultimo: ' + str(end_test) + '\n'
        # comment += 'Recorrido elementos del ultimo al primero: ' + str(end_test_reverse)
        return state_val, end_val, end_val_anteriores, comment

    if state_val == VALIDATION_STATES[1]:
        for i in range(len(end_test)):
            if defaultfunction(end_test[i], end_test_reverse[num_elementos_atras-1-i]) != 0:
                state_val = VALIDATION_STATES[-1]
                comment = 'Problema enlaces al interior lista resultante.\n'
                comment += 'Diferencia en los elementos recorriendo hacia adelante y recorriendo hacia atras'
                comment += 'El elemento hacia adelante en posicion ' + str(i) + ' deberia ser igual al elemento hacia atras en posicion ' + str(num_elementos_atras-1-i)
                comment += 'Elemento hacia adelante ' + str(end_test[i]) + ' NO es igual al elemento hacia atras ' + str(end_test_reverse[num_elementos_atras-1-i])
                return state_val, end_val, end_val_anteriores, comment

    # complemento al resultado cuando funciona bien
    # comment += str(estructura.estructura) + '\n'                 # contenido de la lista a probar (estudiante)
    # comment += str(num_elementos_adelante) + ' elementos recorriendo hacia adelante y ' + str(num_elementos_atras) + ' recorriendo hacia atras\n'
    # comment += 'Recorrido elementos del primero al ultimo: ' + str(end_test) + '\n'
    # comment += 'Recorrido elementos del ultimo al primero: ' + str(end_test_reverse)

    return state_val, end_val, end_val_anteriores, comment    

def validar_lista_anadir_first(init_test, end_test, nodo, tipo):
    '''
    Valida la operacion de añadir un elemento a la lista enlazada. 
    Se espera que el elemento se añada al final (contrato de los metodos de la estructura)
       
    Args:
        init_test: lista de elementos de la lista enlazada antes de ejecutar la operacion
        end_test: lista de elementos de la lista enlazada despues de ejecutar la operacion
        nodo: nodo que se añade a la lista enlazada
        tipo: tipo de lista enlazada (1: sencilla, 2: doble)
        
    Returns:
        state_val: Estado final de la validacion (WARNING, SUCCESSFUL, FAILED)
        end_val: lista de los elementos de la estructura de referencia al ejecutar la operacion en cuestion
        comment: mensaje informativo para el usuario
    '''
    structure_ref = referenciaLista(tipo)
    for i in init_test:                     #Inicializacion de la estructura de prueba
        structure_ref.addNode_byValue(i)
    structure_ref.addNode_byValueFirst(nodo)     #Ejecutar Funcion de Prueba
    end_val = structure_ref.getNodeValues() #Resultado de validacion
    
    if len(end_test) == len(end_val): # Hay la cantidad esperada de elementos
        sameOrder = True
        for i in range(len(end_test)):
            if end_test[i] != end_val[i]:
                sameOrder = False
                break                       
        if sameOrder:
            comment = 'El elemento "'+ str(nodo) + '" se añadió Bien'
            state_val = VALIDATION_STATES[1]
        else:
            test = set(end_test)
            val = set(end_val)
            if test == val:
                comment = 'El elemento "'+ str(nodo) + '" se añadió satisfactoriamente, pero no en la posición esperada'
                state_val = VALIDATION_STATES[0]
            else:
                comment = 'El elemento "'+ str(nodo) + '" NO se añadió, hay un elemento adicional pero no corresponde al elemento esperado'
                state_val = VALIDATION_STATES[-1]
    elif len(end_test) == len(end_val) - 1: # no hay cambios en la cantidad de elementos
        sameOrder = True
        for i in range(len(end_test)):
            if end_test[i] != end_val[i]:
                sameOrder = False
                break
        if sameOrder:
            comment = 'No se añadió el elemento "' + str(nodo) + '"'
            state_val = VALIDATION_STATES[-1]
        else:
            comment = 'El elemento "'+ str(nodo) + '" pudo haberse añadido, pero reemplazó a un elemento de la lista'
            state_val = VALIDATION_STATES[-1]
    elif len(end_test) < len(init_test): # Se eliminaron elementos
        comment = 'Se eliminaron elementos de la lista, hay menos de los que habian antes de ejecutar la operación de añadir'
        state_val = VALIDATION_STATES[-1]
    else:   # Hay mas elementos de los esperados
        cant = len(end_test) - len(end_val)
        comment = 'Hay '+ str(cant) + ' elementos más de los esperados'
        state_val = VALIDATION_STATES[-1]
    return state_val, end_val, comment

def validar_lista_eliminar(init_test, end_test, nodo, tipo, ans):
    '''
    Valida la operacion de eliminar un elemento de la lista enlazada. 
    Se espera que el elemento se elimine de la lista.
       
    Args:
        init_test: lista de elementos de la lista enlazada antes de ejecutar la operacion
        end_test: lista de elementos de la lista enlazada despues de ejecutar la operacion
        nodo: nodo que se elimina de la lista enlazada
        tipo: tipo de lista enlazada (1: sencilla, 2: doble)
        ans: resultado (True/False) de ejecutar el metodo deleteNode_byValue() en la estructura de prueba
        
    Returns:
        state_val: Estado final de la validacion (WARNING, SUCCESSFUL, FAILED)
        end_val: lista de los elementos de la estructura de referencia al ejecutar la operacion en cuestion
        comment: mensaje informativo para el usuario
    '''
    structure_ref = referenciaLista(tipo)
    for i in init_test:                     #Inicializacion de la estructura de prueba
        structure_ref.addNode_byValue(i)
    ans2 = structure_ref.deleteNode_byValue(nodo)  #Ejecutar accion
    end_val = structure_ref.getNodeValues() #Resultado de validacion

    if len(end_test) != len(end_val):         # numero de elementos diferentes despues de la operacion
        detail = 'El numero de elementos resultado de la operacion es diferente. Se esperaba ' + str(len(end_val)) + ' y se obtuvo ' + str(len(end_test))
        comment = 'Problema en eliminacion de "'+ str(nodo) + '" \n' + detail
        state_val = VALIDATION_STATES[-1]
    elif ans == ans2 and ans:   # key aparecia en Lista y se elimino
        comment = 'El elemento "'+ str(nodo) + '" se eliminó satisfactoriamente'
        state_val = VALIDATION_STATES[1]
    elif ans == ans2:         # key No aparece en Lista y No se elimino
        comment = 'El elemento "'+ str(nodo) + '" NO esta en la Lista y NO se eliminó'
        state_val = VALIDATION_STATES[0]
    else:
        detail = 'El resultado de return del método es diferente al esperado. Se esperaba ' + str(ans2) + ' y se obtuvo ' + str(ans)
        comment = 'Problema en eliminacion de "'+ str(nodo) + '" \n' + detail
        state_val = VALIDATION_STATES[-1]

    '''
    # SIMPLIFICACION de validacion
    if nodo not in init_test:
        comment = "El elemento " + str(nodo) + " no se encuentra en la lista, por lo tanto no se puede eliminar"
        state_val = VALIDATION_STATES[0]
    elif len(end_test) == len(end_val): # Hay la cantidad esperada de elementos
        sameOrder = True
        for i in range(len(end_test)):
            if end_test[i] != end_val[i]:
                sameOrder = False
                break                       
        if sameOrder:
            comment = 'El elemento "'+ str(nodo) + '" se eliminó satisfactoriamente'
            state_val = VALIDATION_STATES[1]
        else:
            end_test = sorted(end_test, key=functools.cmp_to_key(defaultfunction))
            end_val = sorted(end_val, key=functools.cmp_to_key(defaultfunction))
            if(end_test == end_val):
                comment = 'Se eliminó una de las instancias del elemento "'+ str(nodo) + '"'
                state_val = VALIDATION_STATES[1]
            else:
                comment = 'El elemento "'+ str(nodo) + '" No se eliminó satisfactoriamente, se eliminó un elemento diferente'
                state_val = VALIDATION_STATES[-1]
    elif len(end_test) == len(init_test): # no hay cambios en la cantidad de elementos
        sameOrder = True
        for i in range(len(end_test)):
            if end_test[i] != init_test[i]:
                sameOrder = False
                break
        if sameOrder:
            comment = 'No se eliminó el elemento "' + str(nodo) + '". La lista no presenta cambios'
            state_val = VALIDATION_STATES[-1]
        else:
            comment = 'No se eliminó el elemento "' + str(nodo) + '". La lista presenta cambios no esperados'
            state_val = VALIDATION_STATES[-1]     
    elif len(end_test) < len(end_val): # Se eliminaron mas elementos
        test = set(end_test)
        val = set(end_val)
        if nodo not in end_test:
            comment = 'Se eliminaron todas las instancias del elemento "' + str(nodo) +'" cuando solo una de ellas se debia eliminar'
            state_val = VALIDATION_STATES[0]
        elif test == val:
            comment = 'Se eliminaron más instancias del elemento "' + str(nodo) +'" cuando solo una de ellas se debia eliminar'
            state_val = VALIDATION_STATES[-1]
        else:
            comment = 'Se eliminaron más elementos de los esperados'
            state_val = VALIDATION_STATES[-1]
    else:   # Hay mas elementos de los esperados
        cant = len(end_test) - len(end_val)
        comment = 'Hay '+ str(cant) + ' elementos más de los esperados'
        state_val = VALIDATION_STATES[-1]
    
    if ans != ans2:
        ans2 = 'El resultado de return del método es diferente al esperado. Se esperaba ' + str(ans2) + ' y se obtuvo ' + str(ans)
        comment = comment + '\n' + ans2   
    '''
    return state_val, end_val, comment

def validar_lista_encontrar(nodos, nodo, ans):
    '''
    Valida la operacion de encontrar un elemento en la lista enlazada.
       
    Args:
        nodos: lista de elementos de la lista enlazada antes de ejecutar la operacion
        nodo: nodo que se busca en la lista enlazada
        ans: resultado (True/False) de ejecutar el metodo isNodeValue() en la estructura de prueba
        
    Returns:
        state_val: Estado final de la validacion (WARNING, SUCCESSFUL, FAILED)
        ans_val: resultado (True/False) al ejecutar el metodo isNodeValue() en la estructura de referencia
        comment: mensaje informativo para el usuario
    '''
    if nodo in nodos:
        ans_val = True
    else:
        ans_val = False
    
    if ans == ans_val:
        if ans:
            comment = 'El elemento "'+ str(nodo) + '" SI se encuentra en la lista'
        else:
            comment = 'El elemento "'+ str(nodo) + '" NO se encuentra en la lista'
        state_val = VALIDATION_STATES[1]
    elif ans_val:
        comment = 'El elemento "'+ str(nodo) + '" SI se encuentra en la lista pero el método isNodeVale() reporta que NO se encuentra'
        state_val = VALIDATION_STATES[-1]
    else:
        comment = 'El elemento "'+ str(nodo) + '" NO se encuentra en la lista pero el método isNodeVale() reporta que SI se encuentra'
        state_val = VALIDATION_STATES[-1]
    
    return state_val, ans_val, comment

def validar_lista_adyacentes(init_test, listaAdj, nodo, tipo):
    '''
    Valida la operacion de encontrar los valores de los nodos adyacentes a un 
    elemento en la lista enlazada.
       
    Args:
        init_test: lista de elementos de la lista enlazada antes de ejecutar la operacion
        listaAdj: lista de valores de nodos adyacentes obtenida por la estructura de prueba
        nodo: nodo al cual se le buscan los adyacentes
        tipo: tipo de lista enlazada (1: sencilla, 2: doble)
               
    Returns:
        state_val: Estado final de la validacion (WARNING, SUCCESSFUL, FAILED)
        listaAdj_val: lista de los elementos adyacentes obtenidos por la estructura de referencia
        comment: mensaje informativo para el usuario
        exists: indica si el nodo existe en la lista
        
    '''
    structure_ref = referenciaLista(tipo)
    for i in init_test:                     #Inicializacion de la estructura de prueba
        structure_ref.addNode_byValue(i)

    listaAdj_val = structure_ref.findAdjacentNode(nodo)
    exists = structure_ref.isNodeValue(nodo)
    
    ''' CORRECCION Borrar
    listaAdj_val = sorted(listaAdj_val, key=functools.cmp_to_key(defaultfunction))
    listaAdj = sorted(listaAdj, key=functools.cmp_to_key(defaultfunction))
    '''

    if len(listaAdj) != len(listaAdj_val) or listaAdj != listaAdj_val:
        comment = 'Diferencias en los adyacentes\n'
        comment += 'Se esperaban los adyacentes: ' + str(listaAdj_val) + '\n'
        comment += 'Se obtuvieron los adyacentes: ' + str(listaAdj)
        state_val = VALIDATION_STATES[-1]
    else:
        comment = 'El elemento "'+ str(nodo)+ '" tiene '+str(len(listaAdj_val))+' adyacente(s): ' + str(listaAdj)
        state_val = VALIDATION_STATES[1]

    '''
    txt = ''
    for i in listaAdj_val:
        txt = txt + str(i) + ', '
        
    if listaAdj == listaAdj_val:
        comment = 'El elemento "'+ str(nodo)+ '" tiene '+str(len(listaAdj_val))+' adyacente(s): ' + txt[:-2]
        state_val = VALIDATION_STATES[1]
    else:
        comment = 'No se encontraron todos los adyacentes del elemento\nSe esperaban los elementos: ' + txt[:-2]
        txt = ''
        for i in listaAdj:
            txt = txt + str(i) + ', '
        comment = comment + '\nSe obtuvo: ' + txt[:-2]
        state_val = VALIDATION_STATES[-1]
    '''
    return state_val, listaAdj_val, comment, exists