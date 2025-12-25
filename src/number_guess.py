import random

secret = random.randint(1, 100)
tries = 0

print("Guess the number (1-100)")

while True:
    guess = int(input("Your guess: "))
    tries += 1
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print(f"Correct! Tries: {tries}")
        break
