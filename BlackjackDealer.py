class BlackjackDealer:
    
    def __init__(self):
        self.hand = []
        self.minimum_possible_score = 0
        self.maximum_possible_score = 0
        self.stand = False
        self.bust = False
        self.show_all_cards = False
    
    def add_card(self, card):
        self.hand.append(card)
        self.update_score(card)
    
    def update_score(self, card):
        self.minimum_possible_score += card.get_possible_card_points()[0]
        self.maximum_possible_score += card.get_possible_card_points()[1]
        if self.minimum_possible_score > 21:
            self.bust = True
    
    def get_hand(self):
        if self.show_all_cards:
            return self.hand
        else:
            return self.hand[0:1]
    
    def get_score(self):
        if self.maximum_possible_score > 21:
            return self.minimum_possible_score
        return self.maximum_possible_score

    