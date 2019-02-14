import math

def add (x , y):
    return x + y
def subtract (x , y):
    return x - y
def multiply (x , y):
    return x * y
def divide (x , y):
    return x / y
def exponent (x , y):
    return x ** y
def longexponent (x,y):
    answer = int
    answer = 1
    for _ in range (y):
        answer = answer*x
    return answer
def squareroot (x):
    return math.sqrt( x )
def cosine (x):
    return math.cos(x)
def sine (x):
    return math.sin(x)
def tangent (x):
    return math.tan(x)
def invcosine (x):
  try:
   return math.acos(x)
  except:
    print ("\n")
def invsine (x):
  try:
   return math.asin(x)
  except:
    print ("\n")
def invtangent (x):
  try:
   return math.atan(x)
  except:
    print ("\n")

def opselect (x):
  for option in x:
    print (option,x[option])
  selection = input ("Enter Choice: ")
  if int(selection) in x.keys():
   return selection