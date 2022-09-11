"""
I'll be making hangman in python, I know you know the game so let's get started.
I'll need three things
- random module
- arranging words and dashes
- display of hangman
"""
#Importing the module
import random

def hangman():
    list_of_words = ["ramaphosa", "sibabalwe", "gerald", "giraff", "thamsanqa"]
    word = random.choice(list_of_words) # It will create a random word from the list of words
    #print(word)

    turns = 10

    guess_made = ""
    valid_entry = set("abcdefghijklmnopqrstuvwxyz")

    while len(word)> 0:
        main_word = ""
        missed = 0
        
        for letter in word:
            if letter in guess_made:
                main_word += letter
            else:
                main_word += "_ " 
        if main_word == word:
            print(f"{main_word}\n You won!")
            break

        print(f"Guess the word {main_word}")
        guess = input()

        if guess in valid_entry:
            guess_made += guess 
        else:
            print("Enter valid character")
            guess=input()
        
        if guess not in word:
            turns = turns - 1

            if turns == 9:
                print(f"Left with {turns} turns!")
                print("""
                        ______________________

                
                
                """)

            elif turns == 8:
                print(f"Left with {turns} turns!")
                print("""
                        ______________________
                                  
                                  O
                
                
                """)

            elif turns == 7:
                print(f"Left with {turns} turns!")
                print("""
                        ______________________
                                  
                                  O
                                  |
                
                """)

            if turns == 6:
                print(f"Left with {turns} turns!")
                print("""
                        ______________________
                                  
                                  O
                                  |
                                |/ 
                """)

            if turns == 5:
                print(f"Left with {turns} turns!")
                print("""
                        ______________________
                                  
                                  O
                                  |
                                |/ \|
                """)

            if turns == 4:
                print(f"Left with {turns} turns!")
                print("""
                        ______________________
                                  
                                 \O
                                  |
                                |/ \|
                """)

            if turns == 3:
                print(f"Left with {turns} turns!")
                print("""
                        ______________________
                                  
                                 \O/
                                  |
                                |/ \|
                """)

            if turns == 2:
                print(f"Left with {turns} turns!")
                print("""
                        ______________________
                                  
                                 \O/    |
                                  |
                                |/ \|
                """)

            if turns == 1:
                print(f"Left with {turns} turns! You're about to be a murderer!")
                print("""
                        ______________________
                                  |     |
                                 \O/    |   
                                  |     |    
                                |/ \|   |
                """)
            if turns == 0:
                print(f"You l{turns}0SE !! and you killed a man")
                break


        

name = input("Please enter your name: ")
print(f"Welcome {name}")
print("_"*120)
print("Let's see if you can guess a word in less than 10 attempts!")
hangman() #After entering your name it will call the above function
