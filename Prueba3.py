def validar_precio(precio):
    if not isinstance(precio, (int, float)):
        raise TypeError("El precio debe ser un número.")
    if precio <= 0:
        raise ValueError("El precio debe ser mayor que cero.")


def validar_stock(cantidad):
    if not isinstance(cantidad, int):
        raise TypeError("La cantidad debe ser un número entero.")
    if cantidad < 0:
        raise ValueError("La cantidad no puede ser negativa.")


def registrar_producto(nombre, precio, stock):
    try:
        validar_precio(precio)
        validar_stock(stock)
        return {"nombre": nombre, "precio": precio, "stock": stock}
    except ValueError as e:
        print(f"Error de valor: {e}")
        return None
    except TypeError as e:
        print(f"Error de tipo: {e}")
        return None


def mostrar_inventario(inventario):
    if not inventario:
        print("El inventario está vacío.")
        return
    print("\nINVENTARIO")
    print("-" * 40)
    for i, producto in enumerate(inventario, 1):
        print(f"{i}. Nombre: {producto['nombre']} | Precio: ${producto['precio']:.2f} | Stock: {producto['stock']}")
    print("-" * 40)


inventario = []

while True:
    print("\n--- Registrar nuevo producto ---")
    nombre = input("Nombre del producto: ")

    try:
        precio = float(input("Precio del producto: "))
    except ValueError:
        print("Error: ingresa un número válido para el precio.")
        continue

    try:
        stock = int(input("Cantidad en stock: "))
    except ValueError:
        print("Error: ingresa un número entero para el stock.")
        continue

    producto = registrar_producto(nombre, precio, stock)
    if producto:
        inventario.append(producto)
        print(f"Producto '{nombre}' registrado correctamente.")

    mostrar_inventario(inventario)

    salir = input("\n¿Deseas agregar otro producto? (s/n): ").strip().lower()
    if salir == "n":
        print("Saliendo del sistema.")
        break