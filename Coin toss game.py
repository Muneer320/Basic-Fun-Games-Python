import random

coin = ["heads", "tails"]
while True:
    toss = random.choice(coin)
    selection = input("Heads or Tails: ")

    if selection == toss:
        print('You win! coin landed on ' + toss)
    else:
        print('You lost! coin landed on ' + toss)