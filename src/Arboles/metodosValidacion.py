import functools
from soporte.soporte import defaultfunction, VALIDATION_STATES
from referencias.arbol_BST_disc import bst as referenciaBST
from referencias.arbol_RBT_disc import RBT as referenciaRBT


def validar_bst_crear(nodos, end_test):
    '''
    Valida la operacion de crear un arbol BST
       
    Args:
        nodos: llaves que se añadieron al crear el BST
        end_test: llaves que tiene el BST 
               
    Returns:
        state_val: Estado final de la validacion (WARNING, SUCCESSFUL, FAILED)
        end_val: llaves en la estructura de referencia ("Preorder")
        comment: mensaje informativo para el usuario
        
    '''
    state_val = VALIDATION_STATES[1]
    end_val = list()
    comment = 'Sin validacion en el BST'
    # return state_val, end_val, comment

    structure_ref = referenciaBST()
    for key in nodos:                     #Inicializacion de la estructura de prueba
        structure_ref.addNode_byValue(key)
    
    end_val = structure_ref.getNodeValues("Preorder")
    
    if len(end_test) != len(end_val):         # numero de elementos diferentes despues de la operacion
        detail = 'El numero de llaves resultado de la operacion es diferente. Se esperaba ' + str(len(end_val)) + ' y se obtuvo ' + str(len(end_test))
        comment = 'Problema en crear BST ' + '\n' + detail
        state_val = VALIDATION_STATES[-1]

    else: # Hay la cantidad esperada de elementos
        sameOrder = True
        for i in range(len(end_test)):
            if (end_test[i] != end_val[i]):
                sameOrder = False
                break
        if sameOrder:
            comment = 'Creación de BST satisfactoria'
            state_val = VALIDATION_STATES[1]
        else:
            comment = 'Creación de BST con llaves en orden diferente'
            state_val = VALIDATION_STATES[-1]

    return state_val, end_val, comment

    ''' SIMPLIFICACION DE LA VALIDACION
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
    '''

def validar_bst_anadir(init_test, end_test, nodo):
    '''
    Valida la operacion de añadir un elemento al BST. 
    Se espera que el elemento se añada en la posicion correcta
       
    Args:
        init_test: lista de elementos del BST antes de ejecutar la operacion
        end_test: lista de elementos del BST despues de ejecutar la operacion
        nodo: nodo que se añade al arbol
        
    Returns:
        state_val: Estado final de la validacion (WARNING, SUCCESSFUL, FAILED)
        end_val: lista de los elementos en Preorder de la estructura de referencia al ejecutar la operacion en cuestion
        comment: mensaje informativo para el usuario
    '''
    state_val = VALIDATION_STATES[1]
    end_val = list()
    comment = 'No se hace validacion.'
    # return state_val, end_val, comment

    structure_ref = referenciaBST()
    for key in init_test:                     #Inicializacion de la estructura de prueba
        structure_ref.addNode_byValue(key)
    structure_ref.addNode_byValue(nodo)     #Ejecutar accion
    end_val = structure_ref.getNodeValues("Preorder") #Resultado de validacion

    if len(end_test) != len(end_val):         # numero de llaves diferentes despues de la operacion
        detail = 'El numero de llaves resultado de la operacion es diferente.' + '\n'
        detail += 'Se esperaba ' + str(len(end_val)) + ' y se obtuvo ' + str(len(end_test))
        comment = 'Problema entre BST creado y BST de validación' + '\n' + detail
        state_val = VALIDATION_STATES[-1]

    else: # Hay la cantidad esperada de llaves
        sameOrder = True
        for i in range(len(end_test)):
            if (end_test[i] != end_val[i]):
                sameOrder = False
                break
        if sameOrder:
            comment = 'Validación de BST satisfactoria'
            state_val = VALIDATION_STATES[1]
        else:
            comment = 'BST de validación con llaves en orden diferente'
            state_val = VALIDATION_STATES[-1]

    return state_val, end_val, comment

    ''' SIMPLIFICACION DE LA VALIDACION    
    if len(end_test) == len(end_val): # Hay la cantidad esperada de elementos
        sameOrder = True
        if len(init_test) == len(end_val):
            comment = 'El elemento "'+ str(nodo) + '" ya se encontraba en el bst'
            state_val = VALIDATION_STATES[1]
        else:
            for i in range(len(end_test)):
                if end_test[i] != end_val[i]:
                    sameOrder = False
                    break                       
            if sameOrder:
                comment = 'El elemento "'+ str(nodo) + '" se añadió satisfactoriamente'
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
    '''

