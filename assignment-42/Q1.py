# Q1. Implement simple linear regression manually wihout using any ML libraries. 
# Dataset:
# X = [1, 2, 3, 4, 5]
# Y = [3, 4, 2, 4, 5]
# Tasks:
# Calculate:
# Mean of X (X̄) 
# Mean of Y (Ȳ)
# Slope (m) = Σ((X - X̄) * (Y - Ȳ)) / Σ((X - X̄)²)
# Intercept (c) = Ȳ - m * X̄
# Expected output:
# Mean of X: 3.0
# Mean of Y: 3.6
# Slope (m): 0.4
# Intercept (c): 2.4
# Regression line: Y = 0.4X + 2.4
# predicted value for X=6: Y = 4.8

def main():
    X = [1, 2, 3, 4, 5]
    Y = [3, 4, 2, 4, 5]

    # Calculate means
    mean_X = sum(X) / len(X)
    mean_Y = sum(Y) / len(Y)

    # Calculate slope (m)
    # dont use zip function
    numerator = sum((X[i] - mean_X) * (Y[i] - mean_Y) for i in range(len(X)))
    denominator = sum((X[i] - mean_X) ** 2 for i in range(len(X)))
    m = numerator / denominator

    # Calculate intercept (c)
    c = mean_Y - m * mean_X

    # Print results
    print(f"Mean of X: {mean_X}")
    print(f"Mean of Y: {mean_Y}")
    print(f"Slope (m): {m}")
    print(f"Intercept (c): {c}")
    print(f"Regression line: Y = {m}X + {c}")

    # Predict value for X=6
    predicted_Y = m * 6 + c
    print(f"Predicted value for X=6: Y = {predicted_Y}")

if __name__ == "__main__":
    main()