# from . import deck
# from . import card
class Player :
    def __init__(self, name):
        self.name = name
        self.hand = []
    
    def pick_card (self, deck):
        card = deck.give_card()
        self.hand.append(card)
        return self
    
    #return the sum of the card's value of the player
    def hand_value (self) :
        value=0
        for card in self.hand :
            value+= card.point_val
        return value

    def show_player(self):
        print(f"Name : {self.name} | Hand Force = : {self.hand_value()}")