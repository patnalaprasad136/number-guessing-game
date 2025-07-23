import random

def main():
    print("Hi! Welcome to the Number Guessing Game.")
    print("You have 7 chances to guess the number. Let's start!\n")

    # Get bounds from the user
    low = int(input("Enter the Lower Bound: "))
    high = int(input("Enter the Upper Bound: "))

    print(f"\nYou have 7 chances to guess the number between {low} and {high}. Let's start!")

    num = random.randint(low, high)
    ch = 7  # Total allowed chances
    gc = 0  # Guess counter

    while gc < ch:
        gc += 1
        guess = int(input('Enter your guess: '))

        if guess == num:
            print(f'Correct! The number is {num}. You guessed it in {gc} attempts.')
            break
        elif guess > num:
            print('Too high! Try a lower number.')
        elif guess < num:
            print('Too low! Try a higher number.')

    else:
        # Executed if loop completes without a break (no correct guess)
        print(f'Sorry! The number was {num}. Better luck next time.')

if __name__ == "__main__":
    main()
