from flask import Flask
from CreatorTeacher import CreatorTeacher

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello'

@app.route('/teacher')
def teacher():
    creator = CreatorTeacher()
    return creator.display()

if __name__ == "__main__":
    app.run()
