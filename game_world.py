from cell import *
from python import *
from utils import *
import os


class GameWorld():
    def __init__(self, size):
        self.matrix = [[Cell() for x in range(size)] for y in range(size)]
        self.python = None
    
    def add_python(self, python):
        self.python = python

    def print(self):
        os.system('clear')
        for coords, cell in self.python.all_parts().items():
            dims = math_to_python(coords)

            self.matrix[coords.x][coords.y] = cell
        res = ""
        for row in self.matrix:
            for cell in row:
                res += str(cell) + " "
            res += "\n"
        res2 = ""
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                dims = python_to_math(i, j)
                res2 += str(self.matrix[dims[0]][dims[1]]) + " "
            res2 += "\n"
        print(res2)

    # TODO: ACTUALLY START SPAWNING OBJECTS

    def turn_snake(self, direction):
        #TODO: FIX THE MATH INDICES TO 2D PYTHON ARRAY INDICES
        if direction == "RIGHT" and self.python.head.direction != "LEFT":
            self.python.turn_head("RIGHT")
        if direction == "UP" and self.python.head.direction != "DOWN":
            self.python.turn_head("UP")
        if direction == "LEFT" and self.python.head.direction != "RIGHT":
            self.python.turn_head("LEFT")
        if direction == "DOWN" and self.python.head.direction != "UP":
            self.python.turn_head("DOWN")

    def move_snake(self):
        #TODO CHECK IF SNAKE CRASHES 
        #TODO CHECK IF SNAKE MUNCHES //self.python.tail_coordinates shouldnt be removed
        self.python.tail_coordinates
        tail = self.python.tail_coordinates()
        self.python.move()
        self.matrix[tail.x][tail.y] = Cell()




