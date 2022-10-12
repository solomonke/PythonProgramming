# Constructors
# This is a function inside a class
# It is called the __init__ class
# It is used to initialize attributes of a class
# A class contains attributes/properties/states and behaviors/methods

class Book:
    def __init__(self, author, title, price, quantity):
        self.author = author
        self.title = title
        self.price = price
        self.quantity = quantity

    def show_book(self):
        print(f"The author is {self.author}, The title is {self.title}, The price is {self.price}, and the quantity is {self.quantity}")

book1 = Book("James", "Python Programming", "$10", "20")
print(book1.price)
book1.show_book()
