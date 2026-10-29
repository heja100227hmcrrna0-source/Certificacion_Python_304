carrito=[]
n_productos=int(input("Ingresa el numero de los productos"))
for i in range(n_productos):
    producto=input("Ingresa el producto a tu carrito")
    carrito.append(producto)
    print("Lista creada  corectamente")
    carrito[0]="barritas"
    print(carrito[0])
    print(carrito[1])
    print(carrito)