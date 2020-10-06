import json


class Library:
    def __init__(self):
        #data=[]
        try:
            with open("books.json", encoding="windows-1250") as jsonfile:
                self.books = json.load(jsonfile)
                #json.dump(self.books, jsonfile, ensure_ascii=False)

        except FileNotFoundError:
            self.books = []

    def all(self):
        return self.books

    def get(self, id):
        return self.books[id]

    def create(self, data):
        data.pop('csrf_token')
        self.books.append(data)

    def save_all(self):
        with open("books.json", "w") as f:
            json.dump(self.books, f, encoding="windows-1250")


    def update(self, id, data):
        data.pop('csrf_token')
        self.books[id] = data
        self.save_all()

    '''
    def get(self, id):
        todo = [todo for todo in self.all() if todo["id"] == id]
        if todo:
            return todo[0]
        return []

    def create(self, data):
        self.todos.append(data)
        self.save_all()

    def delete(self, id):
        todo = self.get(id)
        if todo:
            self.todos.remove(todo)
            self.save_all()
            return True
        return False

    def update(self, id, data):
        todo = self.get(id)
        if todo:
            index = self.todos.index(todo)
            self.todos[index] = data
            self.save_all()
            return True
        return False
'''
books = Library()