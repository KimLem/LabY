import numpy as np
from Maze_Generator import Box
from copy import deepcopy


class Line:
    __new = True

    def __init__(self, n: int, line: np.ndarray = None, info: str = 'info'):
        """Constructor"""
        self.__n = n
        if Line.__new:
            line = Line._fillEmptyValue(self.__n)
            Line.__new = False
        else:
            line = Line._prepareNewLine(line)
        self.line = line

    def __copy__(self):
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__.update(self.__dict__)
        return result

    def __deepcopy__(self, memodict={}):
        cls = self.__class__
        result = cls.__new__(cls)
        memodict[id(self)] = result
        for k, v in self.__dict__.items():
            setattr(result, k, deepcopy(v, memodict))
        return result

    @property
    def Elements(self) -> np.ndarray:
        return self.line

    @Elements.setter
    def Elements(self, value: np.ndarray) -> None:
        self.line = value

    def assignUniqueSet(self, key: int) -> int:

        for box in self.line:
            if box.Set == 0:
                box.Set = key
                key += 1
        # print(f'Now the row {i:.1f} is unique')
        return key

    def addRightWalls(self) -> None:
        for i in range(len(self.line) - 1):
            random_choice = np.random.randint(0, 2, dtype=bool)
            if random_choice or self.line[i].Set == self.line[i + 1].Set:
                self.line[i].Right = True
            else:
                self._mergeSet(i)
        self.line[-1].Right = True
        # print(f'Right walls were added')

    def addBottomWalls(self) -> None:

        for box in self.line:
            random_choice = np.random.randint(0, 2, dtype=bool)
            # Maybe this condition can be removed, because bottom_walls cover it
            members_condition = box.Set_member.Members_number > 1
            bottom_walls_condition = box.Set_member.Numbers_of_set_feature == (box.Set_member.Members_number - 1)
            if random_choice and members_condition and not bottom_walls_condition:
                box.Bot = True
                box.Set_member.Numbers_of_set_feature += 1
        # print(f'Bottom walls were added')

    def addEndLine(self) -> None:

        for i in range(len(self.line) - 1):
            self.line[i].Bot = True
            if self.line[i].Set != self.line[i + 1].Set:
                self.line[i].Right = False
                self._mergeSet(i)
        self.line[- 1].Bot = True

    def printLine(self) -> None:
        string_line = ''
        for box in self.line:
            try:
                left_elem = f'l' if box.getFeature('left') else f''
                string_line += left_elem

            except AttributeError:
                pass

            try:
                top_elem = f'+' if box.getFeature('top') else f''
                string_line += top_elem
            except AttributeError:
                pass

            bot_elem = f'_{box.Set}_' if box.Bot else f'{box.Set}'
            right_elem = '|' if box.Right else ' '
            string_line += bot_elem + right_elem
        print(string_line, '\n')

    def _mergeSet(self, index: int) -> None:

        for box in self.line:
            if box.Set == self.line[index + 1].Set:
                box.Set_member = self.line[index].Set_member
                # print(f'Numbers of set of the Box: {box.Set} were changed')
        # print(f'Boxes sets of rhe line were merged')

    @staticmethod
    def _fillEmptyValue(columns: int) -> np.ndarray:
        # first_line = [Box.Box() for _ in range(columns)]

        first_line = np.array([Box.EnhancedBox(('left', 'top'))])
        first_line = np.append(first_line, [Box.EnhancedBox(('top',)) for _ in range(columns - 1)])
        # print(f'Empty line was filled for {columns:.1f} columns')
        # Box.resetBoxes()
        return first_line

    @staticmethod
    def _prepareNewLine(line: np.ndarray) -> np.ndarray:

        new_line = deepcopy(line)
        for i, box in enumerate(line):
            new_line[i] = Box.Box() if i != 0 else Box.EnhancedBox(('left',))
            if not box.Bot:
                # new_line[i].Set_member = box.Set_member
                new_line[i].Set = box.Set
                # # Need to rewrite following conditions,
                # # because set the wrong number of members in the set for each box in line
                # new_line[i].Set_member.Members_number = 1
                # new_line[i].Set_member.Numbers_of_set_feature = 0

        return new_line

    @classmethod
    def renewClassLine(cls) -> None:
        cls.__new = True
        print('Now Class line is renewable')
