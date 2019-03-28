def dividir(dividiendo, divisor):
    cociente = 0
    while dividiendo >= divisor:
        dividiendo -= divisor
        cociente += 1
    print("Cociente: ", cociente, "Residuo: ", dividiendo)
    main()

def probarDivisiones():
    dividir(15, 6)
    dividir(4, 6)
    dividir(500, 21)
    dividir(151, 32)
    dividir(1024, 8)

def encontrarMayor():
    Mayor = 0
    print("Teclea una serie de numeros para encontrar el mayor.")
    numero = int(input("Teclea un número [-1 para salir]: "))
    if numero<0:
        print("No se encontró valor mayor.")
    elif numero != -1:
        while numero != -1:
            if numero >= Mayor:
                Mayor = numero
            numero = int(input("Teclea un número [-1 para salir]: "))
        print(Mayor, "es mayor.")
    main()



def main():
    print("Misión 07. Ciclos while")
    print("Autor: Ruth Salmun Nehmad")
    print("Matrícula: A01379037")
    print("1. Calcular divisiones")
    print("2.Encontrar el mayor")
    print("3. Salir")
    opcion = int(input("Teclea tu opción: "))
    while opcion != 3:
        if opcion == 1:
            dividiendo = int(input("Teclea el dividendo: "))
            divisor = int(input("Tecleo el divisor: "))
            dividir(dividiendo, divisor)

        elif opcion == 2:
            encontrarMayor()

        elif opcion < 0 or opcion > 3:
            print("Opción no disponible.")
            print("Misión 07. Ciclos while")
            print("Autor: Ruth Salmun Nehmad")
            print("Matrícula: A01379037")
            print("1. Calcular divisiones")
            print("2.Encontrar el mayor")
            print("3. Salir")
            opcion = int(input("Teclea tu opción: "))

    print("Adiós.")

main()
