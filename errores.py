try:
   x=int(input("enter a number:"))
   y=1/x
   print(y)
except ZeroDivisionError:
        print("you cannot divide vy zero, sorry")
except ValueError:
        print("you cannot divide vy zero, sorry")

except:
        print("algo salio mal,hay un error")
print("fin")
