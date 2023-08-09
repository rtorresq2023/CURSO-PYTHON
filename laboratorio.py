# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 20:18:14 2023

@author: usuario
"""

def validarNumero(prompt, min, max):
    while (True):
        try:
            print("Ingrese un valor entre ",min," y ",max)
            x = int(input(prompt))
            assert x >= min and x <= max
            return x

        except ValueError:

            print("Ingresar solo numeros")

        except:
            
            print("Error, el valor debe estar dentro del RANGO ")

v = validarNumero("Ingrese un valor en el rango:", -100, 100)

print("El número es:", v)
        

    