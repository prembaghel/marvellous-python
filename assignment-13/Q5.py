# 5. write a program which accepts marks and displays grade.
def calculate_grade(marks):
    if marks >= 75:
        return 'Distinction'
    elif marks >= 60:
        return 'First Class'
    elif marks >= 50:
        return 'Second Class'
    elif marks < 50:
        return 'Fail'
    

def main():
    marks = float(input("Enter marks: "))
    grade = calculate_grade(marks)
    print(f"Grade for marks {marks} is: {grade}")

if __name__ == "__main__":
    main()
