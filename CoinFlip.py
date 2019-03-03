from random import randint
import sys
import msvcrt as m

HeadsCount = int(0)
TailsCount = int(0)
ActualIterations = int(0)

def FlipCoin (y):
 global HeadsCount
 global TailsCount
 global ActualIterations
 for x in range(0,y):
        CoinVal = randint(1,2)
        if CoinVal ==1 :
                print("Heads")
                HeadsCount = HeadsCount + 1
        elif CoinVal ==2 :
                print("Tails")
                TailsCount = TailsCount + 1
        print("Press a key to flip again (x to exit)")
        key = m.getch()
        if str(key) == "b'x'":
              break  
        ActualIterations = ActualIterations +1

while True: 
   coinFlipCount = int(input("How many times do you wish to run the Coin Flipper?"))
   if coinFlipCount<= 50:
           break
   print("Try again ye daftie")

FlipCoin(coinFlipCount)
print("We flipped %d times, and got %d heads and %d tails, and the probability of flipping heads is %.10f which is %.1f per cent off normal" % (ActualIterations,HeadsCount,TailsCount,HeadsCount/coinFlipCount, HeadsCount/coinFlipCount*100-50))
