letras=[
    ["A", "B", "C", "D", "E"],
    ["F", "G", "H", "I", "J"],
    ["K", "L", "M", "Ñ", "O"],
    ["P", "Q", "R", "S", "T"],
    ["U", "V", "W", "X", "Y"],
    ["Z", "",  "",  "", "", ] 
]  
filas=len(letras)
columnas=len(letras[0])
for i in range(0,6):
    for j in range(0,5):
        print(f"[{i}] [{j}] = {letras[i][j]}")