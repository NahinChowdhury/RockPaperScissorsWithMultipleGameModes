# Single Player Rock,Paper, Scissor

# ideas for more - https://www.icebreakers.ws/large-group/extreme-rock-paper-scissors.html
import SinglePlayerRockPaperScissorsWithDifficultyLevels


def introduction():
    print("")
    print("Welcome to the Single PLayer Rock,Paper and Scissors game.")
    print("Rules:")
    print("You can only choose Rock, Paper or Scissors.")
    print("")

def difficultyType():
    print("What difficulty would you like you face?")

    options = ["Easy","Medium","Hard","Impossible"]
    for i in options:
        print(" -"+i)

    difficulty = ""

    while difficulty not in ['easy','medium','hard','impossible']:
        difficulty = input("Please enter your choice: ").lower().strip()

    print("")
    return difficulty


def turnValidity():
    turn = ''
    valid = False
    while turn.isdigit() != True or valid != True:
        turn = input("Please enter how many wins you need to end game: ").strip()

        if turn.isdigit() == True:
            if int(turn) > 0:
                valid = True
    print("")
    return int(turn)


def playerInputValidity():
    playerChoice = ''
    
    while playerChoice not in ["rock", "paper","scissors"]:
        playerChoice = input("You choose: ").lower().strip()

    print("")
    return playerChoice


def botChoiceOutput(botChoices):
    print("Computer Robot chooses: "+ botChoices)
    print("")

def winner(playerOneChoice,botChoice):
    # if player one 
    precedence = ["rock", "paper","scissors"]
    
    # if player1 == pred[smth] and player2 == pred[smth - 1]
    # player 1 wins
    # if player1 ==pred[smth] and player 2 == pred[smth - 2]
    # player 2 wins
    
    playerOnePos = precedence.index(playerOneChoice)
    # if player1 chooses smth and player2 chooses something weaker than him
    if playerOneChoice == precedence[playerOnePos] and botChoice == precedence[playerOnePos]:
        return 0
    
    elif playerOneChoice == precedence[playerOnePos] and botChoice == precedence[playerOnePos - 1]:
        return 1
    
    else:
        return 2    
    
def scores(playerOneWins,botWins):
    
    print("")
    print("Scores so far:")
    print("You: "+ str(playerOneWins))
    print("Computer Robot: "+ str(botWins))
    print("")
        
def winnerAnnouncement(playerOneWins,turn):
    print("")
    if playerOneWins >= turn:
        print("You Win!")
    else:
        print("Computer Robot Wins!")    

def gameEndingLines():
    print("")
    print("Game Over! Thank you for playing.")    



def main():
    
    introduction()
    difficulty = difficultyType()
    turns = turnValidity()

    playerOneWins = 0
    botWins = 0
    
    while(playerOneWins < turns and botWins < turns):
        if difficulty == 'easy':
            playerOneChoice = playerInputValidity()
            botChoices = SinglePlayerRockPaperScissorsWithDifficultyLevels.botChoiceEasy(playerOneChoice)
            botChoiceOutput(botChoices)

            result = winner(playerOneChoice,botChoices)

            if result == 0:
                pass
            elif result == 1:
                playerOneWins += 1
            else:
                botWins += 1

            scores(playerOneWins,botWins)

        elif difficulty == 'medium':
            playerOneChoice = playerInputValidity()
            botChoices = SinglePlayerRockPaperScissorsWithDifficultyLevels.botChoiceMedium()
            botChoiceOutput(botChoices)

            result = winner(playerOneChoice,botChoices)

            if result == 0:
                pass
            elif result == 1:
                playerOneWins += 1
            else:
                botWins += 1

            scores(playerOneWins,botWins)

        elif difficulty == 'hard':
            playerOneChoice = playerInputValidity()
            botChoices = SinglePlayerRockPaperScissorsWithDifficultyLevels.botChoiceHard(playerOneChoice)
            botChoiceOutput(botChoices)

            result = winner(playerOneChoice,botChoices)

            if result == 0:
                pass
            elif result == 1:
                playerOneWins += 1
            else:
                botWins += 1

            scores(playerOneWins,botWins)

        elif difficulty == 'impossible':
            playerOneChoice = playerInputValidity()
            botChoices = SinglePlayerRockPaperScissorsWithDifficultyLevels.botChoiceImpossible(playerOneChoice)
            botChoiceOutput(botChoices)

            result = winner(playerOneChoice,botChoices)

            if result == 0:
                pass
            elif result == 1:
                playerOneWins += 1
            else:
                botWins += 1

            scores(playerOneWins,botWins)

    winnerAnnouncement(playerOneWins,turns)

    gameEndingLines()

if __name__ == '__main__':
    main()