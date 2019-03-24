import random
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

# Class Card


class Card:

    def __init__(self, suit, card):
        self.suit = suit
        self.card = card

    def __repr__(self):
        return f'{self.card} of {self.suit}'


class Deck:

    def __init__(self):
        for suit in suits:
            for card in cards:
                self.cards[suit] = card

    def __repr__(self):
        return f'Deck of {self.count()} cards'

    def count(self):
        return len(self.cards)

    def _deal(self, number):
        if self.count() == 0:
            raise ValueError('All cards have been dealt')

        if number > self.count():
            self.cards.clear()

        if number == 1:
            return self.cards.popitem()

        return_list = []
        for i in range(number):
            return_list.append(self.cards.popitem())

        return return_list

    def shuffle(self):
        if self.count() != 52:
            raise ValueError('Only full decks can be shuffled')

        return random.shuffle(self.cards)

    def deal_card(self):
        return self._deal(1)

    def deal_hand(self, number):
        return self._deal(number)
