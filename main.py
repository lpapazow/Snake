from game_world import *

gmwrld = GameWorld(15)
gmwrld.add_python(Python(Vector2D(2, 2), "UP"))

while True:
    gmwrld.print()
    inpt = input("Press W, A, S, D for turn, G for move:\n Then press enter")
    if inpt == "W":
        gmwrld.turn_snake("UP")
    elif inpt == "D":
        gmwrld.turn_snake("DOWN")
    elif inpt == "A":
        gmwrld.turn_snake("LEFT")
    elif inpt == "D":
        gmwrld.turn_snake("RIGHT")
    elif inpt == "G":
        gmwrld.move_snake()
    sleep(0.2)
