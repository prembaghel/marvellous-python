# Q2. Using same Dataset from Q1, calculate model performance,
# Tasks:
# 1. Predict all Y values using regression equation
# 2. Calculate Mean squared error (MSE) = (1/n) * Σ((Y - Y_pred)²)
# 3. Calculate R-squared (R²) = 1 - (Σ((Y - Y_pred)²) / Σ((Y - Ȳ)²))


def main():
    X = [1, 2, 3, 4, 5]
    Y = [3, 4, 2, 4, 5]

    # Calculate means
    mean_X = sum(X) / len(X)
    mean_Y = sum(Y) / len(Y)

    # Calculate slope (m)
    numerator = sum((X[i] - mean_X) * (Y[i] - mean_Y) for i in range(len(X)))
    denominator = sum((X[i] - mean_X) ** 2 for i in range(len(X)))
    m = numerator / denominator

    # Calculate intercept (c)
    c = mean_Y - m * mean_X

    # Predict Y values formula Y = mX + c
    Y_pred = [m * x + c for x in X]

    # Calculate Mean Squared Error (MSE)
    # MSE = (1/n) * Σ((Y - Y_pred)²)
    mse = sum((Y[i] - Y_pred[i]) ** 2 for i in range(len(Y))) / len(Y)

    # Calculate R-squared (R²) = 1 - (Σ((Y - Y_pred)²) / Σ((Y - Ȳ)²))
    ss_total = sum((Y[i] - mean_Y) ** 2 for i in range(len(Y)))
    ss_residual = sum((Y[i] - Y_pred[i]) ** 2 for i in range(len(Y)))
    r_squared = 1 - (ss_residual / ss_total)

    # Print results
    print(f"Mean squared error (MSE): {mse}")
    print(f"R-squared (R²): {r_squared}")

if __name__ == "__main__":
    main()