promedio=float(input("ingresa tu promedio"))
# El numeo ingresado es 9
if promedio<=0:
    print("QUE VERGUENZA")
    print("Tu promedio no existe tiene que ser mayor que cero nadie saca  - calificación ¡¡PON ATENCIOn!!")

elif promedio<=5:
    print("Tu promedio es muy bajo")

elif promedio<=5  and promedio<=7:
    print("Tu promedio es bajo")

elif promedio>7 and promedio<=9:
    print("Tu promedio es bueno")

elif promedio>9 and promedio<=10:
    print("Tu promedio es exelente")
    
else:
    print("Ese promedio no existe")