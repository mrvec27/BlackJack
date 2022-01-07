from BlackjackPlayer import BlackjackPlayer
from BlackjackDealer import BlackjackDealer
from BlackjackDeck import BlackjackDeck
from Card import Card

class BlackjackGame:
    def __init__(self):
        self.deck = BlackjackDeck()
        self.dealer = BlackjackDealer()
        self.player = BlackjackPlayer()
        self.dealer.add_card(self.deck.deal())
        self.dealer.add_card(self.deck.deal())
        self.player.add_card(self.deck.deal())
        self.player.add_card(self.deck.deal())
        self.show_cards_player()
        self.show_cards_dealer()

    def show_cards_player(self, show_score = False):
        player_cards = self.player.get_hand()
        
        print("Player's cards:")
        card_count = 1
        for card in player_cards:
            print(str(card_count) + " : " +card.get_card_description())
            card_count += 1
        
        if show_score:
            print("Score : " + str(self.player.get_score()))
    
    def show_cards_dealer(self, show_score = False):
        dealer_cards = self.dealer.get_hand()

        print("Dealer's cards:")
        card_count = 1
        for card in dealer_cards:
            print(str(card_count) + " : " +card.get_card_description())
            card_count += 1
        if not self.dealer.show_all_cards:
            print("X : Dealer's second card is hidden")
        
        if show_score:
            print("Score : " + str(self.dealer.get_score()))
    
    def player_turn(self):
        player_input = input("Do you want to hit or stand? (HIT/STAND)")
        if player_input == "HIT":
            self.player.add_card(self.deck.deal())
            self.show_cards_player(True)
            if self.player.bust:
                print("Player busts!")
            else:
                self.player_turn()

        elif player_input == "STAND":
            self.player.stand = True
            self.show_cards_player(True)
            print("Player stands!")

        else:
            print("Invalid input!")
            self.player_turn()
    
    def dealer_turn(self):
        self.dealer.show_all_cards = True
        if self.dealer.get_score() < 17:
            self.dealer.add_card(self.deck.deal())
            self.show_cards_dealer(True)
            self.dealer_turn()

        elif self.dealer.get_score() <= 21:
            self.show_cards_dealer(True)
            print("Dealer stands!")

        else:
            self.show_cards_dealer(True)
            print("Dealer busts!")
    
    def start_game(self):
        self.player_turn()
        if self.player.bust:
            print("Dealer wins!")
            return

        self.dealer_turn()
        if self.dealer.bust:
            print("Player wins!")
            return

        if self.player.get_score() > self.dealer.get_score():
            print("Player wins!")
        elif self.player.get_score() < self.dealer.get_score():
            print("Dealer wins!")
        else:
            print("Draw!")

