try:
   y=1/0
except ZeroDivisionError:
    print("Divicion para zero")
except ArithmeticError:
    print("problema aritmetico")
except:
    print("error")
print("fin")
