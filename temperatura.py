def convertir_temperatura():
    """Convierte temperaturas entre Celsius y Fahrenheit."""
    temp = input("Introduce la temperatura (ejemplo: 32C, 89F): ")
    if temp[-1].upper() == 'C':
        fahrenheit = (float(temp[:-1]) * 9/5) + 32
        print(f"{temp} es igual a {fahrenheit:.2f}F")
    elif temp[-1].upper() == 'F':
        celsius = (float(temp[:-1]) - 32) * 5/9
        print(f"{temp} es igual a {celsius:.2f}C")
    else:
        print("Formato no reconocido. Por favor, usa el formato correcto (ejemplo: 32C, 89F).")

# Para probar la función, simplemente llama a convertir_temperatura()
convertir_temperatura()
