from User import User


class Teacher(User):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def showPage(self):
        html = '<h1>страница преподователя</h1>'
        html += f'Фамилия: { self.surname }<br>'
        html += f'Имя: {self.name}<br>'

        return html