def validar_bst_eliminar(init_test, end_test, nodo, ans):
    '''
    Valida la operacion de eliminar un elemento del BST. 
       
    Args:
        init_test: lista de elementos del BST antes de ejecutar la operacion
        end_test: lista de elementos del BST despues de ejecutar la operacion
        nodo: nodo que se elimina del BST
        ans: resultado (True/False) de ejecutar el metodo deleteNode_byValue() en la estructura de prueba
        
    Returns:
        state_val: Estado final de la validacion (WARNING, SUCCESSFUL, FAILED)
        end_val: lista de los elementos de la estructura de referencia al ejecutar la operacion en cuestion
        comment: mensaje informativo para el usuario
    '''
    state_val = VALIDATION_STATES[1]
    end_val = list()
    comment = 'No se hace validacion.'
    # return state_val, end_val, comment

    structure_ref = referenciaBST()
    for key in init_test:                     #Inicializacion de la estructura de prueba
        structure_ref.addNode_byValue(key)
    ans2 = structure_ref.deleteNode_byValue(nodo)  #Ejecutar accion
    end_val = structure_ref.getNodeValues("Preorder") #Resultado de validacion
    # return state_val, end_val, comment

    if len(end_test) != len(end_val):         # numero de elementos diferentes despues de la operacion
        detail = 'El numero de llaves resultado de la operacion es diferente.' + '\n'  
        detail += 'Se esperaba ' + str(len(end_val)) + ' y se obtuvo ' + str(len(end_test))
        comment = 'Problema en eliminacion de "'+ str(nodo) + '" \n' + detail
        state_val = VALIDATION_STATES[-1]
    elif ans != ans2:
        detail = 'El resultado de return de la función es diferente al esperado.' + '\n'
        detail += 'Se esperaba ' + str(ans2) + ' y se obtuvo ' + str(ans)
        comment = 'Problema en eliminacion de "'+ str(nodo) + '" \n' + detail
        state_val = VALIDATION_STATES[-1]
    elif ans == ans2 and ans:   # key aparecia en arbol BST y se elimino
        sameOrder = True
        for i in range(len(end_test)):
            if (end_test[i] != end_val[i]):
                sameOrder = False
                break
        if sameOrder:
            comment = 'Validación de BST satisfactoria'
            state_val = VALIDATION_STATES[1]
        else:
            comment = 'Validación de BST con llaves en orden diferente'
            state_val = VALIDATION_STATES[-1]
    elif ans == ans2:         # key No aparecia en arbol BST y No se elimino
        comment = 'La llave "'+ str(nodo) + '" NO esta en el arbol BST y NO se eliminó'
        state_val = VALIDATION_STATES[0]

    return state_val, end_val, comment

    ''' SIMPLIFICACION VALIDACION 

    if nodo not in init_test:
        comment = "El elemento " + str(nodo) + " no se encuentra en el arbol, por lo tanto no se puede eliminar"
        state_val = VALIDATION_STATES[0]
      
    elif len(end_test) == len(end_val): # Hay la cantidad esperada de elementos
        sameOrder = True
        for i in range(len(end_test)):
            if end_test[i] != end_val[i]:
                sameOrder = False
                break                       
        if sameOrder and end_test != init_test:
            comment = 'El elemento "'+ str(nodo) + '" se eliminó satisfactoriamente'
            state_val = VALIDATION_STATES[1]
        else:
            comment = 'El elemento "'+ str(nodo) + '" No se pertenece al BST'
            state_val = VALIDATION_STATES[0]
    elif len(end_test) == len(init_test): # no hay cambios en la cantidad de elementos
        sameOrder = True
        for i in range(len(end_test)):
            if end_test[i] != init_test[i]:
                sameOrder = False
                break
        if sameOrder:
            comment = 'No se eliminó el elemento "' + str(nodo) + '". La estructura no presenta cambios'
            state_val = VALIDATION_STATES[-1]
        else:
            comment = 'No se eliminó el elemento "' + str(nodo) + '". La estructura presenta cambios no esperados'
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

def validar_bst_encontrar(nodos, nodo, ans):
    '''
    Valida la operacion de encontrar un elemento en el BST.
       
    Args:
        nodos: lista de elementos del BST antes de ejecutar la operacion
        nodo: nodo que se busca en el BST
        ans: resultado (True/False) de ejecutar el metodo isNodeValue() en la estructura de prueba
        
    Returns:
        state_val: Estado final de la validacion (WARNING, SUCCESSFUL, FAILED)
        end_ans: resultado (True/False) de ejecutar el metodo isNodeValue() en la estructura de referencia
        end_val: lista de llaves en la estructura de referencia
        comment: mensaje informativo para el usuario
    '''

    state_val = VALIDATION_STATES[1]
    end_val = list()
    end_ans = False
    comment = 'No se hace validacion.'
    # return state_val, end_ans, end_val, comment

    structure_ref = referenciaBST()
    for key in nodos:                     #Inicializacion de la estructura de prueba
        structure_ref.addNode_byValue(key)
    end_ans = structure_ref.isNodeValue(nodo)  #Ejecutar accion
    end_val = structure_ref.getNodeValues("Preorder") #Resultado de validacion

    if len(nodos) != len(end_val):         # numero de elementos diferentes despues de la operacion
        detail = 'Se esperaba BST de validación con ' + str(len(nodos)) + ' y se obtuvo ' + str(len(end_val))
        comment = 'Problema en inicializacion del BST de validación. '+ '\n' + detail
        state_val = VALIDATION_STATES[-1]
        return state_val, end_ans, end_val, comment

    if ans == end_ans:
        if ans:
            comment = 'El elemento "'+ str(nodo) + '" SI se encuentra en el BST'
            state_val = VALIDATION_STATES[1]
        else:
            comment = 'El elemento "'+ str(nodo) + '" NO se encuentra en el BST'
            state_val = VALIDATION_STATES[0]
    elif end_ans:
        comment = 'El elemento "'+ str(nodo) + '" SI se encuentra en el BST pero el método isNodeValue() reporta que NO se encuentra'
        state_val = VALIDATION_STATES[-1]
    else:
        comment = 'El elemento "'+ str(nodo) + '" NO se encuentra en el BST pero el método isNodeValue() reporta que SI se encuentra'
        state_val = VALIDATION_STATES[-1]
    
    return state_val, end_ans, end_val, comment

def validar_bst_adyacentes(init_test, existe, listaAdj, nodo):
    '''
    Valida la operacion de encontrar los valores de los nodos adyacentes a un 
    elemento en el BST.
       
    Args:
        init_test: lista de elementos del BST antes de ejecutar la operacion
        existe: si el nodo se encuentra o No en el BST
        listaAdj: lista de valores de nodos adyacentes obtenida por la estructura de prueba
        nodo: nodo al cual se le buscan los adyacentes
               
    Returns:
        state_val: Estado final de la validacion (WARNING, SUCCESSFUL, FAILED)
        existe_val: existe nodo en la estructura de referencia
        listaAdj_val: lista de los elementos adyacentes obtenidos por la estructura de referencia
        comment: mensaje informativo para el usuario        
    '''
    state_val = VALIDATION_STATES[1]
    existe_val = False
    listaAdj_val = list()
    comment = 'No se hace validacion.'
    # return state_val, existe_val, listaAdj_val, comment

    print("No se hace validacion.", existe_val, listaAdj_val)

    structure_ref = referenciaBST()
    for i in init_test:                     #Inicializacion de la estructura de prueba
        structure_ref.addNode_byValue(i)
    existe_val, listaAdj_val = structure_ref.findAdjacentNode(nodo)   
    
    print("validacion", existe_val, listaAdj_val)

    ''' SIMPLIFICACION VALIDACION
    listaAdj_val = sorted(listaAdj_val, key=functools.cmp_to_key(defaultfunction))
    listaAdj = sorted(listaAdj, key=functools.cmp_to_key(defaultfunction))
    txt = ''
    for i in listaAdj_val:
        txt = txt + str(i) + ', '
    '''

    print("caso validacion 1")
    if existe != existe_val:
        detail = 'Se esperaba existencia de la llave ' + str(existe_val) + ' y se obtuvo ' + str(existe)
        comment = 'Problema en la existencia de la llave '+ '\n' + detail
        state_val = VALIDATION_STATES[-1]
        return state_val, existe_val, listaAdj_val, comment

    print("caso validacion 2")
    if len(listaAdj) != len(listaAdj_val):         # numero de elementos diferentes despues de la operacion
        detail = 'Se esperaban ' + str(len(listaAdj_val)) + ' adyacentes y se obtuvieron ' + str(len(listaAdj))
        comment = 'Problema en el numero de adyacentes. '+ '\n' + detail
        state_val = VALIDATION_STATES[-1]
        return state_val, existe_val, listaAdj_val, comment

    print("caso validacion 3")
    if listaAdj == listaAdj_val:
        if existe_val:
            comment = 'La llave "'+ str(nodo) + '" existe y tiene ' + str(len(listaAdj_val)) + ' adyacente(s)'
            state_val = VALIDATION_STATES[1]
        else:
            comment = 'La llave "'+ str(nodo) + '" NO existe y tiene ' + str(len(listaAdj_val)) + ' adyacente(s)'
            state_val = VALIDATION_STATES[0]
    else:
        comment = 'Hay diferencia en los adyacentes de la llave "' + str(nodo) + '"'
        state_val = VALIDATION_STATES[-1]
     
    return state_val, existe_val, listaAdj_val, comment

def validar_bst_darNodos(init_test, nodos, orden):
    '''
    Valida la operacion de encontrar listar los valores de los nodos de un arbol dado un orden
       
    Args:
        init_test: lista de elementos del arbol en preorder
        nodos: lista de valores de nodos obtenida de listar los nodos en el orden dado
        orden: orden en el cual se listan los nodos (preorder, inorder, postorder)
               
    Returns:
        state_val: Estado final de la validacion (WARNING, SUCCESSFUL, FAILED)
        nodos_val: lista de los elementos en el orden dado, en la estructura de referencia
        comment: mensaje informativo para el usuario
        
    '''
    state_val = VALIDATION_STATES[1]
    nodos_val = list()
    comment = 'No se hace validacion.'
    # return state_val, nodos_val, comment

    structure_ref = referenciaBST()
    for i in init_test:                     #Inicializacion de la estructura de prueba
        structure_ref.addNode_byValue(i)
    
    nodos_val = structure_ref.getNodeValues(orden)
    
    '''
    txt_val = ''
    for i in nodos_val:
        txt_val = txt_val + str(i) + ', '
        
    txt_test = ''
    for i in nodos:
        txt_test = txt_test + str(i) + ', '
    '''
    if len(nodos) != len(nodos_val):         # numero de elementos diferentes despues de la operacion
        detail = 'El numero de llaves resultado del recorrido es diferente. Se esperaba ' + str(len(nodos_val)) + ' y se obtuvo ' + str(len(nodos))
        comment = 'Problema en recorrido ' + orden + '\n' + detail
        state_val = VALIDATION_STATES[-1]

    else: # Hay la cantidad esperada de elementos
        sameOrder = True
        for i in range(len(nodos)):
            if (nodos[i] != nodos_val[i]):
                sameOrder = False
                break
        if sameOrder:
            comment = 'Recorrido ' + orden + ' satisfactorio'
            state_val = VALIDATION_STATES[1]
        else:
            comment = 'Recorrido ' + orden + ' en orden diferente'
            state_val = VALIDATION_STATES[-1]

    return state_val, nodos_val, comment




#Metodos de validacion RBT
def validar_rbt_crear(nodos, st_nodos):
    '''
    Valida la operacion de crear un arreglo

    Args:
        nodos: nodos que se añadieron al crear el arreglo
        st_nodos: nodos que la estructura tiene

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
                comment = 'Nodos: ' + txt_nodos[:-2]
            else:
                comment = 'Nodos: []'
            state_val = VALIDATION_STATES[1]
        else:
            nodos = sorted(nodos, key=functools.cmp_to_key(defaultfunction))
            st_nodos = sorted(
                st_nodos, key=functools.cmp_to_key(defaultfunction))

            if nodos == st_nodos:
                comment = 'Nodos: ' + txt_nodos[:-2]
                state_val = VALIDATION_STATES[1]
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


