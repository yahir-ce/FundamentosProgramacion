'''
Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto
debera pagar finalmente por su compra

'''
total = float(input("Cual fue el total de la compra: "))
d = (total)*0.15
td = (total-d)
print("El total con el descuento es:", td)
