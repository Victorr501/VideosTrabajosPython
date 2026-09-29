class Producto:
    def __init__(self, nombre, precio, cantidad):
        if not nombre or not nombre.strip():
            raise ValueError("Error: El nombre del preoducto no puede ser vacío")
        if precio < 0:
            raise ValueError("Error: El precio no puede ser inferior a 0")
        if cantidad < 0:
            raise ValueError("Error: La cantidad no puede ser inferior a 0")
        
        
        self.nombre = nombre.strip()
        self.precio = float(precio)
        self.cantidad = int(cantidad)
        
    def actualizar_precio(self, nuevo_precio):
        if nuevo_precio <= 0:
            raise ValueError("Error: El precio tiene que ser mayor a 0")
        self.precio = float(nuevo_precio)
        
    def actualizar_cantidad(self, nueva_cantidad):
        if nueva_cantidad <= 0:
            raise ValueError("Error: El precio tiene que ser mayor a 0")
        self.cantidad = int(nueva_cantidad)
        
    def calcular_valor_total(self) -> float:
        return self.cantidad * self.precio
    
    def __str__(self):
        return f"Producto: {self.nombre} | Precio: ${self.precio:.2f} | Cantidad: {self.cantidad} | Total: {self.calcular_valor_total():.2f}"
    
class Inventario:
    def __init__(self):
        self.lista = []
    
    def agregar_producto(self ,producto):
        """
        Esto agrega productos
        """
        self.lista.append(producto)
        
    def buscar_producto(self, nombre):
        for prod in self.lista:
            if prod.nombre.lower() == nombre.strip().lower():
                return prod
        return None
    
    def calcular_valor_inventario(self):
        total = 0
        for prod in self.lista:
            total += prod.calcular_valor_total()
        return total    
    
    def listar_productos(self):
        if len(self.lista) == 0:
            print("El inventario estaá vació")
            return
        
        print("\n LISTA DE PRODUCTOS EN INVENTARIO ")
        for prod in self.lista:
            print(prod)
        print("====================================")
        
def menu_principal():
    mi_invetario = Inventario()
    
    while True:
        print("\n --- MENÚ DEL SISTEMA DE INVENTARIO ---")
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Listar productos")
        print("4. Calcular valor total del inventario")
        print("5. Salir")
        
        opcion = int(input("Selecciona una opción (1-5)"))
        
        match opcion:
            case 1:
                try:
                    nombre = input("Introduce el nombre del producto: ")
                    precio = float(input("Introduce el precio (ej: 15.50): "))
                    cantidad = int(input("Introduce la cantidad (número entero):"))
                    
                    nuevo_producto = Producto(nombre, precio, cantidad)
                    
                    mi_invetario.agregar_producto(nuevo_producto)
                    print(f"¡Éxito! Producto '{nombre}' agregado correctamente. ")

                except ValueError as e:
                    print(f"\n[ERROR] Entrada inválida: {e}")
                    print("Asegúrate  de introducir número carrectos y que no sean negativos")
            case 2:
                nombre_buscar = input("Introduce el nombre del producto a buscar: ")
                producto_encontrado = mi_invetario.buscar_producto(nombre_buscar)
                
                if producto_encontrado:
                    print("\n Producto encontrado:")
                    print(producto_encontrado)
                else:
                    print(f"\n No se encontró ningún producto con el nombre `{nombre_buscar}.")
            case 3:
                mi_invetario.listar_productos()
            case 4:
                print(f"\nEl valor toal de todo el inventario es: ${mi_invetario.calcular_valor_inventario():.2f}")
            case 5:
                print("\nSaliendo del programa... ¡Hasta pronto!")
                break
            case _:
                print("\n[!] Opción no válida. Por favor, elige un número del 1 al 5.")
                
if __name__ == "__main__":
    menu_principal()

    