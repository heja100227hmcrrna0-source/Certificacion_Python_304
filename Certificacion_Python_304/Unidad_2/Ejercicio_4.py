# El mapa del tesoro
mapa=[
    [".",".",".","."],
    [".",".","X","."], 
    [".",".",".","."],
    [".",".",".","."] 
]
filas=len(mapa)
columnas=len(mapa)
# Recoriendo la matriz con ciclos anidados
# Ciclo externo para manejar filas(i
for i in range(filas):
    for j in range(columnas):
        # Verificamos si encontramos el tesoro
        if mapa[i][j]=="X":
            print(f"Mapa encontrado en la posición [{i}][{j}]")