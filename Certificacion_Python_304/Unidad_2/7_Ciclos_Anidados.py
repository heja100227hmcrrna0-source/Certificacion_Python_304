# Ciclo externo para el comentario de la base de la tabla
for i in range(1,4):
    print(r"---Tabla del {i}---")
    # Ciclo inerno, multiplica la basa (i) por el numero (j)
    for j in range(1,11):
        print(f"{i} x {j} ={i*j}")
    print(f"AQUI TERMINA LA TABLA DEL {i}")
