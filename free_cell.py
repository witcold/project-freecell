# coding=utf-8
from classes import Stack


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
            self.cells += Cell()
        self.foundations = []
        for _ in xrange(4):
            self.foundations += Foundation()
        self.cascades = []
        for _ in xrange(8):
            self.cascades += Cascade()
        # TODO fill cascades with cards
