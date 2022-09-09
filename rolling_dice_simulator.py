"""
I'll be creating a rolling dice simulator, this is a basic code simulation 
I will be only using generic python code and the random module
"""
# Import random to generate the sample randomly 
import random

#We need to prompt user for input whether they want to play or not
user_input = input("Would you like to play a dice game:")

#Let's create a while loop to continue playing 

while user_input.lower() == "yes" :
    # let's generate numbers from [1, 6]
    number = random.randint(1,6)
    
    #Now let's create a visual representation of the dice
    if number == 1:
        print("""
                 ________________
                |                |
                |                |       
                |                |
                |       O        |
                |                |
                |                |
                |________________|
        """)
    elif number == 2:
        print("""
                 ________________
                |                |
                |       O        |       
                |                |
                |                |
                |                |
                |       0        |
                |________________|
        """)

    elif number == 3:
        print("""
                 ________________
                |                |
                |       O        |       
                |                |
                |       0        |
                |                |
                |       0        |
                |________________|
        """)

    elif number == 4:
        print("""
                 ________________
                |                |
                |  O          O  |       
                |                |
                |                |
                |                |
                |  O          O  |
                |________________|
        """)
    elif number == 5:
        print("""
                 ________________
                |                |
                |  O          O  |       
                |                |
                |       0        |
                |                |
                |  O          O  |
                |________________|
        """)

    elif number == 6:
        print("""
                 ________________
                |                |
                |  O     O    O  |       
                |                |
                |                |
                |                |
                |  O     0    O  |
                |________________|
        \n\n""")

    user_input = input("press yes to roll again and no to exit: ")
    print("\n")
    print("\n")
