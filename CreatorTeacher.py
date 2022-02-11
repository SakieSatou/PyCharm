from Creator import Creator
from Teacher import Teacher


class CreatorTeacher(Creator):
    def FactoryMethod(self):
        return Teacher('Сакиэ', 'Сато')
