import sys
import math
from calcfunctions import * #Imports functions used in calculator
invalidChoice = False # Default to valid choice

optype = { #Optiontype
  1 : "Arithmetic",
  2 : "Exponential",
  3 : "Trigonometric",
  4 : "Inverse Trigonometric",
}

arithtype = {
    1 : "Add",
    2 : "Subtract",
    3 : "Multiply",
    4 : "Divide",
}
exptype = {
    5 : "Exponent",
    6 : "Long Exponent",
    7 : "Square Root",
}
trigtype = {
   8 : "Sine",
   9 : "Cosine",
   10 : "Tangent",
}
invtrigtype = {
  11 : "Inverse Sine",
  12 : "Inverse Cosine",
  13 : "Inverse Tangent"
}


print ("Select operation type:")
choice1 = opselect(optype)
print ("User Selected", choice1)
#Points to opselect function in calcfunctions, returns whichever optype selected by user as shown in dict optype


if choice1 == "1":
  choice = opselect(arithtype)
elif choice1 == "2":
  choice = opselect(exptype)
elif choice1 == "3":
  choice = opselect(trigtype)
elif choice1 == "4":
  choice = opselect(invtrigtype)
else:
  invalidChoice = True

if not choice or invalidChoice:
  print()
  print ("Invalid Choice")
  sys.exit()

num2 = -1 # default value - to avoid error later.
num1 = int (input("Enter first number:  "))

if 1 <= int(choice) <= 6:
  num2 = int (input("Enter second number:  "))
 

myfunc = {
'1' : add(num1,num2),
'2' : subtract(num1,num2),
'3' : multiply(num1,num2),
'4' : divide(num1,num2),
'5' : exponent(num1,num2),
'6' : longexponent(num1,num2),
'7' : squareroot(num1),
'8' : sine(num1),
'9' : cosine(num1),
'10' : tangent(num1),
'11' : invsine(num1),
'12' : invcosine(num1),
'13' : invtangent(num1)
}

print("The Answer is :", myfunc[choice])
