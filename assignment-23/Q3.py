# Q.3 Write a python program to implement a class named Numbers with following requirements:
# - the class should contain one instance variables: Value
# - Define a constructor (__init__) that accept initial Value from user and initialize Value.
# - Implement following instance method :
#   -   ChkPrime() - return True if Value is prime otherwise return False.
#   -   ChkPerfect() - return True if Value is perfect number otherwise return False.
#   -   Factors() - display all factors of number.
#   -   SumFactors() - return sum of all factors of number.

class Numbers:
    def __init__(self):
        self.Value = int(input("Enter initial value: "))

    def ChkPrime(self):
        if self.Value <= 1:
            return False
        for i in range(2, int(self.Value**0.5) + 1):
            if self.Value % i == 0:
                return False
        return True

    def ChkPerfect(self):
        sum_of_factors = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                sum_of_factors += i
        return sum_of_factors == self.Value

    def Factors(self):
        factors = []
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                factors.append(i)
        print(f"Factors of {self.Value}: {factors}")

    def SumFactors(self):
        sum_of_factors = 0
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                sum_of_factors += i
        return sum_of_factors
    
obj = Numbers()
print(f"Is {obj.Value} prime? {obj.ChkPrime()}")
print(f"Is {obj.Value} perfect? {obj.ChkPerfect()}")
obj.Factors()
print(f"Sum of factors of {obj.Value}: {obj.SumFactors()}")
