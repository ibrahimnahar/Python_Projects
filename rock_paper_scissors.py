import random


def play():
    player = input("what's your choice? 'r' for rock 'p' for paper 's' for scissors: ")
    computer = random.choice(["r", "p", "s"])

    if player == computer:
        return "it's a tie"

    if is_win(player, computer):
        return "congrats you won!! "

    return "sorry! computer won's"


def is_win(player, computer):
    if (
        (player == "r" and computer == "s")
        or (player == "p" and computer == "r")
        or (player == "s" and computer == "p")
    ):
        return True


print(play())
