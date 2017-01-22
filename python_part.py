from settings import *
from cell import *
from vector2d import *

class PythonPart(Cell):
    def __init__(self, coordinates, direction):
        Cell.__init__(self)
        self.coordinates = coordinates
        self.direction = direction
        self.is_empty = False

    def movement_vector(self):
        return VECTOR_MOVEMENTS[self.direction]

    def next_piece_coordinates(self):
        return self.coordinates + VECTOR_MOVEMENTS[self.direction].reverse()
