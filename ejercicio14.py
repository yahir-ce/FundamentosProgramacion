'''
Dado un n umero nde dos cifras diseñe un algoritmo que permita obtener el numero invertido.

'''
numero = int(input("Introduce un numero de dos cifras: "))
decenas = numero // 10
unidades = numero % 10
numero_invertido = unidades * 10 + decenas
print("El numero invertido de numero es: numero_invertido")
