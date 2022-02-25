#!/usr/bin/env python3
'''Python training class certification project
   Author: eric.koetters@citi.com

   Description:
   Game to guess a system selected random number'''

# Import needed packages
import crayons
from random import randint

# System selected random number
# 1 to 10 inclusive
numSelected = randint(1,10)

def main():
    '''Main function'''

    print("The system has picked a number 1 through 10")

    # Ask user for their guess, only accept intergers
    # Will keep asking until interger is enterd
    while True:
        try:
            numGuessed = int(input("Can you guess what it is?? Enter your guess: "))
            break
        except:
            print("You must enter an interger only, please try again.") 

    # Show the system selected number and the user guess
    print(f"The system picked: {numSelected}")
    print(f"You entered: {numGuessed}")

    # Test to see if the guess is correct
    if numGuessed == numSelected:
        print(crayons.green("YOU WIN"))
    else:
        print(crayons.red("Sorry your guess is incorrect, you loose"))

if __name__ == "__main__":
    main()
