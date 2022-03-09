from abc import ABCMeta, abstractmethod

class Book(object, metaclass=ABCMeta):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def display(self):
        pass

class MyBook(Book):
    def __init__(self, title, author, price):
        super(Book, self).__init__()
        self.price = price

    def display(self):
        print("Title:", title)
        print("Author:", author)
        print("Price:", price)

# class MyBook(Book):
#     def __init__(self,title,author,price):
#         Book.__init__(self,title,author)
#         self.price = price
#
#     def display(self):
#         print("Title:", self.title)
#         print("Author:", self.author)
#         print("Price:", self.price)

# class MyBook(Book):
#     def __init__(self, title, author, price):
#         super(MyBook, self).__init__(title, author)
#         self.price = price
#
#     def display(self):
#         print("Title: %s" % (self.title))
#         print("Author: %s" % (self.author))
#         print("Price: %s" % (self.price))

title = input()
author = input()
price = int(input())
new_novel = MyBook(title, author, price)
new_novel.display()
