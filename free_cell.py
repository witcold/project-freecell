# coding=utf-8
from itertools import izip
from classes import Stack, Deck
from utils import chunks


class Foundation(Stack):
    pass


class Cascade(Stack):
    pass


class Cell(Stack):
    pass


class Game(object):
    def __init__(self):
        self.cells = []
        for _ in xrange(4):
            self.cells.append(Cell())
        self.foundations = []
        for _ in xrange(4):
            self.foundations.append(Foundation())
        self.cascades = []
        for _ in xrange(8):
            self.cascades.append(Cascade())
        # TODO fill cascades with cards
        deck = Deck()
        deck.shuffle()
        for chunk in chunks(deck, 8):
            for cascade, card in izip(self.cascades, chunk):
                cascade.append(card)

    def show(self):
        depths = [len(x) for x in self.cascades]
        max_depth = max(depths)
        for i in xrange(max_depth):
            for j, cascade in enumerate(self.cascades):
                if i < depths[j]:
                    print cascade[i],
                else:
                    print '  ',
            print

if __name__ == '__main__':
    Game().show()
