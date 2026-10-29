tabla=[
    ["Nombre","Edad","Calificación"],
    ["Angel",16,9.0],
    ["Joshua",16,9.0],
    ["Danna",16,9.0],
    ["Jorge",16,3.0],
    ["Alma",16,7.0],
    ["Santiago",17,9.0],
    ["Angela",16,7.0],
    ["Fatima",16,7.0],
    ["Aaron",17,4.0]
]
nombre = input("Introduce un nombre")
filas = len(tabla)
columnas = len(tabla[0])
for i in range(filas):
    for j in range(columnas):
        if tabla[i][j] == nombre:
            print(f"Nombre encontrado en la posición [{i}][{j}]")
            print(f"Edad {tabla[i][j]}")
            print(f"Calificación {tabla[i][j]}")
            