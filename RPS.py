from random import randint
import time

l = ["rock", "paper", "scissor"]

cmptr = l[randint(0,2)]

Usrnm = input("Please Enter Your Name! ")

print("Hey!", Usrnm, "Welcome")
time.sleep(2)
print("The Game is between You and Bot\nThere will be 11 turns\nOne thing to mention is that for your ease press:")
time.sleep(8)
print("R for Rock\nP for Paper\nS for Scissor")


usrpnt = 0
cmptrpnt = 0
for n in range(1,11):
  User = input("Enter Your Choice!")
  if User == cmptr:
    print("Oops! Tied")

  elif User == "R":
      if cmptr == "P":
         cmptrpnt +=1
      else:
          usrpnt +=1
  elif User == "P":
      if cmptr == "R":
          usrpnt +=1
      else:
          cmptrpnt +=1
  elif User == "S":
      if cmptr == "P":
          usrpnt +=1
      else:
          cmptrpnt +=1
  else:
      print("Please Enter a valid Choice...!")

  print(11 - n, "turns left")
  print("Score:")
  print(Usrnm, ":", usrpnt)
  print("Bot :", cmptrpnt)

if usrpnt > cmptrpnt:
    print("Hurray!", Usrnm," You Won...!")
elif usrpnt == cmptrpnt:
    print("That was close...\nMatch tied...!")
else:
    print("Better luck next time...!")











