from copy import copy
import json

import numpy as np

from Maze_Generator import Line


class Labyrinth:

    def __init__(self, rows: int, columns: int):
        self.__rows, self.__columns = rows, columns
        self.__key = 1
        self.__map_lab = self.CreateMap()
        # self._printMap()

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
        map_lab[-1].addEndLine()

        return np.array(map_lab)

    def serialize(self) -> np.ndarray:

        right_walls = ''
        bot_walls = ''

        for line in self.GetMap:

            for box in line.Elements:
                right_walls += str(int(box.Right))
                bot_walls += str(int(box.Bot))
            right_walls += 'e'
            bot_walls += 'e'

        return np.array([right_walls[:-1], bot_walls[:-1]])

    @staticmethod
    def _encodeLabyrinth(labyrinth) -> dict:

        if isinstance(labyrinth, Labyrinth):

            walls = []
            y = 0
            for line in labyrinth.GetMap:
                x = 0
                for box in line.Elements:
                    if box.Right:
                        walls.append({"__Wall__": True, "Type": "vertical", "X": x, "Y": y})
                    if box.Bot:
                        walls.append({"__Wall__": True, "Type": "horizontal", "X": x, "Y": y})

                    x += 1
                y += 1

            return {"__Labyrinth__": True, "name": "",
                    "rows": labyrinth.Rows, "columns": labyrinth.Columns, "walls": walls}
        else:
            type_name = labyrinth.__class__.__name__
            raise TypeError(
                f"Object of type '{type_name}' is not JSON serializable")

    def serializeToJSON(self) -> str:

        # encodedL = self._encodeLabyrinth()
        # json_labyrinth = json.dumps(encodedL)
        json_labyrinth = json.dumps(self, default=Labyrinth._encodeLabyrinth)

        return json_labyrinth

    def _printMap(self) -> None:
        map_lab = self.GetMap
        for line in map_lab:
            line.printLine()
