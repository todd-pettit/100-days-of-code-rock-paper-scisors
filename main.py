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


selections = ['Rock', 'Paper', 'Scissors']
tied_message = "You have tied!"
defeated_message = "You have been defeated!"
victory_message = "You have won! Congratulations!"

user_input = int(input("What do you choose? Type '0' for Rock, '1' for Paper, or '2' for Scissors. "))
user_selection = selections[user_input]
npc_selection = selections[random.randint(0,2)]

if user_selection == 'Rock':
    print("user selection: \n", rock)
    if npc_selection == 'Rock':
        print("npc selection: \n", rock)
        print(tied_message)
    elif npc_selection == 'Paper':
        print("npc selection: \n", paper)
        print(defeated_message)
    elif npc_selection == 'Scissors':
        print("npc selection: \n", scissors)
        print(victory_message)

if user_selection == 'Paper':
    print("user selection: \n", paper)
    if npc_selection == 'Rock':
        print("npc selection: \n", rock)
        print(victory_message)
    elif npc_selection == 'Paper':
        print("npc selection: \n", paper)
        print(tied_message)
    elif npc_selection == 'Scissors':
        print("npc selection: \n", scissors)
        print(defeated_message)    

if user_selection == 'Scissors':
    print("user selection: \n", scissors)
    if npc_selection == 'Rock':
        print("npc selection: \n", rock)
        print(defeated_message)
    elif npc_selection == 'Paper':
        print("npc selection: \n", paper)
        print(victory_message)
    elif npc_selection == 'Scissors':
        print("npc selection: \n", scissors)
        print(tied_message)
