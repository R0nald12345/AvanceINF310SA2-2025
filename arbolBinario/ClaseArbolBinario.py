from ClaseNodo import ClaseNodo

class ArbolBinario:

    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        self.raiz = self._insertarRecursivo(self.raiz, valor)

    def _insertarRecursivo(self, raizAux, valor):
        if raizAux is None:
            return ClaseNodo(valor)
        else:
            if valor < raizAux.getValor():
                raizAux.setHijoIzquierdo(self._insertarRecursivo(raizAux.getHijoIzquierdo(), valor))
            else:
                raizAux.setHijoDerecho(self._insertarRecursivo(raizAux.getHijoDerecho(), valor))
            return raizAux

    def contarNodos(self):
        return self._contarNodosRecursivo(self.raiz)

    def _contarNodosRecursivo(self, raizAux):
        if raizAux is None:
            return 0
        return 1 + self._contarNodosRecursivo(raizAux.getHijoIzquierdo()) + self._contarNodosRecursivo(raizAux.getHijoDerecho())

    def isVacio(self):
        return self.raiz is None

    def eliminar(self, x):
        self.raiz = self.__eliminarRecursivo(self.raiz, x)

    def __eliminarRecursivo(self, nodoRaiz, x):
        if nodoRaiz is None:
            return None
        if x == nodoRaiz.getValor():
            return self.eliminarNodo(nodoRaiz)
        if x < nodoRaiz.getValor():
            nodoRaiz.setHijoIzquierdo(self.__eliminarRecursivo(nodoRaiz.getHijoIzquierdo(), x))
        else:
            nodoRaiz.setHijoDerecho(self.__eliminarRecursivo(nodoRaiz.getHijoDerecho(), x))
        return nodoRaiz

    def eliminarNodo(self, nodo):
        if nodo.verificarRaiz():
            return None
        if nodo.getHijoIzquierdo() is None and nodo.getHijoDerecho() is not None:
            return nodo.getHijoDerecho()
        if nodo.getHijoIzquierdo() is not None and nodo.getHijoDerecho() is None:
            return nodo.getHijoIzquierdo()
        nodoVerdeDato = self.__buscarSiguienteSucesor(nodo.getHijoDerecho())
        nodo.setValor(nodoVerdeDato)
        nodo.setHijoDerecho(self.__eliminarRecursivo(nodo.getHijoDerecho(), nodoVerdeDato))
        return nodo

    def __buscarSiguienteSucesor(self, nodoDerecho):
        while nodoDerecho.getHijoIzquierdo() is not None:
            nodoDerecho = nodoDerecho.getHijoIzquierdo()
        return nodoDerecho.getValor()

if __name__ == "__main__":
    arbol1 = ArbolBinario()
    arbol1.insertar(100)
    arbol1.insertar(90)
    arbol1.insertar(120)
    arbol1.insertar(70)
    arbol1.insertar(75)
    arbol1.insertar(130)
    arbol1.insertar(200)
    print("Cantidad de nodos:", arbol1.contarNodos())