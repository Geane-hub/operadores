nombreProducto=input("Ingrese el nombre del producto: ")
precioProducto=input("Ingrese el precio de un producto: ")
precioReal=float(precioProducto)
cantidad=input("Ingrese la cantidad de productos que lleva: ")
venta=int(cantidad)
total=precioReal*venta
print(f"El usuario ingresa {nombreProducto}, luego ingresa {precioReal} y luego ingresa {venta}")
print(f"El valor de {venta} {nombreProducto} es de {total}")