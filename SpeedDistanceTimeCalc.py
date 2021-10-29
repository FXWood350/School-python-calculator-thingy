import sys
def distanceCalc (x , y):
    return x*y
def speedCalc (x , y):
    return x/y
def timeCalc (x , y):
    return x/y
def calc_mins(x):
    x.strip(" ")
    if x.find("h")>0:
        formattedHours = x.strip("h")
        return float(formattedHours)
    elif x.find("m")>0:
        formattedMins = x.strip("m")
        return float(formattedMins)/60
    else:
        print("Dodgy time format")
        sys.exit(0)


print("Select Operation Type: /n Distance (1), Speed (2) or Time (3)")
Opselect = input ()
invalidChoice = False

if int(Opselect) == 1:
    speed = input("Input average speed in mph: ")
    time = input("Input travel time in mins or hrs e.g. 60m or 2h: ")
    print("The distance you travelled is: %.1f miles" % (distanceCalc(float(speed),calc_mins(time))))
elif int(Opselect) == 2:
    distance = input("Input miles to travel: ")
    time = input("Input timeframe in mins or hrs e.g. 60m or 2h: ")
    print("The speed you must travel to reach your destination in time is: %.1f mph" % speedCalc(float(distance),calc_mins(time)))
elif int(Opselect) == 3:
    distance = input("Input distance to travel in miles: ")
    speed = input("Input speed in mph: ")
    print("The time that the journey will take at current speeds is: %.2f hours" % timeCalc(float(distance),float(speed)))
else:
    invalidChoice = True

if invalidChoice:
    print ("Selection not valid")
