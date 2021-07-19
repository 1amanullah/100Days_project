import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choose = int(input("What do you choose?Type 0 for Rock , 1 for Paper and 2 for Scissors.\n"))
computer_choose = random.randint(0,2)

symbols = [rock,paper,scissors]
if user_choose >=3 or computer_choose < 0:
  print("You input invalid number")

else:
  print("You choose {}".format(user_choose))

  print(symbols[user_choose])

  print("Computer choose {}".format(computer_choose))

  print(symbols[computer_choose])


  if user_choose == 0 and computer_choose == 2:
    print("Yeah,You win ")

  elif user_choose > computer_choose:
    print("Yeah,You win")

  elif user_choose < computer_choose:
    print("Oh,You lose")

  else:
    print("Ooo,It's Draw")
