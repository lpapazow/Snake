# Converts standard mathematical coord system to out 2D python array indices

from vector2d import *

def math_to_python(vector2d):
    return (vector2d.y, vector2d.x)

def python_to_math(x, y):
    return (y, -1 * x)