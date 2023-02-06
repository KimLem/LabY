class Fellowship:

    def __init__(self, info: str = 'info'):
        """Constructor"""
        self.__name_set = 0
        self.__members_number = 1
        self.__numbers_of_set_feature = 0
        self.__absolutely_len = 1

    def __add__(self, other):
        self.__members_number = self.__members_number + other.__members_number
        self.__numbers_of_set_feature = self.__numbers_of_set_feature + other.__numbers_of_set_feature
        self.__name_set = other.__name_set
        self.__absolutely_len = self.__absolutely_len + other.__absolutely_len

        return self

    def __len__(self) -> int:
        return self.__absolutely_len

    @property
    def Name_set(self) -> int:
        return self.__name_set

    @Name_set.setter
    def Name_set(self, value: int) -> None:
        self.__name_set = value

    @property
    def Members_number(self) -> int:
        return self.__members_number

    @Members_number.setter
    def Members_number(self, value: int) -> None:
        self.__members_number = value
        self.__absolutely_len += value

    @property
    def Numbers_of_set_feature(self) -> int:
        return self.__numbers_of_set_feature

    @Numbers_of_set_feature.setter
    def Numbers_of_set_feature(self, value: int):
        self.__numbers_of_set_feature = value
