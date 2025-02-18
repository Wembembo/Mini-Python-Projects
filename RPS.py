import random

ai_weapon = ["R", "P", "S"]
ai_choice = random.choice(ai_weapon)
player_choice=input("welcome to rock paper scissors, please select either [R]ock, [P]aper, [S]cissors: ")
player_input=player_choice.upper()
print(ai_choice)
if ai_choice == player_input:
    print("We picked the same thing, it's a tie")
elif player_input == "R":
    if ai_choice == "S":
        print("Rock beats paper, you win!")
    else:
        print("Paper beats rock, I win")
elif player_input == "P":
    if ai_choice == "R":
        print("Paper beats Rock, you win!")
    else:
        print("Scissors beat paper, I win")
elif player_input == "S":
    if ai_choice == "P":
        print("Scissors beats paper, you win!")
    else:
        print("Rock beats Scissors, I win")

#if ai_choice == player_input:
#    print("We picked the same thing, it's a tie")
#elif ai_choice == "R" and player_input == "P":
#    print("Paper beats rock, you win")
#elif ai_choice == "R" and player_input== "S":
#    print("Rock smashes scissors, I win:")
#elif ai_choice == "P" and player_input == "S":
#    print("Scissors beats paper, you win")
#elif ai_choice == "P" and player_input == "R":
#    print("Paper beats rock, I win")
#elif ai_choice == "S" and player_input == "R":
#    print("Rock beats scissors, you win!")
#elif ai_choice == "S" and player_input == "P":
#    print("Scissors beats paper, I win")