""" 
a = 5
a = "Hello, World!" # može i s jednostrukim navodnicima
print(a) # Hello, World!



print("Hello world")

"""
"""
a = 5 
b = 10 

print(a + b)  # Zbrajanje
print(a - b)  # Oduzimanje  
print(a * b)  # Množenje
print(a / b)  # Dijeljenje
print(a // b) # Cjelobrojno dijeljenje
print(a % b)  # Modulo
print(a ** b) # Stepenovanje

"""

"""

print("ovo je moj prvi kalkusulator u pythonu")


print("Unesite prvi broj: ")
a = int(input())

print("Unesite drugi broj: ")
b = int(input())

print("Unesite operator:")
operator = input()

match operator:
    case "+":
        print(a+b)
    case "-":
        print(a-b)
    case "*":
        print(a*b)
    case "/":
        print(a/b)
    case _ : 
        print("unjeli ste krivu oznaku, promjenite ju!")

"""
"""

print("program za provjeravanje prjestupne godine")

print("unesite godinu:")
a = int(input())

if (a % 4 == 0 and a % 100 != 0 ) or (a % 400 == 0):
    print("godina ",  a , " je pristupna" )
else : 
    print("godina", a , "nije prijestupna ")


"""

import random

print("pogodite broj o d 1 do 100: ")

print("unesite jedan broj: ")

a = int(input())

broj = random.randint(1,100)

while a != broj:
    print("ponovno unesite broj vas broj nije tocan")

    if (a < broj):
        print("unjeli ste previse mali broj ")
    elif (a > broj):
        print("Unjeli set pre veliki broj ")

    a = int(input())

print("pogodili ste broj")





