
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def get_possible_card_points(self):
        if self.rank == 1:
            return 1,11
        elif self.rank > 10:
            return 10,10
        else:
            return self.rank,self.rank
    
    def get_card_description(self):
        if self.rank == 1:
            return "Ace of " + self.suit
        elif self.rank > 10:
            if self.rank == 11:
                return "Jack of " + self.suit
            elif self.rank == 12:
                return "Queen of " + self.suit
            elif self.rank == 13:
                return "King of " + self.suit
        else:
            return str(self.rank) + " of " + self.suit
