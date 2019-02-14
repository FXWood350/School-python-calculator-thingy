import time
import sys
import math
from calcfunctions import * #Imports functions used in calculator
invalidChoice = False # Default to valid choice

optype = {
  1 : "Arithmetic",
  2 : "Exponential",
  3 : "Trigonometric",
  4 : "Inverse Trigonometric",
}
#Optiontype
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
#submenus of optype/inv functions removed- see below comments

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

if invalidChoice:
  print()
  print ("Invalid Choice")
  sys.exit()

num2 = -1 # default value - to avoid error later.
num1 = int (input("Enter first number:  "))

if 1 <= int(choice) <= 6:
  num2 = int (input("Enter second number:  "))
 

#TODO investigate if myfunc definition calls all methods or not
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
#Temporarily removed- see below comment
}
#Just print the answer
print("The Answer is :", myfunc[choice])

#TODO investigate if you can use print() in the dictionary
myoutput = {
'1' : (str(num1) + " + " + str(num2) + " = " + str(add(num1,num2))),
'2' : (str(num1) + "-" + str(num2) + " = " + str(subtract(num1,num2))),
'3' : (str(num1) + "*" + str(num2) + " = " + str(multiply(num1,num2))),
'4' : (str(num1) + "/" + str(num2) + " = " + str(divide(num1,num2))),
'5' : (str(num1) + "**" + str(num2) + " = " + str(exponent(num1,num2))),
'6' : (str(num1) + "**" + str(num2) + " = " + str(longexponent(num1,num2))),
'7' : ("√ " + str(num1) + " = " + str(squareroot(num1))),
'8' : ("sin(" + str(num1) + ") = " + str(sine(num1))),
'9' : ("cos(" + str(num1) + ") = " + str(cosine(num1))),
'10' : ("tan(" + str(num1) + ") = " + str(tangent(num1))),
'11' : ("invsin(" + str(num1) +") =" + str(invsine(num1))),
'12' : ("invcos(" + str(num1) +") =" + str(invcosine(num1))),
'13' : ("invtan(" + str(num1) +") =" + str(invtangent(num1))),
#Above functions removed temporarily due to issues with large numbers
}

#Then print the equation and answer
print("The Ouput is :", myoutput[choice])
