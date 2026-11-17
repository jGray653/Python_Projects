import random

def main():
    print("---------------------------------------")
    print("Number Guessing Game!")
    while True:
        print("Please select a difficulty:")
        print("1: Easy (1 - 10)")
        print("2: Medium (1 - 100)")
        print("3: Hard (1 - 1000)")
        print("4: Custom")
        choice = int(input("Choice: "))

        print("---------------------------------------")
        if choice == 1:
            easy()
            break
        elif choice == 2:
            medium()
            break
        elif choice == 3:
            hard()
            break
        elif choice == 4:
            custom()
            break
        else:
            print("Invalid selection. Please choose again.")
            print("---------------------------------------")

#---
def easy():
    num = generate(0, 10)
    tries = 0

    while True:
        guess = int(input("Guess: "))

        if guess < num:
            print("Guess too Small!")
            tries += 1
        elif guess > num:
            print("Guess too Big!")
            tries += 1
        elif guess == num:
            print("You Guessed Correctly!")
            break

        if tries == 5:
            print("You guessed wrong too many times!")
            print(f"The answer was {num}")
            break

    while True:
        print("Play Again?")
        choice = input("Y/N? ").upper()

        if choice == "Y":
            main()
            break
        elif choice == "N":
            break
        else:
            "Incorrect Selection. Try Again."

#---
def medium():
    num = generate(0, 100)
    tries = 0
    
    while True:
        guess = int(input("Guess: "))
    
        if guess < num:
            print("Guess too Small!")
            tries += 1
        elif guess > num:
            print("Guess too Big!")
            tries += 1
        elif guess == num:
            print("You Guessed Correctly!")
            break
    
        if tries == 5:
            print("You guessed wrong too many times!")
            print(f"The answer was {num}")
            break

    while True:
        print("Play Again?")
        choice = input("Y/N? ").upper()

        if choice == "Y":
            main()
            break
        elif choice == "N":
            break
        else:
            "Incorrect Selection. Try Again."

#---
def hard():
    num = generate(0, 1000)
    tries = 0
    
    while True:
        guess = int(input("Guess: "))
    
        if guess < num:
            print("Guess too Small!")
            tries += 1
        elif guess > num:
            print("Guess too Big!")
            tries += 1
        elif guess == num:
            print("You Guessed Correctly!")
            break
    
        if tries == 5:
            print("You guessed wrong too many times!")
            print(f"The answer was {num}")
            break

    while True:
        print("Play Again?")
        choice = input("Y/N? ").upper()

        if choice == "Y":
            main()
            break
        elif choice == "N":
            break
        else:
            "Incorrect Selection. Try Again."

#---
def custom():
    a = int(input("Lower Bound: "))
    b = int(input("Upper Bound: "))

    num = generate(a, b)
    tries = 0
    
    while True:
        guess = int(input("Guess: "))
    
        if guess < num:
            print("Guess too Small!")
            tries += 1
        elif guess > num:
            print("Guess too Big!")
            tries += 1
        elif guess == num:
            print("You Guessed Correctly!")
            break
    
        if tries == 5:
            print("You guessed wrong too many times!")
            print(f"The answer was {num}")
            break

    while True:
        print("Play Again?")
        choice = input("Y/N? ").upper()

        if choice == "Y":
            main()
            break
        elif choice == "N":
            break
        else:
            "Incorrect Selection. Try Again."

#---
def generate(a, b):
    return random.randint(a, b)

#---
if __name__ == "__main__":
    main()