import sys
import random
from enum import Enum

def rps():

    game_count = 0
    your_score = 0
    python_score = 0


    def play_rps(): 
        nonlocal your_score
        nonlocal python_score
        
        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3


        playerchoice = input(
            "\nEnter... \n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")
        if playerchoice not in ["1", "2", "3"] :
            print ("You must enter 1, 2, or 3.")
            return play_rps()
        player = int(playerchoice)
        computerchoice = random.choice("123")

        computer = int(computerchoice)

        print(f"\nYou chose {str(RPS(player)).replace('RPS.', '').title()}.")
        print(f"Python chose {str(RPS(computer)).replace('RPS.', '').title()}.\n")
        
        def decide_winner (player, computer) :
            nonlocal your_score
            nonlocal python_score
            if player == 1 and computer == 3:
                your_score += 1
                return "🎉 You win!"
            elif player == 2 and computer == 1:
                your_score += 1
                return "🎉 You win!"
            elif player == 3 and computer == 2:
                your_score += 1
                return "🎉 You win!"
            elif player == computer:
                return "😲 Tie game!"
            else: 
                python_score += 1
                return "🐍 Python wins!"
                
        
        game_result = decide_winner(player, computer)
        print(game_result)

        nonlocal game_count
        game_count+=1
        print(f"\nGame count: {str(game_count)}" )
        print(f"\nYour score: {str(your_score)}" )
        print(f"Python score: {str(python_score)}" )

        print("\nPlay again ?")

        while True :
            playagain = input("\nY for Yes or \nQ to Quit \n\n")
            if playagain.lower() not in ["y", "q"] :
                print("\nyou have to press Y or Q")
                continue
            else:
                break
        if playagain.lower() == "y":
            return play_rps()
        else:
            print("\n🎉🎉🎉🎉")
            print("Thank you for playing!\n")
            sys.exit("Bye! 👋")

    return   play_rps

play = rps()

play()