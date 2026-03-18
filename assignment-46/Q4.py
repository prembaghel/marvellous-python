# Q4. A regression model is given as:
# Salary = 12 * Experience + 25
# Calculate the predicted salary for the following experience values: [2, 5, 7]

# Ans:

def CalculateSalary(Val):
    return 12 * Val + 25

def main():
    ExperienceList = [2, 5, 7]
    for exp in ExperienceList:
        Result = CalculateSalary(exp)
        print(f"Predicted salary for {exp} years experience is {Result}K.")
    

if __name__ == "__main__":
    main()