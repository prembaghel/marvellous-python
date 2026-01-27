# Q1. write a program which contains one function named Add(). which accepts two numbers from user and return addition of that two numbers.
def Add(a, b):
    return a + b    

def main():
    print("Enter first number:")
    no1 = int(input())
    print("Enter second number:")
    no2 = int(input())
    
    ret = Add(no1, no2)
    
    print("Addition is:", ret)

if __name__ == "__main__":
    main()
    
