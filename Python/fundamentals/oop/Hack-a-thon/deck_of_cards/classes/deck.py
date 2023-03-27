from . import card
import random

class Deck:


    def __init__( self ):
        suits = [ "spades" , "hearts" , "clubs" , "diamonds" ]
        self.cards = []

        for s in suits:
            for i in range(1,14):
                str_val = ""
                if i == 1:
                    str_val = "Ace"
                elif i == 11:
                    str_val = "Jack"
                elif i == 12:
                    str_val = "Queen"
                elif i == 13:
                    str_val = "King"
                else:
                    str_val = str(i)
                self.cards.append(card.Card( s , i , str_val ) )

    def show_cards(self):
        for card in self.cards:
            card.card_info()
    
    #return randomly a card for the deck
    def give_card(self):
        shuffle = random.randint(0, len(self.cards)-1)
        return self.cards[shuffle]
