from Maze_Generator.Labyrinth import *
import numpy as np


def main():

    pu = Labyrinth(3, 5)
    s = pu.serializeToJSON()
    pu._printMap()


if __name__ == '__main__':
    main()
