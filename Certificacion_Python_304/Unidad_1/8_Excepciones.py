#Ejercicio 1 sin manejo de excepciones
try:

   numero1=float(input("Ingresa el primer número"))
   numero2=float(input("Ingresa el segundo número"))  

   resultado=numero1/numero2
   print(resultado)

except ZeroDivisionError:
        print("Error: No se puede dividir una letra")

except ValueError:
        print("Error: No se puede dividir una letra")
