# coding=utf-8


class Suit(object):
    SPADES = 1
    CLUBS = 2
    DIAMONDS = 3
    HEARTS = 4
    icons = ['♠', '♣', '♦', '♥']
    blank = ['♤', '♧', '♢', '♡']


class Value(object):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    icons = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return Value.icons[self.value] + Suit.icons[self.suit]


class Stack(object):
    def __init__(self, *cards):
        self.cards = cards
