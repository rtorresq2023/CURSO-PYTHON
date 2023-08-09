archivo=open("C:/Users/usuario/Downloads/devices.txt", 'w') 
while True:
    nuevoDispositivo=input("ingrese la palabra")
    if nuevoDispositivo=="exit":
        print("esta hecho")
        break
    archivo.write(nuevoDispositivo+"\n")
    print(nuevoDispositivo)
archivo.close()
