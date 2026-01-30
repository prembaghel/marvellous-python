# Q2. Write a python program to implement a class named Circle with following requirements:
# - the class should contain three instance variables: Radius Area and Circumference
# - the class should contain one class variable named PI, initialized to 3.14
# - Define a constructor (__init__) that initialize the instance variable to 0.0
# - Implement two instace methods:
#  -   Accept() - accept radius of circle from user
#  -   CalculateArea() - calculate the area of circle and store it in instance variable Area
#  -   CalculateCircumference() - calculate the circumference of circle and store it in variable Circumference
#  -   Display() - display the radius, area and circumference of circle

# create multiple objects of circle class and invoke all instance methods for each object



class Circle:
    PI = 3.14 # Class variable

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        self.Radius = float(input("Enter the radius of the circle: "))       
    
    def CalculateArea(self):
        self.Area = Circle.PI * (self.Radius ** 2)
    
    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    def Display(self):
        print(f"Radius: {self.Radius}")
        print(f"Area: {self.Area}")
        print(f"Circumference: {self.Circumference}")

c1 = Circle()
c1.Accept()
c1.CalculateArea()
c1.CalculateCircumference()
c1.Display()

c2 = Circle()
c2.Accept()
c2.CalculateArea()
c2.CalculateCircumference()
c2.Display()


    
    