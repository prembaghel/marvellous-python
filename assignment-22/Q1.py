# Q1. Write a python program to implement a class named Demo with following specifications:
# - the class should contain two instance variables: no1 and no2
# - the class should contain one class variable named Value
# - Define a constructor (__init__) that accept two parameters and initialize the instance variables.
# - Implement two instace methods:
#  -   Fun() - displays the values of instance variables no1 and no2
#  -   Gun() - displays the values of instance variables no1 and no2 

# create two object of the demo class as follows:
# -   obj1 = Demo(11,21)
# -   obj2 = Demo(51,101)
# -   call the instace method in the given sequence
#    obj1.Fun()
#    obj2.Fun()
#    obj1.Gun()
#    obj2.Gun()


class Demo:
    Value = 0  # Class variable

    def __init__(self, no1, no2):
        self.no1 = no1  
        self.no2 = no2  

    def Fun(self):
        print(f"Fun Method: no1 = {self.no1}, no2 = {self.no2}")

    def Gun(self):
        print(f"Gun Method: no1 = {self.no1}, no2 = {self.no2}")

obj1 = Demo(11, 21)
obj2 = Demo(51, 101)

obj1.Fun()
obj2.Fun()
obj1.Gun()
obj2.Gun()
