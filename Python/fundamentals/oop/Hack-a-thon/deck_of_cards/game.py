from classes.deck import Deck
from classes.player import Player

#Main------------------------------------
print("Welcome to our special BlackJack")
print("-----------------------------------")

bicycle = Deck()
player1 = Player(input("Player 1: What's your name : "))
player2 = Player(input("Player 2: What's your name : "))
# casino = Player("Bellagio")

#Each player gets 5 cards
for i in range (5) :
    player1.pick_card(bicycle)
    player2.pick_card(bicycle)
    # casino.pick_card(bicycle)

#Show information (Name and Hand Value) about the players
player1.show_player()
player2.show_player()
# casino.show_player()

#Checking whose hand is bigger
if (player1.hand_value()>player2.hand_value()):
    print(f"{player1.name} Wins")
elif (player1.hand_value()<player2.hand_value()):
    print(f"{player2.name} Wins")
else:
    print("It's a tie")
