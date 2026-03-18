# Q7. Write a python program using LinearRegression to train regression model using below dataset.
# StudyHours = [1 2 3 4 5]
# Marks = [50 55 60 65 70]

# Ans:
# consider equation Y = mX + C
# here Y = Marks, for X = StudyHours

import numpy as np
from sklearn.linear_model import LinearRegression

X = [1, 2, 3, 4, 5 ]
Y = [50, 55, 60, 65, 70]

X_mean = np.mean(X)
Y_mean = np.mean(Y)

n = len(X)
numerator = 0
denominator = 0

 # Y = mX + C
 # m = (summ (X - X_bar) * (Y - Y_bar) / (Summ (X - X_bar)) ** 2)
for i in range(n):
    numerator = numerator + ((X[i] - X_mean) * (Y[i]-Y_mean))
    denominator = denominator + ((X[i] - X_mean) ** 2)

m = numerator / denominator

print("Slop of line, m:", m)  


C = Y_mean - (m * X_mean)

print("Y intersect of line i.e. C:", C)

X_trans = np.array(X).reshape(-1, 1)
Y_trans = np.array(Y)
model = LinearRegression()
model.fit(X_trans, Y_trans)

Y_pred = model.predict([[6], [7]])

print("Y_pred:",Y_pred)


