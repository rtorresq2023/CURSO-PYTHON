lista=[]
archivo=open("C:/Users/usuario/Downloads/devices.txt")
for item in archivo:
       item=item.strip()
       lista.append(item) 
       print(item)
archivo.close()
print(lista)


             
