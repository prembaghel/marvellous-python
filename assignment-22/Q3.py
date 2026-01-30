# Q3. Write a python program to implement a class named Arithmetic with following characteristics:
# - the class should contain two instance variables: Value1 and Value2
# - Define a constructor (__init__) that initialize the instance variable to 0
# - Implement following instance methods:
#  -   Accept() - accept values for Value1 and Value2 from user
#  -   Addition() - return addition of Value1 and Value2
#  -   Subtraction() - return subtraction of Value1 and Value2
#  -   Multiplication() - return multiplication of Value1 and Value2
#  -   Division() - return division of Value1 and Value2(handle divid by zero)

# create multiple objects of Arithmetic class and invoke all instance methods for each object

class Arithmetic:
    
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0
       
    def Accept(self):
        self.Value1 = int(input("Enter the first value: "))
        self.Value2 = int(input("Enter the second value: "))

    def Addition(self):
        return self.Value1 + self.Value2

    def Subtraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2

    def Division(self):
        if self.Value2 != 0:
            return self.Value1 / self.Value2
        else:
            return "Division by zero error"

a1 = Arithmetic()
a1.Accept()
print(f"Addition: {a1.Addition()}")
print(f"Subtraction: {a1.Subtraction()}")
print(f"Multiplication: {a1.Multiplication()}")
print(f"Division: {a1.Division()}")

a2 = Arithmetic()
a2.Accept()
print(f"Addition: {a2.Addition()}")
print(f"Subtraction: {a2.Subtraction()}")
print(f"Multiplication: {a2.Multiplication()}")
print(f"Division: {a2.Division()}")