# from replit import clear
from art import logo


def suma(n1, n2):
    return n1 + n2


def resta(n1, n2):
    return n1 - n2


def multi(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


operaciones = {
    "+": suma,
    "-": resta,
    "*": multi,
    "/": div
}


def calculator():
    print(logo)

    num1 = float(input("Cual es tu primer número?:\n"))
    for simbolo in operaciones:
        print(simbolo)
    debe_continuar = True

    while debe_continuar:
        operador = input("Escoge tu operador:\n")
        num2 = float(input("Cual es el siguiente número?:\n"))
        funcion_calcular = operaciones[operador]
        respuesta = funcion_calcular(num1, num2)
        print(f"{num1} {operador} {num2} = {respuesta}")

        if input(f"Escribe 'si' para continuar calculando con {respuesta}, o escribe 'no' para empezar una nueva operación: ") == 'si':
            num1 = respuesta
        else:
            debe_continuar = False
            # clear()
            calculator()


calculator()
