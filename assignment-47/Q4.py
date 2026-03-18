# Q2. Consider the Dataset: 5,7,9,11,13
# perform following steps:
# - calculate mean
# - find the deviation of each value from the mean
# - calculate the square of each deviation
# - calculate the variance of dataset

# Ans:
import math

X = [5,7,9,11,13]
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

# 5. Standart Deviation = √variance
SD = math.sqrt(Variance)
print("Standard Deviation:", SD)