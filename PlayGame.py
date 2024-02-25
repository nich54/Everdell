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

    first = ""
    while (first != "y" and first != "n"):
        first = input("Going first? (y/n) ")
    
    print("\nMEADOW:")
    for _ in range(8):
        draw_card(deck, startingDeck, False)
    print("\nYOUR HAND:")
    for _ in range(5 if first == "y" else 6):
        draw_card(deck, startingDeck, False)
    print("\nTHEIR HAND:")
    for _ in range(6 if first == "y" else 5):
        draw_card(deck, startingDeck, True)
    print("")

    while (True):
        x = input("Draw a card? ")
        draw_card(deck, startingDeck, len(x) == 0)