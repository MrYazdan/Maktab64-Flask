class User:
    __users__ = {}

    def __init__(self, name, family) -> None:
        self.name = name
        self.family = family
        self.__id = len(self.__class__.__users__)
        self.__class__.__users__[self.__id] = self

    @property
    def id(self):
        return self.__id

    def __str__(self) -> str:
        return f"User ID {self.id} : {self.name} {self.family}"
