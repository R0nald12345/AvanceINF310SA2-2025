class NodoMVias:

    def __init__(self, orden, clave_insertar=None):
        self.orden = orden
        self.lista_de_claves = [None] * (orden - 1)
        self.lista_de_hijos = [None] * orden
        if clave_insertar is not None:
            self.lista_de_claves[0] = clave_insertar

# getters y setters por poscion de clave e hijo
    
    def get_clave(self, posicion):
        return self.lista_de_claves[posicion]

    def get_hijo(self, posicion):
        return self.lista_de_hijos[posicion]

    def set_clave(self, posicion, clave):
        self.lista_de_claves[posicion] = clave 

    def set_hijo(self, posicion, hijo):
        self.lista_de_hijos[posicion] = hijo

    def es_hijo_vacio(self, posicion):
        return self.lista_de_hijos[posicion] is None

    def es_clave_vacia(self, posicion):
        return self.lista_de_claves[posicion] is None
    
    def estan_claves_llenas(self):
        return all(clave is not None for clave in self.lista_de_claves)
    
    def es_hoja(self):
        return all(hijo is None for hijo in self.lista_de_hijos)