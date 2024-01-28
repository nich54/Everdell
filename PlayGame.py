from EverdellDeck import *
from DecryptCard import decrypt

if (__name__ == "__main__"):
    startingDeck = create_deck()
    shuffle_deck(startingDeck)
    deck = encrypt_deck(startingDeck)

    while (True):
        x = input("Draw a card? ")
        if (len(deck) == 0):
            print("Ruh roh")
        else:
            cardNum = deck.pop()
            if (len(x) > 0):
                print(decrypt(cardNum, startingDeck), cardNum)
            else:
                print(cardNum)
    