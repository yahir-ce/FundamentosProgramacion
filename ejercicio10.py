'''
Un alumno desea saber cual es su calificacion final en la materia de Algoritmos, dicha calificacion se compone de los siguientes porcentajes
· 55% del promedio de sus tre calificaciones parciales
· 30% de la calificacion del examen final
· 15% de la calificacion de un trabajo final

'''
calificacion1 = float(input("Introduce la primera calificacion parcial: "))
calificacion2 = float(input("Introduce la segunda calificacion parcial: "))
calificacion3 = float(input("Introdice la tercera calificacion parcial: "))

promedio_parciales = (calificacion1 + calificacion2 + calificacion3) / 3

calificacion_examen_final = float(input("Introduce la calificacion del examen final: "))
calificacion_trabajo_final = float(input("Introduce la calificacion del trabajo final: "))
calificacion_final1 = (promedio_parciales * 0.55) + (calificacion_examen_final * 0.30) + (calificacion_trabajo_final * 0.15)

print("la calificacion final en la materia de algoritmos es : calificacion_final: ")

                       