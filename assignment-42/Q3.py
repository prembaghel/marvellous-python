# Q3. Train linear regression model.
# predict salary for 6 years of experience
# Plot regression line using matplotlib
# Dataset:
# Experience (X) = [1, 2, 3, 4, 5]
# Salary (Y) = [20000, 25000, 30000, 35000, 40000]
# Expected output:
# Predicted salary for 6 years of experience: 45000
# Graph should Display:
# Data points (Experience vs Salary)
# Regression line

import matplotlib.pyplot as plt

def train_linear_regression(X, Y):
    # Calculate means
    mean_X = sum(X) / len(X)
    mean_Y = sum(Y) / len(Y)

    # Calculate slope (m)
    numerator = sum((X[i] - mean_X) * (Y[i] - mean_Y) for i in range(len(X)))
    denominator = sum((X[i] - mean_X) ** 2 for i in range(len(X)))
    m = numerator / denominator

    # Calculate intercept (c)
    c = mean_Y - m * mean_X

    return m, c

def predict_salary(m, c, years_of_experience):
    return m * years_of_experience + c

def plot_regression_line(X, Y, m, c):
    plt.scatter(X, Y, color='blue', label='Data points')
    plt.plot(X, [m * x + c for x in X], color='red', label='Regression line')
    plt.xlabel('Years of Experience')
    plt.ylabel('Salary')
    plt.title('Experience vs Salary')
    plt.legend()
    plt.show()

def main():
    # Dataset
    X = [1, 2, 3, 4, 5]
    Y = [20000, 25000, 30000, 35000, 40000]

    # Train model
    m, c = train_linear_regression(X, Y)

    # Predict salary for 6 years of experience
    predicted_salary = predict_salary(m, c, 6)
    print(f"Predicted salary for 6 years of experience: {predicted_salary}")

    # Plot regression line
    plot_regression_line(X, Y, m, c)

if __name__ == "__main__":
    main()