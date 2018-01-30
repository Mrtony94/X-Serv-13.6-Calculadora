#!/usr/bin/python3

import sys

len_P = len(sys.argv)
Function_P = {'suma', 'resta', 'mult', 'div'}

def comprobacion():
    if len_P != 4:
        sys.exit("Has cometido un error, vuelve a intentarlo")

def suma(num1,num2):
    print(num1, "+", num2, "=", num1 + num2)
def resta(num1,num2):
    print(num1, "-", num2, "=", num1 - num2)
def mult(num1,num2):
    print(num1, "*", num2, "=", num1 * num2)
def div(num1,num2):
    try:
        print(num1, "/", num2, "=", num1 / num2)
    except ZeroDivisionError:
        print ("\nNo se puede dividir entre cero :Sorry\n")

def operaciones(num1, num2):
    if Function_P == 'suma':
        return suma(num1, num2)
    if Function_P == 'resta':
        return resta(num1, num2)
    if Function_P == 'mult':
        return mult(num1, num2)
    if Function_P == 'div':
        return div(num1, num2)
Function_P = sys.argv[1]
num1 = float(sys.argv[2])
num2 = float(sys.argv[3])

comprobacion()
operaciones(num1,num2)
