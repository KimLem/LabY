from Maze_Generator.Fellowship import *


class Box:
    _numbers_ = 0

    # def __new__(cls, *args):
    #     if cls.numbers == 0:
    #         print("This is the first instance of the class Box")
    #
    #     return super(Box, cls).__new__(cls)

    def __init__(self, info: str = 'info'):
        """Constructor of Box class"""
        self.info = info
        self._numbers()
        self._set = Fellowship()
        [self.__setattr__(i, False) for i in ['_bot', '_right', '_marked', '_player']]

    @classmethod
    def _numbers(cls) -> None:
        """Counts every call to the class constructor"""
        cls._numbers_ += 1

    @classmethod
    def resetBoxes(cls) -> None:
        print(f'Numbers of Boxes: {(1 + cls._numbers_):.1f}')
        cls._numbers_ = 0

    @property
    def Set(self) -> int:
        return self._set.Name_set

    @Set.setter
    def Set(self, value: int) -> None:
        self._set.Name_set = value

    @property
    def Set_member(self) -> Fellowship:
        return self._set

    @Set_member.setter
    def Set_member(self, value: Fellowship) -> None:
        self._set = self._set + value

    @property
    def Bot(self) -> bool:
        return self._bot

    @Bot.setter
    def Bot(self, value: bool) -> None:
        self._bot = value

    @property
    def Right(self) -> bool:
        return self._right

    @Right.setter
    def Right(self, value: bool) -> None:
        self._right = value

    # field for player#1
    @property
    def Marked(self) -> bool:
        return self._marked

    @Marked.setter
    def Marked(self, value: bool) -> None:
        self._marked = value

    # field for player#2
    @property
    def Player(self) -> bool:
        return self._player

    @Player.setter
    def Player(self, value: bool) -> None:
        self._player = value


class EnhancedBox(Box):
    def __init__(self, features: tuple):
        """Constructor"""
        super(EnhancedBox, self).__init__()
        [self.__setattr__(feature, True) for feature in features]

    def getFeature(self, name: str) -> bool:
        return self.__getattribute__(name)

