import random
from IPython.display import clear_output
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Ace':11, 'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10}

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
    
    def show_deck(self):
        
        for each_card in self.all_cards:
            print(each_card)


class Hand:
    
    def __init__(self):
        
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self, card):
        
        self.value += card.value
        
        if card.rank == 'Ace':
            self.aces += 1
        
        self.cards.append(card)
           
    def adjust_for_ace(self):
        
        while self.value > 21 and self.aces:
            self.aces -= 1
            self.value -= 10
                    
    def show_hand(self):
        
        for my_card in self.cards:
            print(my_card)
            

class Chips:
    
    def __init__(self):
        
        self.total = 100
        self.bet = 0
        
    def win_bet(self):
        
        self.total += self.bet
        
    def lose_bet(self):
        
        self.total -= self.bet

        
def take_bet(chips):
    
    while True:
        
        try:
            chips.bet = int(input(f"Enter your bet amount: "))
        except:
            print("Something went wrong, invalid entry!")
        else:  
            if chips.bet > chips.total:
                print("You don't have enough chips")
            else:
                break
    
def display_hand(player):
    
    pass

def hit(deck,hand):
    
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    
    global playing  # to control an upcoming while loop
    
    while True:
        
        choice = input("Please choose hit or stand 'h' or 's': ")
        
        if choice[0].lower() == 'h':
            hit(deck, hand)
            
        elif choice[0].lower() == 's':
            print("Player stands, now dealers turn")
            playing = False
            
        else:
            print("Incorrect entry, please try again")
            continue
            
        break

def show_some(player,dealer):
    
    pass
    
def show_all(player,dealer):
    
    pass

def player_busts():
    pass

def player_wins():
    pass

def dealer_busts():
    pass
    
def dealer_wins():
    pass
    
def push():
    pass
