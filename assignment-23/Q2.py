# Q.2 Write a python program to implement a class named BankAccount with following requirements:
# - the class should contain two instance variables: Name and Amount
# - the class should contain one class variable: ROI initialized to 10.5
# - Define a constructor (__init__) that accept Name and initial Amount.
# - Implement following instance method :
#   -   Display() - display the Name and current Amount of the account
#   -   Deposit() - accept amount to be deposited from user and add the amount to current Amount
#   -   Withdraw() - accept amount from user to be withdrawn and deduct the amount from current Amount(when only sufficiant balance is available)
#   -   CalculateInterest() - calculate interest on current Amount based on ROI and display it. (Amount * ROI)/100

class BankAccount:
    ROI = 10.5  # Class variable

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print(f"Account Holder: {self.Name}, Current Amount: {self.Amount}")

    def Deposit(self):
        amount = float(input("Enter amount to deposit: "))
        self.Amount += amount
        print(f"Deposited: {amount}. New Amount: {self.Amount}")

    def Withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        if amount <= self.Amount:
            self.Amount -= amount
            print(f"Withdrawn: {amount}. New Amount: {self.Amount}")
        else:
            print("Insufficient balance!")

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        print(f"Interest on current Amount: {interest}")

obj1 = BankAccount("Prem", 1000)
obj1.Display()
obj1.Deposit()
obj1.Withdraw()
obj1.CalculateInterest()
