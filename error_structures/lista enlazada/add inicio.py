class node():
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.before = None
    def hasNext(self):
        return self.next != None

class listaEnlazadaSencilla():
    def __init__(self):
        self.first = None
        
    def addNode_byValue(self, infoNodo):
        if self.first == None:
            self.first = node(infoNodo)
        else:
            nodo = self.first
            self.first = node(infoNodo)
            self.first.next = nodo
    
    def getNodeValues(self):
        listaNodos = list()
        nodo = self.first
        while(nodo != None):
            listaNodos.append(nodo.value)
            nodo = nodo.next
        return listaNodos
    
    def deleteNode_byValue(self, infoNodo):
        bol = False
        if self.first != None and self.first.value == infoNodo:
            self.first = self.first.next
            bol = True
                
        elif self.first != None:
            before = self.first
            actual = self.first.next
            while(actual != None):
                if actual.value == infoNodo:
                    before.next = actual.next
                    bol = True
                    break
                before = before.next
                actual = actual.next
        return bol
    
    def isNodeValue(self, infoNodo):
        bol = False
        nodo = self.first
        while(nodo != None):
            if nodo.value == infoNodo:
                bol = True
                break
            nodo = nodo.next
        return bol

    def findAdjacentNode(self, infoNodo):
        adj = list()
        nodo = self.first
        while(nodo != None):
            if nodo.value == infoNodo:
                if nodo.next != None:
                    adj.append(nodo.next.value)
                break
            nodo = nodo.next
        return adj

class listaEnlazadaDoble():
    def __init__(self):
        self.first = None
        
    def addNode_byValue(self, infoNodo):
        if self.first == None:
            self.first = node(infoNodo)
        else:
            nodo = self.first
            self.first = node(infoNodo)
            self.first.next = nodo
            nodo.before = self.first
    
    def getNodeValues(self): 
        listaNodos = list()
        nodo = self.first
        while(nodo != None):
            listaNodos.append(nodo.value)
            nodo = nodo.next
        return listaNodos
    
    def deleteNode_byValue(self, infoNodo):
        bol = False
        if self.first != None and self.first.value == infoNodo:
            aux = self.first
            self.first = aux.next
            if self.first != None:
                self.first.before = None
            bol = True
                
        elif self.first != None:
            before = self.first
            actual = self.first.next
            while(actual != None):
                if actual.value == infoNodo:
                    next = actual.next
                    if next != None:
                        next.before = before
                    before.next = next
                    bol = True
                    break
                before = before.next
                actual = actual.next
        return bol
    
    def isNodeValue(self, infoNodo):
        bol = False
        nodo = self.first
        while(nodo != None):
            if nodo.value == infoNodo:
                bol = True
                break
            nodo = nodo.next
        return bol

    def findAdjacentNode(self, infoNodo):
        adj = list()
        nodo = self.first
        while(nodo != None):
            if nodo.value == infoNodo:
                if nodo.next != None:
                    adj.append(nodo.next.value)
                if nodo.before != None:
                    adj.append(nodo.before.value)
                break
            nodo = nodo.next
        return adj

class listaEnlazada():
    def __init__(self, type):
        if type == 1: 
            self.estructura = listaEnlazadaSencilla()
        elif type == 2:
            self.estructura = listaEnlazadaDoble()
    def addNode_byValue(self, infoNodo):
        self.estructura.addNode_byValue(infoNodo)
    def deleteNode_byValue(self, infoNodo):
        return self.estructura.deleteNode_byValue(infoNodo)
    def getNodeValues(self):
        return self.estructura.getNodeValues()
    def isNodeValue(self, infoNodo):
        return self.estructura.isNodeValue(infoNodo)
    def findAdjacentNode(self, infoNodo):
        return self.estructura.findAdjacentNode(infoNodo)
    