def validar_rbt_anadir(init_test, end_test, nodo):
    '''
    Valida la operacion de añadir un elemento al RBT. 

    Args:
        init_test: lista de llaves del RBT antes de ejecutar la operacion
        end_test: lista de llaves del RBT despues de ejecutar la operacion
        nodo: nodo que se añade al RBT

    Returns:
        state_val: Estado final de la validacion (WARNING, SUCCESSFUL, FAILED)
        end_val: lista de llaves de la estructura de referencia al ejecutar la operacion en cuestion
        comment: mensaje informativo para el usuario
    '''
    # IMPORTANTE: Se requiere garantizar que el arbol RBT inicie con el mismo tamaNo, estructura y contenido que la estructura a validar
    structure_ref = referenciaRBT()

    state_val = VALIDATION_STATES[1]
    end_val = list()
    comment = 'No se hace validacion.'
    return state_val, end_val, comment

    for i in init_test:  # Inicializacion de la estructura de prueba
        structure_ref.addNode_byValue(i)
    structure_ref.addNode_byValue(nodo)  # Ejecutar accion
    end_val = structure_ref.getNodeValues()  # Resultado de validacion

    if len(end_test) == len(end_val):  # Hay la cantidad esperada de elementos
        sameOrder = True
        for i in range(len(end_test)):
            if end_test[i] != end_val[i]:
                sameOrder = False
                break
        if sameOrder:
            comment = 'El elemento "' + \
                str(nodo) + '" se añadió satisfactoriamente'
            state_val = VALIDATION_STATES[1]
        else:
            test = set(end_test)
            val = set(end_val)
            if test == val:
                comment = 'El elemento "' + \
                    str(nodo) + '" se añadió satisfactoriamente, pero no en la posición esperada'
                state_val = VALIDATION_STATES[0]
            else:
                comment = 'El elemento "' + \
                    str(nodo) + '" NO se añadió, hay un elemento adicional pero no corresponde al elemento esperado'
                state_val = VALIDATION_STATES[-1]
    elif len(end_test) == len(end_val) - 1:  # no hay cambios en la cantidad de elementos
        sameOrder = True
        for i in range(len(end_test)):
            if end_test[i] != end_val[i]:
                sameOrder = False
                break
        if sameOrder:
            comment = 'No se añadió el elemento "' + str(nodo) + '"'
            state_val = VALIDATION_STATES[-1]
        else:
            comment = 'El elemento "' + \
                str(nodo) + '" pudo haberse añadido, pero reemplazó a un elemento del arreglo'
            state_val = VALIDATION_STATES[-1]
    elif len(end_test) < len(init_test):  # Se eliminaron elementos
        comment = 'Se eliminaron elementos del arreglo, hay menos de los que habian antes de ejecutar la operación de añadir'
        state_val = VALIDATION_STATES[-1]
    else:   # Hay mas elementos de los esperados
        cant = len(end_test) - len(end_val)
        comment = 'Hay ' + str(cant) + ' elementos más de los esperados'
        state_val = VALIDATION_STATES[-1]
    return state_val, end_val, comment


