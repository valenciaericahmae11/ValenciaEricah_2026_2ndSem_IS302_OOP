class Book:
    def __init__(self, title, author, year):
        self.title_EIV = title
        self.author_EIV = author
        self.year_EIV = year

    def display_book(self):
        print("Title:", self.title_EIV)
        print("Author:", self.author_EIV)
        print("Year:", self.year_EIV)
        print()


book1 = Book("Python Programming", "John Smith", 2022)
book2 = Book("Learning OOP", "Ana Cruz", 2023)
book3 = Book("Data Structures", "Mark Lee", 2021)

book1.display_book()
book2.display_book()
book3.display_book()

