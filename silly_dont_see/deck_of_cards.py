suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

# Class Card


class Card:

    def __init__(self, suit, card):
        self.suit = suit
        self.card = card

    def __repr__(self):
        return f'{self.card} of {self.suit}'
