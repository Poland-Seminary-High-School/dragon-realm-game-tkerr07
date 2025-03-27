import random
import time

def displayintro():
    print("you are in a land full od dragons. in front of you,"
    "you see two caves \n"
    "In once cave the dragon is friendly\n "
    "and will shaew his treasure with you. The other dragon is greedy and hungry\n,"
    "and will eat you on sight ")

    print()

def choosecave():
    cave = ''
    while cave != '1' and cave != '2':

     print("whart cave would you like to enter?")
     cave = input()

     return cave
    
def checkcave(chosencave):
   print("you approch the cave...")
   time.sleep(2)
   print("its dark and spooky...")
   time.sleep(2)
   print("A large dragoon jumps out in front of you! he opens his jaes and....")
   time.sleep(2)

   friendlycave = random.randint(1, 2)

   if choosecave == str(friendlycave):
        print("the dragoon gives you TREASURE")
   else:
         print("you got swallowed whole")


playagain = "yes"
while playagain == "yes" or playagain == "y":
   displayintro()
   cavenumber = choosecave()
   checkcave(cavenumber)

   print("do you want to play again? (yes or no)")
   playagain = input


