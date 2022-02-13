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
images = [rock, paper, scissors]
print("Rock, Paper, Scissors, Shoot!!")

user = int(input("Select 0 for Rock, 1 for Paper or 2 for Scissors\n"))
if user >= 3 or user < 0:
  print ("Invalid Choice! Try Again")
else: 
  print(images[user])

  computer = random.randint(0,2)
  print(f"The computer chose {computer}")
  print(images[computer])

#Rock = 0
#Paper = 1
#Scissors = 2

  if user == computer:
    print ("This is a Draw! Let's keep going")
  elif computer == 0 and user == 2:
    print ("You lose")
  elif user == 0 and computer == 2:
    print ("You win")
  elif user > computer:
    print ("You win")
  elif computer > user:
    print ("You lose")
