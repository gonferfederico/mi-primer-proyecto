def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def mostrar_menu():
    print("\n--- CONVERSOR DE TEMPERATURA ---")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    print("3. Salir")

if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-3): ")

        if opcion == '1':
            c = float(input("Ingresa grados Celsius: "))
            print(f"{c}°C equivalen a {celsius_a_fahrenheit(c):.2f}°F")
        elif opcion == '2':
            f = float(input("Ingresa grados Fahrenheit: "))
            print(f"{f}°F equivalen a {fahrenheit_a_celsius(f):.2f}°C")
        elif opcion == '3':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")
