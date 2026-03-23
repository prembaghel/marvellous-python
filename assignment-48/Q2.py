# Q1. Write a python program that calculates the variance and standart deveiation for the following values:
# [6,7,8,9,10,11,12]

import numpy as np

X = [6,7,8,9,10,11,12]
X_mean = np.mean(X)
print("Mean:",X_mean)

X_deviation_square = []

for val in X:
    X_deviation_square.append((val-X_mean)**2)

sum_of_square = sum(X_deviation_square)
print("sum_of_square:", sum_of_square )

# Variance = sum(X-mean)^2 / n
Variance = sum(X_deviation_square) / len(X)
print("Variance:", Variance)


# Standart Deviation = √variance
StandartDeviation = np.sqrt(Variance)
print("Standart Deviation:", StandartDeviation)