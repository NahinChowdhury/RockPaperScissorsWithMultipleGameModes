import random

# userinput gets taken

# for easy difficulty, bot always loses
#       to make this happen, we will have a list [rock,paper,scissors]
#       we find the index of the player's input in the list and return list[player''s index - 1], so we always lose
#       so, if player chooses rock, we choose scissors. If they choose scissors, we choose paper. and always lose

# for medium difficulty, we will use the bot we have now and it will choose an output using random.randint

# for impossible difficulty, bot never loses
#       we take user input, and get its index in [rock,paper,scissors]
#       if player's input's index is 0 or 1, return list[input index + 1]
#       else return list[0]

def botChoiceEasy(yourChoice):

    precedence = ["rock", "paper", "scissors"]

    yourChoiceIndex = precedence.index(yourChoice)

    return precedence[yourChoiceIndex - 1]


def botChoiceMedium():

    precedence = ["rock", "paper", "scissors"]

    randomChoice = random.randint(0, len(precedence) - 1)
    
    return precedence[randomChoice]

def botChoiceHard(yourChoice):

    precedence = ["rock", "paper", "scissors"]

    max = 100
    randomChoice = random.randint(0, max)
    yourChoiceIndex = precedence.index(yourChoice)

    if randomChoice <= ((10/100) * max):
        return precedence[yourChoiceIndex - 1]

    elif randomChoice <= ((50/100) * max):
        return precedence[yourChoiceIndex]
        #return precedence[random.randint(0, 2)]

    else:
        return precedence[yourChoiceIndex%2 + 1]


def botChoiceImpossible(yourChoice):

    precedence = ["rock", "paper", "scissors"]

    yourChoiceIndex = precedence.index(yourChoice)

    return precedence[yourChoiceIndex%2 + 1]
