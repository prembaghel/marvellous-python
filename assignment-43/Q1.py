# Q1. write linear regression from scratch using python for Advertising data. 
# The program should be able to fit a line to a given set of data points 
# follow given steps:


import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

def main():
    # Step 1: Load the data
    df = pd.read_csv('Advertising.csv')

    print("data", df.describe())

    # Step 2: Remove/Clean unwanted data
    if "Unnamed: 0" in df.columns:
        df.drop(columns=["Unnamed: 0"], inplace=True)

    # display data
    print(df.describe())

    print("correlation matrix:\n",df.corr())

    # Transform data in required format, Select the features and target
    X = df[['TV', 'radio', 'newspaper']]
    y = df['sales']

    print("independent variables X:", X.shape)
    print("independent variables y:", y.shape)
    #Step 3: Train model 
    # order of defining variables is important
    X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print("X_train shape:", X_train.shape)
    print("Y_train shape:", Y_train.shape)
    print("X_test shape:", X_test.shape)
    print("Y_test shape:", Y_test.shape)

    model = LinearRegression()
    model.fit(X_train, Y_train)

    #step 4: Test data
    Y_pred = model.predict(X_test)


    MSE = mean_squared_error(Y_test, Y_pred)
    RMSE = np.sqrt(MSE)
    R2 = r2_score(Y_test, Y_pred)
    
    print("Mean Squared Error:",MSE)
    print("Root Mean Squared Error:",RMSE)
    print("R2 squar:",R2)

    #Step 5: Display
    Result = pd.DataFrame({
        'Actual sale': Y_test.values,
        'Predicted sale': Y_pred
        })
    
    print("Result:\n", Result.head())

    
if __name__ == "__main__":
    main()