import sys
from EverdellDeck import *

if (__name__ == "__main__"):
    unshuffledDeck = create_deck()
    print(len(unshuffledDeck))
    deck = encrypt_deck(unshuffledDeck)

    while (True):
        x = input("Draw a card?")
        if (len(deck) == 0):
            print("Ruh roh")
        else:
            print(deck.pop())


    