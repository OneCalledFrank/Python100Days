#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇


# Primero dejo todos los inputs en el tipo de dato que necesito.
# En este caso son int y float.
print("Bienvenido a la calculadora de propinas!")
total = input("¿Cuánto fue el total de la cuenta?\n $")
porcentaje = input(
    "¿Cuál es el porcentaje de propina que desea dar? 10, 12 o 15%\n")
personas = input("¿Cuántas personas pagarán la propina?\n")



total_float = float(total)
porcentaje_float = float(porcentaje)
personas_int = int(personas)

# Luego se divide el total de la cuenta por las personas
# Tambien se saca el porcentaje, que se divide por 100 para que
# quede en decimal y se le suma 1. Quedando 1.10 - 1.12 - 1.15 
# Luego se multiplica y te da el respultado con 2 decimales
# Por eso se le coloca el ":.2f" 
resultado = (total_float / personas_int) * ((porcentaje_float / 100) + 1)

print(f"Cada persona deberá pagar: ${resultado: .2f}")
print("Gracias por usar la calculadora de propinas!")
print("Hasta luego.")
