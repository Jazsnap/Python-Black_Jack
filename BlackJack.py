import random
from IPython.display import clear_output
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Ace':11, 'Ace_lo':1, 'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace_hi':14}
player_hand = []
dealer_hand = []

class Card:
    
    def __init__(self,rank,suit):
    
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        
        return self.rank + " of " + self.suit

class Deck:

    def __init__(self):
        
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(rank,suit))
                
    def shuffle(self):
        
         random.shuffle(self.all_cards)
            
    def deal(self):
        
        new_card = self.all_cards.pop()
        return new_card


class Hand:
    
    def __init__(self):
        
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self, card):
        
        new_card = Deck.deal()
        
        if new_card.rank == 'Ace':
            self.aces += 1
        else:
            pass
        
        self.cards.append(new_card)
           
    def adjust_for_ace(self):
        
        if self.aces != 0:
            for aces in self.cards:
                try:
                    choice = input(f"Ace high or low? for {self.card}: ")
                    if choice not in ["high","low"]:
                        clear_output()
                        continue
                    elif choice == "high":
                        self.value = values['Ace_hi']
                        print(f"{self.card} has value of {self.value}")
                    elif choice == "low":
                        self.value = values['Ace_lo']
                        print(f"{self.card} has value of {self.value}")
                except:
                    print("Only 'High' or 'low' allowed")
                    
pack = Deck()
pack.shuffle()