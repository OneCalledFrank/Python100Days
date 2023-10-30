print('''
+-----------------------------------------------------------------------------+
| |       |\                                           -~ /     \  /          |
|~~__     | \                                         | \/       /\          /|
|    --   |  \                                        | / \    /    \     /   |
|      |~_|   \                                   \___|/    \/         /      |
|--__  |   -- |\________________________________/~~\~~|    /  \     /     \   |
|   |~~--__  |~_|____|____|____|____|____|____|/ /  \/|\ /      \/          \/|
|   |      |~--_|__|____|____|____|____|____|_/ /|    |/ \    /   \       /   |
|___|______|__|_||____|____|____|____|____|__[]/_|----|    \/       \  /      |
|  \mmmm :   | _|___|____|____|____|____|____|___|  /\|   /  \      /  \      |
|      B :_--~~ |_|____|____|____|____|____|____|  |  |\/      \ /        \   |
|  __--P :  |  /                                /  /  | \     /  \          /\|
|~~  |   :  | /                                 ~~~   |  \  /      \      /   |
|    |      |/                        .-.             |  /\          \  /     |
|    |      /                        |   |            |/   \          /\      |
|    |     /                        |     |            -_   \       /    \    |
+-----------------------------------------------------------------------------+
|          |  /|  |   |  2  3  4  | /~~~~~\ |       /|    |_| ....  ......... |
|          |  ~|~ | % |           | | ~J~ | |       ~|~ % |_| ....  ......... |
|   AMMO   |  HEALTH  |  5  6  7  |  \===/  |    ARMOR    |#| ....  ......... |
+-----------------------------------------------------------------------------+
''')
print("Bienvenido a DOOM - La aventura de texto - ")
print("Tu misión es llegar al final.") 

camino = input("¿Quieres ir a la derecha o a la izquierda?\n").lower()
if camino == "derecha":
  print("Has matado a los demonios.")
  print("Sigues avanzando.")
  ambiente = input("¿Quieres tomar la escopeta o ir por el arma de plasma?\n").lower()
  if ambiente == "arma de plasma":
    print("Puedes matar al barón del infierno.")
    print("Sigues avanzando.")
    llave = input("Hay tres puertas, ¿Cuál eliges? Roja, Amarilla o Azul\n").lower()
    if llave == "roja":
      print("La llave roja te lleva al infierno.")
      print("Game Over.")
    elif llave == "amarilla":
      print("Llegaste al final con poca vida, lograste completar DOOM, la aventura de texto")
      print("Felicidades.")
    else:
      print("Los demonios han entrado hasta tu casa por esa puerta.")
      print("Game Over.")
  else:
    print("Tomaste la escopeta, pero un barón del infierno te ha matado.")
    print("Game Over.")
else:
  print("Has caído en una trampa de demonios.")
  print("Game Over.")

