class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} - ${self.precio:,.0f}"


class Promocion:
    def __init__(self, nombre, productos_incluidos, precio_normal, precio_promocion):
        """
        productos_incluidos: lista de tuplas (Producto, cantidad)
        """
        self.nombre = nombre
        self.productos_incluidos = productos_incluidos
        self.precio_normal = precio_normal
        self.precio_promocion = precio_promocion

    def ahorro(self):
        return self.precio_normal - self.precio_promocion

    def __str__(self):
        detalle = ", ".join(
            f"{cantidad}x {producto.nombre}" for producto, cantidad in self.productos_incluidos
        )
        return (
            f"{self.nombre}\n"
            f"  Incluye: {detalle}\n"
            f"  Precio normal: ${self.precio_normal:,.0f}\n"
            f"  Precio promoción: ${self.precio_promocion:,.0f}\n"
            f"  Ahorro: ${self.ahorro():,.0f}"
        )
        
# PRODUCTOS
huevos = Producto("Huevos (cubeta x 30)", 18000)
leche = Producto("Leche (1 litro)", 4500)
pan_tajado = Producto("Pan tajado (500 g)", 6000)
cafe = Producto("Café (250 g)", 12000)
azucar = Producto("Azúcar (1 kg)", 5000)
chocolate = Producto("Chocolate en polvo (250 g)", 8000)
galletas = Producto("Galletas (paquete)", 3500)
queso = Producto("Queso (500 g)", 14000)
mantequilla = Producto("Mantequilla (250 g)", 7000)
arepas = Producto("Arepas (paquete x 10)", 9000)

productos = [
    huevos, leche, pan_tajado, cafe, azucar,
    chocolate, galletas, queso, mantequilla, arepas
]

# PROMOCIONES
desayuno_completo = Promocion(
    "DESAYUNO COMPLETO",
    [(huevos, 2), (arepas, 1), (leche, 1)],
    precio_normal=8100,
    precio_promocion=7000
)

cafe_con_pan = Promocion(
    "CAFÉ CON PAN",
    [(cafe, 1), (pan_tajado, 1)],
    precio_normal=18000,
    precio_promocion=16000
)

onces = Promocion(
    "ONCES",
    [(chocolate, 1), (galletas, 1), (leche, 1)],
    precio_normal=16000,
    precio_promocion=14000
)

promociones = [desayuno_completo, cafe_con_pan, onces]