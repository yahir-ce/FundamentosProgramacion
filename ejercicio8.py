'''
Un vendedor recibe un sueldo base mas un 10% extra por comision de sus ventas, el vendedor desea saber 
cuanto dinero obtendra por concepto de comisiones por las tres ventas que realiza en el mes y el total
que recibira en el mes tomando en cuenta su sueldo base y comisiones.

'''
sueldo_base = float(input("Introduce el sueldo base del vendedor: "))
venta1 = input("Ingresa la venta 1: ")
venta1 = int(venta1)
venta2 = input("Ingresa la venta 2: ")
venta2 = int(venta2)
venta3 = input("Ingresa la venta 3: ")
venta3= int(venta3)

total_ventas = venta1 + venta2 + venta3
comisiones = total_ventas * 0.10
sueldo_total = sueldo_base + comisiones

print("total de ventas: total de ventas: ")
print("Comisiones (10%): comisiones. ")
print("Sueldo total del vendedor: sueldo total: ")
