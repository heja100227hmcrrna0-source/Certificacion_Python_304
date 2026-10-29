# Crear un diccionario
persona={
    "Nombre":"Jaramillo",
    "Edad":16,
    "Profesion":"Programador",
    "Estudiante":False
}
print(persona)
# Accedoiendo a un valor en especifico
print(persona["Edad"])
# Se puede usar el metodo get()
# Es util por que no marca error si nel valor no existe
print(persona.get("Nombre"))
# modificar un valor existentente
persona["Profesion"]
print(persona("Profesion"))
# Agregar un par clave(Clave:Valor)
persona["Ciudad"]="San pepe ranch"
# Recorrer un diccionario con un bucle