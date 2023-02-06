from copy import copy

import numpy as np

from Maze_Generator import Line


class Labyrinth:

    def __init__(self, rows: int, columns: int):
        self.__rows, self.__columns = rows, columns
        self.__key = 1
        self.__map_lab = self.CreateMap()
        self._printMap()

    @property
    def Rows(self) -> int:
        return self.__rows

    @property
    def Columns(self) -> int:
        return self.__columns

    @property
    def Key(self) -> int:
        return self.__key

    @Key.setter
    def Key(self, value: int) -> None:
        self.__key = value

    @property
    def GetMap(self) -> np.ndarray:
        return self.__map_lab

    def CreateMap(self) -> np.ndarray:
        map_lab = []
        line_elements = None
        for _ in range(self.Rows):
            line = Line.Line(self.Columns, line=line_elements)
            self.Key = line.assignUniqueSet(self.Key)
            line.addRightWalls()
            line.addBottomWalls()
            map_lab.append(copy(line))
            line_elements = line.Elements

        Line.Line.renewClassLine()
        map_lab[- 1].addEndLine()

        return np.array(map_lab)

    def _printMap(self) -> None:
        map_lab = self.__map_lab
        for line in map_lab:
            line.printLine()
