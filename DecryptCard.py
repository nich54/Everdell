from EverdellDeck import *

def decrypt(num, deck):
    return deck[int(num)]

if (__name__ == "__main__"):
    deck = create_deck()

    seed = int(input("Enter the random seed: "))

    shuffle_deck(deck, seed)

    while (True):
        cardNum = input("Enter card number: ")
        print(decrypt(cardNum, deck))
