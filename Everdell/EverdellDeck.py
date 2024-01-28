import json
import random
import time

def current_milli_time():
    return round(time.time() * 1000)

def create_deck():
    file = open("CardData.json")
    cardData = json.load(file)

    deck = []
    
    for card in cardData:
        for _ in range(card["number"]):
            deck.append(card["name"])

    return deck

def encrypt_deck(deck):
    t = current_milli_time()
    print("Random seed:", t)

    random.seed(t)
    random.shuffle(deck)

    xDeck = [i for i in range(len(deck))]
    random.shuffle(xDeck)

    return xDeck
