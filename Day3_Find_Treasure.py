print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

print("Welcome to the Treasure Island")
print("your mission is to find treasure")

choice1 = input('you\'re at cross road.Where do you want to go? Type "left" or "right"\n').lower()

if choice1 == "left":
  choice2 = input('you\'ev come to a lake.There is island in the middle of lake.Type "wait" to wait for boat.Type "swim" to swim across.\n').lower()

  if choice2 == "wait":
   choice3 = input("You arrive at the unharmed.There is a house with three doors.One red,one yellow and one blue.Which colour do you choose?\n").lower()
   
   if choice3 == "red":
    print("There is a room of fire.Game over.")

   elif choice3 == "yellow":
    print("Wow,You found a treasure! You Win!")

   elif choice3 == "blue":
    print("You enter a room of beasts.Game over.") 
     
   else:
    print("There no door which colour you choose")  

  elif choice2 == "swim":
    print("You get attacked by hungry crocodiles.Game Over.")

else:
  print("You fell into a hole.Game over.")
