from random import randint
import time

l = ["rock", "paper", "scissor"]

Usrnm = input("Please Enter Your Name! ")

print("Hey!", Usrnm, "Welcome")
time.sleep(1)
print("The Game is between You and Bot\nThere will be 7 turns") # \nOne thing to mention is that for your ease press:
time.sleep(1)
#print("R for Rock\nP for Paper\nS for Scissor")


usrpnt = 0
cmptrpnt = 0
for n in range(1,8):
  cmptr = l[randint(0, 2)]
  #print(cmptr)
  User = str(input("Enter Your Choice!"))
  if User == cmptr:
    print("Oops! Tied")

  elif User == "rock":
      if cmptr == "paper":
         cmptrpnt +=1
      else:
          usrpnt +=1
  elif User == "paper":
      if cmptr == "rock":
          usrpnt +=1
      else:
          cmptrpnt +=1
  elif User == "scissor":
      if cmptr == "paper":
          usrpnt +=1
      else:
          cmptrpnt +=1
  else:
      print("Please Enter a valid Choice...!")

  print(7 - n, "turns left")
  print("Score:")
  print(Usrnm, ":", usrpnt)
  print("Bot :", cmptrpnt)

if usrpnt > cmptrpnt:
    print("Hurray!", Usrnm," You Won...!")
elif usrpnt == cmptrpnt:
    print("That was close...\nMatch tied...!")
else:
    print("Better luck next time...!")












