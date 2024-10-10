'''
Programa que calcule el area y el perimetro de un rectangulo apartir de su base y su altura
Entradas:
    base: integer
    altura: integer
Salidas:
   perimetro: integer
   area: integer
Analisis
   Se requiere calcular con las formulas para area y perimetro 
'''
base = input("Escribe la base del rectangulo: ")
base = int(base)
altura = input("Escribe la altura del rectangulo: ")
altura = int(altura)
print("programa que calcula area y perimetro de un rectangulo")
area = base * altura
perimetro = base + base + altura + altura
perimetro = (base + altura) * 2
print("El area del rectangulo es ", + str(area))
print("El perimetro del rectangulo es ", perimetro)

