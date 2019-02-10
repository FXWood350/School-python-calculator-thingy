import math

def add (x , y):
    return (str(x) + " + " + str(y) + " = " + str(x+y))

def subtract (x , y):
    return (str(x) + "-" + str(y) + " = " + str(x-y))

def multiply (x , y):
    return (str(x) + "*" + str(y) + " = " + str(x*y))

def divide (x , y):
    return (str(x) + "/" + str(y) + " = " + str(x/y))

def exponent (x , y):
    return (str(x) + "**" + str(y) + " = " + str(x**y))

def longexponent (x,y):
    answer = int
    answer = 1
    for _ in range (y):
        answer = answer*x
    return (str(x) + "**" + str(y) + " = " + str(answer))

def squareroot (x):
    return ("√ " + str(x) + " = " + str(math.sqrt(x)))

def cosine (x):
    return ("Cos(" + str(x) + ") = " + str(math.cos(x)))

def sine (x):
    return ("Sin(" + str(x) + ") = " + str(math.sin(x)))

def tangent (x):
    return ("Tan(" + str(x) + ") = " + str(math.tan(x)))

def invcosine (x):
    return math.acos(x)

def invsine (x):
    return math.asin(x)

def invtangent (x):
    return math.atan(x)

def opselect (x):
  for option in x:
    print (option,x[option])
  selection = input ("Enter Choice: ")
  if int(selection) in x.keys():
   return selection