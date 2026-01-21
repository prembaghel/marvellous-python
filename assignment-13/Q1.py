# 1. write a program which accepts length and width of rectangle and prinnts area.

area_of_rectangle = lambda length, width: length * width
    
def main():
    print("Enter length and width of rectangle:")
    length = float(input("Length: "))
    width = float(input("Width: "))
    area = area_of_rectangle(length, width)
    print(f"Area of rectangle with length {length} and width {width} is: {area}")

if __name__ == "__main__":
    main()
