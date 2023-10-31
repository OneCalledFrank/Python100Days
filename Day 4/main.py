import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

opcion = int(input("Escribe 0 para Piedra, 1 para Papel o 2 para Tijeras:\n"))

if opcion == 0:
    print("Escogiste roca.")
    print(rock)
elif opcion == 1:
    print("Escogiste papel")
    print(paper)
elif opcion == 2:
    print("Escogiste tijeras")
    print(scissors)

computadora = random.randint(0, 2)

if computadora == 0:
    print("La computadora escogió roca.")
    print(rock)
elif computadora == 1:
    print("La computadora escogió papel")
    print(paper)
elif computadora == 2:
    print("La computadora escogió tijeras")
    print(scissors)


if computadora == 0 and opcion == 1:
    print("Papel vence a la Roca.\nGanaste!")
elif computadora == 0 and opcion == 2:
    print("Roca vence a las Tijeras.\nPerdiste :(")
elif computadora == 1 and opcion == 0:
    print("Papel vence a la Roca.\nPerdiste :(")
elif computadora == 1 and opcion == 2:
    print("Tijeras vence al Papel.\nGanaste!")
elif computadora == 2 and opcion == 0:
    print("Roca vence a las Tijeras.\nGanaste!")
elif computadora == 2 and opcion == 1:
    print("Tijeras vence al Papel.\nPerdiste :(")
else:
    print("Empate!")
