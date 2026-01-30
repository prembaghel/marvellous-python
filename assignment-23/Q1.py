# Q.1 Write a python program to implement a class named BookStore with following requirements:
# - the class should contain two instance variables: Name and Author
# - the class should contain one class variable: noOfBooks initialized to 0
# - Define a constructor (__init__) that accept Name and Author and initialize the instance variables.
# - Inside the constructor increment the class variable noOfBooks by 1 whenever a new object is created.
# - Implement instance method Display() - display the Name and Author of the book

# Example :
# obj1 = BookStore("Linux system programing","Robert Love")
# obj1.display() -> Linux system programing by Robert Love. No of books : 1
# obj2 = BookStore("Python Programming","Guido van Rossum")
# obj2.display() -> Python Programming by Guido van Rossum. No of books : 2

class BookStore:
    noOfBooks = 0  # Class variable

    def __init__(self, Name, Author):
        self.Name = Name
        self.Author = Author
        BookStore.noOfBooks += 1  # Increment class variable

    def Display(self):
        print(f"{self.Name} by {self.Author}. No of books : {BookStore.noOfBooks}")

obj1 = BookStore("Linux system programing", "Robert Love")
obj1.Display()  # Linux system programing by Robert Love. No of books : 1

obj2 = BookStore("Python Programming", "Guido van Rossum")
obj2.Display()  # Python Programming by Guido van Rossum. No of books : 2
