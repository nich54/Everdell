import json
import random
import time

def current_milli_time():
    t = round(time.time() * 1000)
    print("Random seed:", t)
    return t

def create_deck():
    file = open("cards/CardData.json")
    cardData = json.load(file)

    deck = []
    
    for card in cardData:
        for _ in range(card["number"]):
            deck.append(card["name"])

    return deck

def shuffle_deck(deck, seed = None):
    if (seed == None):
        seed = current_milli_time()
    random.seed(seed)
    random.shuffle(deck)

def encrypt_deck(deck):
    xDeck = [i for i in range(len(deck))]
    random.shuffle(xDeck)

    return xDeck
