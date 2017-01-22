from vector2d import *

def opposite(direction):
    if "UP":
        return "DOWN"
    elif "DOWN":
        return "UP"
    elif "RIGHT":
        return "LEFT"
    elif "LEFT":
        return "RIGHT"
    return "Invalid direction"

UP = "UP"
LEFT = "LEFT"
DOWN = "DOWN"
RIGHT = "RIGHT"

HEAD_SYMBOLS = {
    'UP':"^",
    'LEFT': "<",
    'DOWN': "v",
    'RIGHT': ">"
}

VECTOR_MOVEMENTS = {
    'UP':Vector2D(0, 1),
    'LEFT': Vector2D(-1, 0),
    'DOWN': Vector2D(0, -1),
    'RIGHT': Vector2D(1, 0)
}

