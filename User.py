from abc import ABC, abstractmethod


class User(ABC):
    name: str
    surname: str

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @abstractmethod
    def showPage(self):
        pass
