# coding=utf-8
from enum import Enum
from random import shuffle


class Suit(Enum):
    __order__ = 'SPADES CLUBS DIAMONDS HEARTS'
    SPADES = '♠'
    CLUBS = '♣'
    DIAMONDS = '♦'
    HEARTS = '♥'


class Value(Enum):
    __order__ = 'ACE TWO THREE FOUR FIVE SIX SEVEN EIGHT NINE TEN JACK QUEEN KING'
    ACE = 'A'
    TWO = '2'
    THREE = '3'
    FOUR = '4'
    FIVE = '5'
    SIX = '6'
    SEVEN = '7'
    EIGHT = '8'
    NINE = '9'
    TEN = '10'
    JACK = 'J'
    QUEEN = 'Q'
    KING = 'K'


class Card(object):
    def __init__(self, suit, value):
        """Creates a Card.

        :type suit: Suit
        :type value: Value
        :rtype: Card
        """
        self.suit = suit
        self.value = value

    def __repr__(self):
        return self.value.value + self.suit.value


class Stack(object):
    def __init__(self):
        self.cards = []

    def __getitem__(self, item):
        return self.cards.__getitem__(item)

    def __iter__(self):
        return self.cards.__iter__()

    def __len__(self):
        return self.cards.__len__()

    def append(self, card):
        self.cards.append(card)


class Deck(Stack):
    def __init__(self):
        self.cards = []
        for suit in Suit:
            for value in Value:
                self.cards.append(Card(suit, value))

    def shuffle(self):
        shuffle(self.cards)
