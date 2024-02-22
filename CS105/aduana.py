class Articulo:
    def __init__ (self, nombre, codigo, descripcion):
        self.nombre = nombre
        self.codigo = int(codigo)
        self.descripcion = descripcion
    
    def __str__(self):
        return f"'{self.nombre}'"

class Contenedor:
    def __init__(self, identificador, tamanio):
        self.identificador = identificador
        self.tamanio = tamanio
        self.articulos = []

    def agregar_articulo(self, articulo):
        self.articulos.append(articulo)  

    def imprimir_articulos(self):
        if not self.articulos:  # Verifica si la lista de artículos está vacía
            print("El contenedor está vacío.")
        else:
            for articulo in self.articulos:  # Itera sobre cada artículo en la lista
                print(articulo)  # Imprime los detalles del artículo

class Transporte:
    def __init__(self, nombre, cedulaJuridica):
        self.nombre = nombre
        self.cedulaJuridica = cedulaJuridica
        self.contenedores = []
    
    def agregar_contenedor(self, contenedor):
        self.contenedores.append(contenedor)

    def imprimir_articulos_en_transporte(self):
        if not self.contenedores:
            print("El transporte no tiene contenedores.")
        else:
            print(f"Artículos en el transporte {self.nombre}:")
            for contenedor in self.contenedores:
                print(f"Contenedor {contenedor.identificador}:")
                contenedor.imprimir_articulos()
                print()  # Agrega una línea en blanco entre los contenedores

contenedor = Contenedor("C1234", 20)

# Creando instancias de Articulo
articulo1 = Articulo("Papa", 22323, "Siuu")
articulo2 = Articulo("Tomate", 11223, "Verduras")

# Agregando artículos al contenedor
contenedor.agregar_articulo(articulo1)
contenedor.agregar_articulo(articulo2)

contenedor.imprimir_articulos()

transporte = Transporte("Barco", "9232dasda")
transporte.agregar_contenedor(contenedor)
transporte.imprimir_articulos_en_transporte()