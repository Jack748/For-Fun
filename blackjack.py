import random

# Define the Card class
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def __repr__(self):
        # Return a string representation of the card
        return f"{self.value} of {self.suit}"

# Define the Deck class
class Deck:
    def __init__(self):
        self.cards = [Card(suit, value) for suit in ['hearts', 'diamonds', 'clubs', 'spades']
                      for value in range(1, 14)]
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self):
        return self.cards.pop()

# Define the Hand class
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.ace = False
    
    def add_card(self, card):
        # Add a card to the hand and update the value and ace status
        self.cards.append(card)
        self.value += min(card.value, 10)
        if card.value == 1:
            self.ace = True
    
    def adjust_for_ace(self):
        # If the hand has an ace and its value is low enough, set the value to 11
        if self.ace and self.value < 12:
            self.value += 10

    def has_ace(self):
        # If the hand has an ace and its value is low enough, set the value to 11
        return self.ace

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()
    
    def __repr__(self):
        return f"Player {self.name}"
    
    def hit(self, deck):
        # Draw a card from the deck and add it to the player's hand
        self.hand.add_card(deck.deal())
        self.hand.adjust_for_ace()
    
    def stand(self):
        # End the player's turn
        pass

class Dealer(Player):
    def __init__(self):
        super().__init__("Dealer")
    
    def __repr__(self):
        return "Dealer"


def play_blackjack():
    # Create a deck of cards and shuffle it
    deck = Deck()
    deck.shuffle()
    
    # Create a player and a dealer
    player = Player("Player")
    dealer = Dealer()
    
    # Deal the initial cards
    player.hand.add_card(deck.deal())
    player.hand.add_card(deck.deal())
    dealer.hand.add_card(deck.deal())
    dealer.hand.add_card(deck.deal())
    
    '''
    # Player's turn
    while True: 
        # Print the player's hand and ask them to hit or stand
        print(f"Player: {player.hand.value}")
        print(f"Dealer: {dealer.hand.value}")
        choice = input("Hit or stand? ").lower()
        if choice == "hit" or choice == "h":
            player.hand.add_card(deck.deal())
            if player.hand.value > 21:
                print(f"Player: {player.hand.value}")
                print("Bust! You lose.")
                return
        elif choice == "stand" or choice == "s":
            break
        

    if player.hand.value == 21:
        return "player"
    elif dealer.hand.value == 21:
        return "dealer"
    
    # Player's turn
    while player.hand.value < 16:
        # Hit until the player has a hand value of less than 17
        player.hand.add_card(deck.deal())
        if player.hand.value > 21:
            return "dealer"
    
    # Dealer's turn
    while dealer.hand.value < 17:
        dealer.hand.add_card(deck.deal())
        if dealer.hand.value > 21:
            return "player"
    
    # Compare the player's hand and the dealer's hand
    if player.hand.value > dealer.hand.value:
        return "player"
    elif player.hand.value < dealer.hand.value:
        return "dealer"
    else:
        return "tie"
    
    
def play_standard():
    # Run the play_blackjack function 1000 times and count the number of wins, losses, and ties
    number_of_games = 50000
    wins = 0
    losses = 0
    ties = 0
    for i in range(number_of_games):
        result = play_blackjack()
        if result == "player":
            wins += 1
        elif result == "dealer":
            losses += 1
        else:
            ties += 1

    # Calculate and print the percentage of games won by the player
    percentage_won = 100 * wins / number_of_games
    print(f"The player won {percentage_won:.1f}% of the games.")
    percentage_ties = 100 * ties / number_of_games
    print(f"The player ties {percentage_ties:.1f}% of the games.")
    percentage_losses = 100 * losses / number_of_games
    print(f"The player losses {percentage_losses:.1f}% of the games.")

    '''

def basic_strategy(player_hand, dealer_hand):
    # Get the value of the player's hand and the dealer's hand
    player_value = player_hand.value
    dealer_value = dealer_hand.value
    
    # Check if the player has a hard hand (no aces) or a soft hand (one or more aces)
    if player_hand.has_ace():
        # If the player has a soft hand, use a different strategy
        if player_value <= 17:
            return "hit"
        elif player_value == 18:
            if dealer_value in [2, 7, 8]:
                return "stand"
            else:
                return "hit"
        else:
            return "stand"
    else:
        # If the player has a hard hand, use a different strategy
        if player_value <= 11:
            return "hit"
        elif player_value == 12:
            if dealer_value in [4, 5, 6]:
                return "stand"
            else:
                return "hit"
        elif player_value >= 13 and player_value <= 16:
            if dealer_value in [2, 3, 4, 5, 6]:
                return "stand"
            else:
                return "hit"
        else:
            return "stand"



def play_blackjack_strategy(initial_bet):
    # Create a deck of cards and shuffle it
    deck = Deck()
    deck.shuffle()
    
    # Create a player and a dealer
    player = Player("Player")
    dealer = Dealer()
    
    # Set the player's bet to the initial bet
    bet = initial_bet
    
    # Deal the initial cards
    player.hand.add_card(deck.deal())
    player.hand.add_card(deck.deal())
    dealer.hand.add_card(deck.deal())
    dealer.hand.add_card(deck.deal())
    
    # Check for Blackjack
    if player.hand.value == 21:
        return bet
    elif dealer.hand.value == 21:
        return -bet
    
    # Player's turn
    while True:
        # Use the basic_strategy function to decide whether to hit or stand
        action = basic_strategy(player.hand, dealer.hand)
        if action == "hit":
            player.hand.add_card(deck.deal())
            if player.hand.value > 21:
                return -bet
        elif action == "stand":
            break
    
    # Dealer's turn
    while dealer.hand.value < 17:
        dealer.hand.add_card(deck.deal())
        if dealer.hand.value > 21:
            return bet
    
    # Compare the player's hand and the dealer's hand
    if player.hand.value > dealer.hand.value:
        return bet
    elif player.hand.value < dealer.hand.value:
        return -bet
    else:
        return 0


def play_strategy():
    # Set the initial bet and run the play_blackjack function 1000 times
    initial_bet = 100
    winnings = 0
    for i in range(100):
        result = play_blackjack_strategy(initial_bet)
        winnings += result

    #print(f"Total winnings: {winnings}€")
    return winnings


import matplotlib.pyplot as plt

total = 0
winnings = []
for i in range(100):
    new = play_strategy()
    total += new
    winnings.append(new)
print(f"Average winnings: {total/100}€")


plt.rcParams["figure.autolayout"] = True


plt.title("Line graph")
plt.plot(winnings, 'go', color="red", marker="o", markersize=3, markeredgecolor="red")
plt.axhline(y=total/100, color='b', linestyle='-')


plt.show()