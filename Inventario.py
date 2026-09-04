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