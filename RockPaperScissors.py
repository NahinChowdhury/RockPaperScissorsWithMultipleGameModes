'''
class player():
    
    def __init__(self, number):
        
        self.number = number
class Game
'''

# Rock,Paper, Scissor

# have 3 turns
# tracks player 1 and 2

# rock > scissors 
# scissors > paper
# paper > rock

# takes player 1 input
# takes player 2 input

# compares power of inputs and announces winner

# repeats system until one player reaches a score of 3
# game ends


def introduction():
    print("")
    print("Welcome to the Classic 2-player Rock,Paper and Scissors game.")
    print("Rules:")
    print("You can only choose Rock, Paper or Scissors.")
    print("")


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


def playerInputValidity(number):
    playerChoice = ''
    
    while playerChoice not in ["rock", "paper","scissors"]:
        playerChoice = input("Player "+ str(number) +" chooses: ").lower().strip()
    print("")
    return playerChoice

def winner(playerOneChoice,playerTwoChoice):
    # if player one 
    precedence = ["rock", "paper","scissors"]
    
    # if player1 == pred[smth] and player2 == pred[smth - 1]
    # player 1 wins
    # if player1 ==pred[smth] and player 2 == pred[smth - 2]
    # player 2 wins
    
    playerOnePos = precedence.index(playerOneChoice)
    # if player1 chooses smth and player2 chooses something weaker than him
    if playerOneChoice == precedence[playerOnePos] and playerTwoChoice == precedence[playerOnePos]:
        return 0
    
    elif playerOneChoice == precedence[playerOnePos] and playerTwoChoice == precedence[playerOnePos - 1]:
        return 1
    
    else:
        return 2    
    
def scores(playerOneWins,playerTwoWins):
    
    print("")
    print("Scores so far:")
    print("Player 1: "+ str(playerOneWins))
    print("Player 2: "+ str(playerTwoWins))
    print("")
        
def winnerAnnouncement(playerOneWins,turn):

    print("")
    if playerOneWins >= turn:
        print("Player One Wins!")
    else:
        print("Player Two Wins!")    

def gameEndingLines():

    print("")
    print("Game Over! Thank you for playing.")    

def main():
    
    introduction()
    
    turns = turnValidity()
    
    playerOneWins = 0
    playerTwoWins = 0
    
    while(playerOneWins < turns and playerTwoWins < turns):
        playerOneChoice = playerInputValidity(1)
        playerTwoChoice = playerInputValidity(2)
        
        result = winner(playerOneChoice,playerTwoChoice)
    
        if result == 0:
            pass
        elif result == 1:
            playerOneWins += 1
        else:
            playerTwoWins += 1 
        
        scores(playerOneWins,playerTwoWins)

    winnerAnnouncement(playerOneWins,turns)

    gameEndingLines()

#main()