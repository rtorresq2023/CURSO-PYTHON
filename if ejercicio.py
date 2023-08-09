acl=int (input("ingrese el de ACL: "))
if acl> 1 and acl<=199:
    print("es una acle estandar")
elif acl>=100 and acl<=199:
        print("es una acl extendida")
else:
        print ("el numero ingresado no es una acl")
