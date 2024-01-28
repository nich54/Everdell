from EverdellDeck import *
from DecryptCard import decrypt

def draw_card(shuffledDeck, startingDeck, hidden):
    if (len(shuffledDeck) == 0):
        print("Deck empty!")
    else:
        cardNum = shuffledDeck.pop()
        if (hidden):
            print(cardNum)
        else:
            print(decrypt(cardNum, startingDeck))
        

if (__name__ == "__main__"):
    startingDeck = create_deck()
    shuffle_deck(startingDeck)
    deck = encrypt_deck(startingDeck)

    while (True):
        x = input("Draw a card? ")
        draw_card(deck, startingDeck, len(x) == 0)