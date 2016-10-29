# Author: Bojan G. Kalicanin
# Date: 29-Oct-2016
# Represents a playing cards in pocker game

import random

class Card(object):
    """Represents a standard playing card."""
    
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank
        
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = ['None', 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10',
        'Jack', 'Queen', 'King']
        
    def __str__(self):
        return "{0:s} of {1:s}".format(Card.rank_names[self.rank],
            Card.suit_names[self.suit])
            
    def __lt__(self, other):
        # Check the suits
        if self.suit > other.suit:
            return True
        if self.suit < other.suit:
            return False
        # If suits are the same, check the rank
        if self.rank > other.rank:
            return True
        if self.rank < other.rank:
            return False
        
        # ranks are the same
        return False
        
    #def __lt__(self, other):
    #    t1 = self.suit, self.rank
    #    t2 = other.suit, other.rank
    #    return operator.lt(t1, t2)
    
class Deck(object):
    """Represents a deck of cards."""
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)
                
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
        
    def pop_card(self):
        # deal card from the bottom
        return self.cards.pop()
        
    def add_card(self, card):
        # add a Card
        self.cards.append(card)
        
    def shuffle(self):
        random.shuffle(self.cards)
        
    def sort(self):
        self.cards.sort()
        
    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())
            
    def deal_hands(self, n_hands, n_per_hand):
        hands = []
        for i in range(n_hands):
            hands.append(Hand(i))
            self.move_cards(hands[i], n_per_hand)
            
        return hands

class Hand(Deck):
    """Represents a hand of playing cards."""
    def __init__(self, label=''):
        self.cards = []
        self.label = label

# To create a Card, you call Card with the suit and rank of the card you want.
queen_of_dimonds = Card(1, 12)
new_deck = Deck()
print(str(new_deck))
print(new_deck.deal_hands(3, 5))