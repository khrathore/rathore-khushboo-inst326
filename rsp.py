from random import random
import random as rand

def winner1(p1,p2):
    if p1 == p2:
        return "The game is a tie"
    if p1 == "r":
        if p2 == "s":
            return "The game is won by player 1"
        else: 
            return "The game is won by player 2"
    elif p1 == "s":
        if p2 == "p":
            return "The game is won by player 1"
        else: 
            return "The game is won by player 2"
    elif p1 == "p":
        if p2 == "r":
            return "The game is won by player 1"
        else: 
            return "The game is won by player 2"
# In class example 1
def winner2(p1,p2):
    if p1 == p2:
        return "The game is a tie"
    elif (p1 == "r" and p2 == "s" or p1 == "p" and p2 == "r" or p1 == "s" and p2 == "p"):
        return "The game is won by player 1"
    else:
        return "The game is won by player 2"

def winner3(p1,p2):
    # Expression 1 if Condition, else Expression 2
    # Expression can be a statement, not all statements are an expression. Condition is an expression that
    # is always going to be boolean
    return(
        "tie" if p1 == p2 else
        "p1" if (p1 == "r" and p2 == "s" or p1 == "p" and p2 == "r" or p1 == "s" and p2 == "p")
        else "p2"
    )

# Don't stop at the obvious solution, try to make it better, easier and more efficient. Be thoughtful about
# the programming that you do
# Put docstrings into your code

tools = ["r", "s", "p"]
p1 = rand.choice(tools)
print("Player 1 has chosen " + p1)
p2 = rand.choice(tools)
print("Player 2 has chosen " + p2)
print(winner3(p1,p2))