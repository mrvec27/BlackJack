import random
from Card import Card

class BlackjackDeck:
    def __init__(self):
        self.deck = []
        self.build()

    def build(self):
        totalNumberOfDecks = random.randint(4,10)
        for i in range(totalNumberOfDecks):
            for suit in ["S", "H", "D", "C"]:
                for rank in range(1, 14):
                    self.deck.append(Card(suit, rank))
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()