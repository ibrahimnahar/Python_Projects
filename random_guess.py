import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while random_number != guess:
        try:
            guess = int(input(f"guess a number between 1 and {x}: "))
            if guess > random_number:
                print(f"guess again. too high! ")
            elif guess < random_number:
                print(f"guess again. too low! ")
        except:
            print("invalid input enter a number. ")
    print(f"congrats! you guessed the number {random_number} correctly!! ")


def computer_guess(x):
    low = 1
    high = x
    guess = 0
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(
            f'is {guess} too high "h", too low "l" or correct "c"?? '
        ).lower()
        if feedback == "l":
            low = guess + 1
        elif feedback == "h":
            high = guess - 1
    print(f"congrats! computer guessed your number, {guess}, correctly!!")


computer_guess(500)
