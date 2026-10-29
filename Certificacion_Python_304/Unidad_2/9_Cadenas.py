cadena1="Hola"
cadena2="Mundo"
Multilinea="""Esto es una cadena
de varias lineas"""
print(cadena1 + cadena2 + Multilinea) # print("f{caadena1}")
# Cadena y repetición
eco="ja" * 3
print(eco)
# Cambiar una cadena de miniscula a mayuscula
tu_nombre="Angel"
print(tu_nombre.upper())
# Cambier una cadena de mayuscula a minuscula
print(tu_nombre.lower())
# Remplazar de texto a una cadena
frase="Me gusta programacion"
print(frase.replace("programacion","filosofia"))
# formato de cadenas (F-Sring)
edad=16
Nombre="Angel"
mensaje=f"Hola, me llamo {Nombre} y tengo {edad} años"
print(mensaje)
# Contar los caracteres de una cadena
texto= " ¡ FELICIDADES ! por aun continuar en el ¡¡¡CECYCERRO!!!"
cantidad_caracteres=len(texto)
print(texto)
print(cantidad_caracteres)
# Coprobar si un texto contiene una palabra
oracion="Aprender python es divertido"
if " C++ " in oracion:
    print("Encontrado")
else:
    print(" ¡¡No esta!! ")
# Valiadr contenido de una cadena
Num_lista="14"
# print(Num_lista.is_integer())
print(Num_lista.isalpha())
print(Num_lista.isdigit())