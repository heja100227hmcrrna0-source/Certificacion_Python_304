# Creando una dupla
coordenadas=(10.5, 20.3, 30.5, 10.5) # Tupla numerica
nombres=("Luis","Ana","Yo") # Dupla de cadena de texto
# coordenadas[0]=10.9  <--- no se puede hacer
for indice, coordenada in enumerate(coordenadas):
  print(f" -Indice- [{indice}] -coordenada- [{coordenada}]")
