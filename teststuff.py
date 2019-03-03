#OptionMenu
#select 1- this allows you to calculate distance (speedxTime)
#select 2- this allows you to calculate speed (distance/time)

def distanceCalculate (s,t):
    d = s*t
    return d

def speedCalculate (d,t):
    s = d/t
    return s




print ("Select operation type: Enter 1 for distance or 2 for speed")
choice = int(input("Input thing: "))

if choice == 1:
    speed = int(input("Please input speed: "))
    time = int(input( "please input time: "))
    print (distanceCalculate(speed,time))
elif choice == 2:
    distance = int(input("Please input distance: "))
    time = int(input("Please input time: "))
    print (speedCalculate(distance,time))