def validar_rbt_eliminar(init_test, end_test, nodo, ans):
    '''
    Valida la operacion de eliminar un elemento del arreglo. 
    Se espera que el elemento se elimine del arreglo.

    Args:
        init_test: lista de elementos del arreglo antes de ejecutar la operacion
        end_test: lista de elementos del arreglo despues de ejecutar la operacion
        nodo: nodo que se elimina del arreglo
        ans: resultado (True/False) de ejecutar el metodo deleteNode_byValue() en la estructura de prueba

    Returns:
        state_val: Estado final de la validacion (WARNING, SUCCESSFUL, FAILED)
        end_val: lista de los elementos de la estructura de referencia al ejecutar la operacion en cuestion
        comment: mensaje informativo para el usuario
    '''

    structure_ref = referenciaRBT()
    for i in init_test:  # Inicializacion de la estructura de prueba
        structure_ref.addNode_byValue(i)
    ans2 = structure_ref.deleteNode_byValue(nodo)  # Ejecutar accion
    end_val = structure_ref.getNodeValues()  # Resultado de validacion
    
    print(end_test)
    print(end_val)

    if len(end_test) == len(end_val):  # Hay la cantidad esperada de elementos
        sameOrder = True
        for i in range(len(end_test)):
            if end_test[i] != end_val[i]:
                sameOrder = False
                break
        if sameOrder:
            if ans2 == False:
                comment = 'El elemento "' + \
                    str(nodo) + '" no hace parte del arbol'
                state_val = VALIDATION_STATES[1]
            else:
                comment = 'El elemento "' + \
                    str(nodo) + '" se eliminó satisfactoriamente'
                state_val = VALIDATION_STATES[1]
        else:
            end_test = sorted(
                end_test, key=functools.cmp_to_key(defaultfunction))
            end_val = sorted(
                end_val, key=functools.cmp_to_key(defaultfunction))
            if(end_test == end_val):
                if ans2 == False:
                    comment = 'El elemento "' + \
                        str(nodo) + '" no hace parte del arbol'
                    state_val = VALIDATION_STATES[1]
                else:
                    comment = 'No se eliminó satisfactoriamente, se eliminó un elemento diferente "' + \
                        str(nodo) + '"'
                    state_val = VALIDATION_STATES[1]
            else:
                comment = 'El elemento "' + \
                    str(nodo) + '" No se eliminó satisfactoriamente, se eliminó un elemento diferente'
                state_val = VALIDATION_STATES[-1]
    elif len(end_test) == len(init_test):  # no hay cambios en la cantidad de elementos
        sameOrder = True
        for i in range(len(end_test)):
            if end_test[i] != init_test[i]:
                sameOrder = False
                break
        if sameOrder:
            comment = 'No se eliminó el elemento "' + \
                str(nodo) + '". La lista no presenta cambios'
            state_val = VALIDATION_STATES[-1]
        else:
            comment = 'No se eliminó el elemento "' + \
                str(nodo) + '". La lista presenta cambios no esperados'
            state_val = VALIDATION_STATES[-1]
    elif len(end_test) < len(end_val):  # Se eliminaron mas elementos
        test = set(end_test)
        val = set(end_val)
        if nodo not in end_test:
            comment = 'No se eliminó satisfactoriamente, se eliminó un elemento diferente "'
            state_val = VALIDATION_STATES[0]
        elif test == val:
            comment = 'No se eliminó satisfactoriamente, se eliminó un elemento diferente "'
            state_val = VALIDATION_STATES[-1]
        else:
            comment = 'Se eliminaron más elementos de los esperados'
            state_val = VALIDATION_STATES[-1]
    else:   # Hay mas elementos de los esperados
        cant = len(end_test) - len(end_val)
        comment = 'Hay ' + str(cant) + ' elementos más de los esperados'
        state_val = VALIDATION_STATES[-1]

    if ans != ans2:
        ans2 = 'El resultado de return del método es diferente al esperado. Se esperaba ' + \
            str(ans2) + ' y se obtuvo ' + str(ans)
        comment = comment + '\n' + ans2

    return state_val, end_val, comment


