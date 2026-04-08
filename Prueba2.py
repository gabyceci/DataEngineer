while True:
    print("\n=== CALCULADORA ===")
    print("Operaciones disponibles: suma, resta, multiplicacion, division")
    operacion = input("Elige una operacion (o escribe 'salir' para terminar): ").strip().lower()

    if operacion == "salir":
        print("¡Hasta luego!")
        break

    if operacion not in ["suma", "resta", "multiplicacion", "division"]:
        print("Operacion no válida. Intenta de nuevo.")
        continue

    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
    except ValueError:
        print("Por favor ingresa números válidos.")
        continue

    if operacion == "suma":
        resultado = num1 + num2
    elif operacion == "resta":
        resultado = num1 - num2
    elif operacion == "multiplicacion":
        resultado = num1 * num2
    elif operacion == "division":
        if num2 == 0:
            print("Error: No se puede dividir entre cero.")
            continue
        resultado = num1 / num2

    print(f"Resultado: {num1} {operacion} {num2} = {resultado}")