from art import logo

print(logo)
print("Bienvenido a la apuesta a ciegas.")

apostadores = {}
terminar_apuesta = False


def encontrar_max_apuesta(record_apuesta):
    max_apuesta = 0
    ganador = ""
    # el record de apuesta = el diccionario {"Franco", 123, "Pablo", 123}
    for apostador in record_apuesta:
        cantidad_apuesta = record_apuesta[apostador]
        if cantidad_apuesta > max_apuesta:
            max_apuesta = cantidad_apuesta
            ganador = apostador
    print(f"El ganador es {ganador} con una apuesta de ${max_apuesta}")


while not terminar_apuesta:
    nombre = input("Cual es tu nombre?\n")
    precio = int(input("Cual es tu apuesta?\n$"))
    apostadores[nombre] = precio
    seguir = input("Hay otros apostadores? Escribe 'si' o 'no'\n").lower()
    if seguir == "no":
        encontrar_max_apuesta(apostadores)
        terminar_apuesta = True
    elif seguir == "si":
        clear()
