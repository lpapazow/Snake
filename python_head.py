import settings
from python_part import *

class PythonHead(PythonPart):
    def __init__(self, coordinates, direction):
        PythonPart.__init__(self, coordinates, direction)
        self.symbol = settings.HEAD_SYMBOLS[direction]

    def turn(self, direction):
        self.direction = direction
        self.symbol = settings.HEAD_SYMBOLS[direction]

    def __str__(self):
        return self.symbol

    def __repr__(self):
        return self.symbol