def validar_rbt_encontrar(nodos, nodo, ans):
    '''
    Valida la operacion de encontrar un elemento en el RBT.

    Args:
        nodos: lista de elementos del RBT antes de ejecutar la operacion
        nodo: nodo que se busca en el RBT
        ans: resultado (True/False) de ejecutar el metodo isNodeValue() en la estructura de prueba

    Returns:
        state_val: Estado final de la validacion (WARNING, SUCCESSFUL, FAILED)
        ans_val: resultado (True/False) de ejecutar el metodo isNodeValue() en la estructura de referencia
        comment: mensaje informativo para el usuario
    '''
    if nodo in nodos:
        ans_val = True
    else:
        ans_val = False

    if ans == ans_val:
        if ans:
            comment = 'El elemento "' + \
                str(nodo) + '" SI se encuentra en el RBT'
        else:
            comment = 'El elemento "' + \
                str(nodo) + '" NO se encuentra en el RBT'
        state_val = VALIDATION_STATES[1]
    elif ans_val:
        comment = 'El elemento "' + \
            str(nodo) + '" SI se encuentra en el RBT pero el método isNodeValue() reporta que NO se encuentra'
        state_val = VALIDATION_STATES[-1]
    else:
        comment = 'El elemento "' + \
            str(nodo) + '" NO se encuentra en el RBT pero el método isNodeValue() reporta que SI se encuentra'
        state_val = VALIDATION_STATES[-1]

    return state_val, ans_val, comment

def validar_rbt_adyacentes(init_test, listaAdj, nodo):
    '''
    Valida la operacion de encontrar los valores de los nodos adyacentes a un 
    elemento en el grafo.
       
    Args:
        init_test: lista de elementos del grafo antes de ejecutar la operacion
        listaAdj: lista de valores de nodos adyacentes obtenida por la estructura de prueba
        nodo: nodo al cual se le buscan los adyacentes
               
    Returns:
        state_val: Estado final de la validacion (WARNING, SUCCESSFUL, FAILED)
        listaAdj_val: lista de los elementos adyacentes obtenidos por la estructura de referencia
        comment: mensaje informativo para el usuario
        exists: indica si el nodo existe en la lista
        
    '''
    structure_ref = referenciaRBT()
    for i in init_test:                     #Inicializacion de la estructura de prueba
        structure_ref.addNode_byValue(i)
    listaAdj_val = structure_ref.findAdjacentNode(nodo)   
    
    listaAdj_val = sorted(listaAdj_val, key=functools.cmp_to_key(defaultfunction))
    listaAdj = sorted(listaAdj, key=functools.cmp_to_key(defaultfunction))
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
    
    exists = structure_ref.isNodeValue(nodo)
    
    return state_val, listaAdj_val, comment, exists