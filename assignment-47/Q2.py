# Q2. Consider the Dataset: 4, 6, 8, 10, 12
# perform following steps:
# - calculate mean
# - find the deviation of each value from the mean
# - calculate the square of each deviation
# - calculate the variance of dataset

# Ans:
X = [4, 6, 8, 10, 12]
# 1: Calculate Mean
Mean = sum(X) / len(X)
print("Mean:", Mean)

# 2. Deviation of each value
X_deviation = []
for val in X:
    val = val - Mean
    X_deviation.append(val)
print("Deviation:", X_deviation)

# 3. Square of deviation
X_deviation_square = []
for val in X_deviation:
    X_deviation_square.append(val**2)
print("Square of deviation:", X_deviation_square)

# 4. Variance of dataset:
# Variance = sum(X-mean)^2 / n

Variance = sum(X_deviation_square) / len(X)
print("Variance:", Variance)