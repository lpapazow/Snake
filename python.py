from python_head import PythonHead
from settings import *
from python_body import *
from vector2d import *
from settings import *
from cell import *
import random


class Python():
    def __init__(self, coordinates, direction):
        self.head = PythonHead(coordinates, direction)
        self.body = [PythonBodyCell(self.head.next_piece_coordinates(), direction)]

    def move(self):
        self.body.insert(0, PythonBodyCell(self.head.coordinates, self.head.direction))
        self.head.coordinates = self.head.coordinates + self.head.movement_vector()
        self.body.pop(-1)

    def turn_head(self, direction):
        self.head.turn(direction)

    def tail_coordinates(self):
        return self.body[-1].coordinates

    def all_parts(self):
        snake = {}
        for body_part in [self.head] + self.body:
            snake[body_part.coordinates] = body_part
        return snake






