# Declarando una Lista
try:
   materias=["Programación", "Filosofia", "Matemáticas", "Ingles"]
   print(materias[0])
   materias.append("Lengua y comunicación")
   print(materias)
   materias[1]="Biologia"
   print(materias)
   materias.remove("Matemáticas")
   print(materias)
except IndexError:
    print("Indice correcto")
