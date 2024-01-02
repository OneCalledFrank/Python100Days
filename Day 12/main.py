# Number Guessing Game Objectives:
from art import logo
import random

numero = random.randint(1, 100)
vidas = 0
adivina = 0
print(f"Psst, la respuesta es {numero}")
print(logo)

print("Bienvenido al juego de la adivinanza.")
text = input("Escoge la dificultad, facil o dificil:\n")

if text == "facil":
    vidas = 10
else:
    vidas = 5

print(f"Tienes {vidas} vidas")

while vidas >= 1:
    adivina = int(input("Escoge un número del 1 al 100:\n"))
    if numero > adivina:
        print("Muy bajo")
        vidas -= 1
        print(f"Te quedan {vidas} vidas")
    elif numero < adivina:
        print("Muy alto")
        vidas -= 1
        print(f"Te quedan {vidas} vidas")
    else:
        print(f"Correcto, escogiste {adivina} y la respuesta era {numero}")
        vidas = -1

if vidas == 0:
    print(f"Perdiste, la respuesta era {numero}")
elif vidas == -1:
    print("Ganaste!")
