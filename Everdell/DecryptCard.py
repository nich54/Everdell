import random

from EverdellDeck import create_deck

if (__name__ == "__main__"):
    deck = create_deck()

    seed = input("Enter the random seed: ")

    random.seed(seed)
    random.shuffle(deck)

    while (True):
        cardNum = input("Enter card number: ")
        print(deck[int(cardNum)])
