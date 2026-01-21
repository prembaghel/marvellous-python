# 2. write a program which accepts radius of circle and prints area.
import math

area_of_circle = lambda radius: math.pi * radius * radius

def main():
    radius = float(input("Enter radius of circle: "))
    area = area_of_circle(radius)
    print(f"Area of circle with radius {radius} is: {area}")

if __name__ == "__main__":
    main()

