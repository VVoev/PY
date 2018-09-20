class Animal():

    def __init__(self):
        print('Animal Created')

    def whoAmI(self):
        print('Animal')

    def eat(self):
        print('Eating')


class Dog(Animal):

    def __init__(self):
        print('Dog Created')

    def bark(self):
        print('Woof')

    def eat(self):
        print('Dog eating')


class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return 'Title: {}, Author: {}, Pages: {}'.format(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print('A book is destoyed')


dog = Dog()
dog.whoAmI()
dog.eat()
dog.bark()

book = Book('Duglas', 'Crockford', 200)
print(book)

print(len(book))
del book
