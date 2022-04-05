#!/usr/bin/env python3

# Created by: Sarah
# Created on: Apr, 5th, 2022
# This program asks the user to  guess a number. It then generates a
# random number. It also checks to see if user guess is a valid number entered 
# to determine if user guess is == rand num. 

import random


def main():
    # declare variables
    random_number = random.randint(0, 9)
    # get number guessed from user
    user_guess = input("Guess a number between 0 and 9: ")
    print("")

    try:
        # Changing string into integer
        user_guess_as_int = int(user_guess)
        # check to see if user guess == random number
        if random_number == user_guess_as_int:
            print("Your guess is correct!")
        else:
            print("Your guess is incorrect, the correct number is: {}".
                  format(random_number))

    except Exception:
        print("{} is not a number.". format(user_guess))


if __name__ == "__main__":
    main()
