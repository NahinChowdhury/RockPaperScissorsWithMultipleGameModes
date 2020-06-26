# Idea of the Health based game was given by Zarif Mohaimen Fahad.
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
    print("Welcome to the 2player Rock,Paper and Scissors with Health game.")
    print("Rules:")
    print("Only valid inputs are 'Rock', 'Paper' and 'Scissors'.")
    print("There should be no spaces between the letters and all forms of capitalisation are allowed.")
    print("First player to reach zero health loses.")
    print("")
    
    
def maxHealthValidity():
    
    maxHealth = ''
    valid = False
    while maxHealth.isdigit() != True or valid != True:
        maxHealth = input("Please enter the max health for each player: ").strip()
    
        if maxHealth.isdigit() == True:
            if int(maxHealth) > 0:
                valid = True
    print("")
    return int(maxHealth)

def damageValidity(maxHealth):
    
    damage = ''
    valid = False
    while damage.isdigit() != True or valid != True:
        damage = input("Please enter how much damage the loser of each round should take: ").strip()
    
        if damage.isdigit() == True:
            if int(damage) <= maxHealth and int(damage) > 0:
                valid = True
    print("")
    return int(damage)    
    
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
    
def negativeHealthChecked(playerHealth):
    if playerHealth < 0:
        return 0
    return playerHealth
    
def health(playerOneHealth,playerTwoHealth):
    playerOneHealth = negativeHealthChecked(playerOneHealth)
    playerTwoHealth = negativeHealthChecked(playerTwoHealth)
    
    print("")
    print("Healths so far:")
    print("Player 1: "+ str(playerOneHealth))
    print("Player 2: "+ str(playerTwoHealth))
    print("")
        
def winnerAnnouncement(playerOneHealth):
    print("")
    if playerOneHealth <= 0:
        print("Player Two Wins!")
    else:
        print("Player One Wins!")    

def gameEndingLines():
    print("")
    print("Game Over! Thank you for playing.")    

def main():
    
    introduction()
    
    # write a code for what the max health should be
    # also, how much damage should the loser take per round
    
    maxHealth = maxHealthValidity()
    damage = damageValidity(maxHealth)
    
    
    playerOneHealth = maxHealth
    playerTwoHealth = maxHealth
    
    while(playerOneHealth > 0 and playerTwoHealth > 0):
        playerOneChoice = playerInputValidity(1)
        playerTwoChoice = playerInputValidity(2)
        
        result = winner(playerOneChoice,playerTwoChoice)
    
        if result == 0:
            pass
        elif result == 1:
            # as player 1 wins, player 2 takes damage
            playerTwoHealth -= damage
        else:
            playerOneHealth -= damage
        
        health(playerOneHealth,playerTwoHealth)

    winnerAnnouncement(playerOneHealth)

    gameEndingLines()

#main()