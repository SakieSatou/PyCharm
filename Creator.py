from abc import ABC, abstractmethod
from User import User


class Creator(ABC):
    html: str

    def makeHeader(self):
        self.html = '<div style-"width:500px;height:100px;border:1px solid red;"></div>'

    @abstractmethod
    def FactoryMethod(self):
        pass

    def makeContent(self):
        user = self.FactoryMethod()

        self.html += '<div style-"width:500px;height:300px;border:1px solid green;">'
        self.html += user.showPage()
        self.html += '</div>'

    def display(self):
        self.makeHeader()
        self.makeContent()
        return self.html
