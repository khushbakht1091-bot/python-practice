# Problem: The program picks a secret number from 1 to 20. The user gets 5 attempts.
# After each wrong guess print Too high or Too low. End with a win or lose message.
# Sample: Secret 14: guesses 10, 18, 14 → Too low, Too high, Correct! You took 3 attempts.

import random

secret_number = random.randint(1, 20)
attempts = 0

while attempts < 5:

    # Reject non-numeric input without crashing or wasting an attempt
    try:
        guess = int(input("Enter Number : "))
    except ValueError:
        print("Invalid Input")
        continue

    # Enforce the 1-20 range before counting the turn as a guess
    if guess < 1 or guess > 20:
        print("Enter guess between 1 and 20")
        continue

    attempts += 1
    if secret_number < guess:
        print("Too High")
    elif secret_number > guess:
        print("Too Low")
    else:
        print("Correct!")
        print(f"You took {attempts} attempts ")
        break

else:
    # Runs only when all 5 attempts are used without breaking
    print("You lost")
