# Q9. Consider below data set 
Data = { 
        "StudyHours": [1,2,3,4,5],
        "SleepHours": [7,6,7,6,8],
        "Marks": [50,55,60,65,70]
    }
# write a pyton program to: 
# 1. Train a regression model using this dataset
# 2. print coefficient for both features
# 3. print the intercept

# Ans:

import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.DataFrame(Data)

print(df.head())

X = df[["StudyHours", "SleepHours"]]
Y = df["Marks"]

model = LinearRegression()

model.fit(X, Y)

print("Intercept:", model.intercept_)
print("Coefficnet:", model.coef_)

Y_pred = model.predict([[6,6]])

print("Y_pred", Y_pred)



