# RPS complete package

import RockPaperScissors
import RockPaperScissorsWithHealth
import SinglePlayerRockPaperScissors

# greet player
# ask them which mode they'd like to play
# classic 2-player mode
# 2player mode with Health
# Single player mode against bot
#   single player should have 3 modes: easy,medium,impossible

def introduction():

    print("")
    print("Welcome to the game of Rock,Paper and Scissors.")
    print("Rules:")
    print("You can only choose Rock, Paper or Scissors.")
    print("")

def options():
    print("Which game mode would you like to play?")
    print(" 1- Classic 2-player")
    print(" 2- 2player mode with Health ")
    print(" 3- Single player mode against bot")

    userChoice = ""
    while userChoice.isdigit() != True or userChoice not in ['1','2','3']:
        userChoice = input("Please enter the number assigned to the mode you'd like to play: ").strip()

    print("")
    return int(userChoice)

def playAgain():
    play = ''
    print("")
    while play.lower().strip() not in ['y','n']:
        play = input("Would you like to play again? (y/n): ")

    print("")

    if play == 'y':
        return True
    elif play == 'n':
        return False
    else:
        print("play is neither True not False, something is wrong.")
        return 0

def gameEndingLines():

    print("")
    print("Thank you for playing. Hope you play again soon!")

def main():

    introduction()
    play = True
    while play:
        choice = options()

        if choice == 1:
            RockPaperScissors.main()
            play = playAgain()
        elif choice == 2:
            RockPaperScissorsWithHealth.main()
            play = playAgain()
        elif choice == 3:
            SinglePlayerRockPaperScissors.main()
            play = playAgain()

    gameEndingLines()

main()