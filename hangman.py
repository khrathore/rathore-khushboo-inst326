word = "toothbrush"
letterg = []
strikes = 0

def hangmanfill(word, letterg):
    hangmanw= "-----------"
    counter = 0
    for char in word:
        if  char in letterg:
            hangmanw = hangmanw[:counter]+char+hangmanw[counter+1:]
        elif counter == 9:
            strikes = strikes + 1
        elif hangmanw == "toothbrush":
            print("Congratulations! You won.")
            exit()
        counter = counter + 1
    return hangmanw 


while strikes < 5:
    guess = input("Guess a letter:").lower()
    if guess.lower() == "quit":
        quit()
    letterg.append(guess)
    hangmanfill(word, letterg)
print("Sorry, the game is over")
    
    
    
        
       
       
           
            