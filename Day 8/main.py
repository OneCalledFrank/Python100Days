from art import logo


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        # Se deja como char el caractér de el alfabeto para cuando uno ingrese un elemento
        # que no existe en el alfabeto, se mantenga. Como un espacio o un signo.
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here's the {cipher_direction}d result: {end_text}")


# Se importa el logo desde el módulo art.
print(logo)

# Se deja una variable en False, para que el ciclo se siga ejecutando
# Se hacen las mismas preguntas que son la dirección, o sea, encriptar o decifrar el código
# y luego cuantas letras se moverán, dependiendo de lo anterior
# Finalmente, si en la última pregunta para continuar se dice que 'no', se termina el programa.
# De otra manera, se sigue ejecutando.
should_end = False
while not should_end:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
# Se hace el módulo por 26 que son las letras del abecedario para que no se salga de la lista.
# Igual se mantiene dos alfabetos dentro de la primera lista 'alphabet'.
    shift = shift % 26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Adiós.")
