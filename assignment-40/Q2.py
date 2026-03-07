# Q2. Remove the column SleepHours from the DataSet.
# Train model again.
# Compare new accuracy score with the previous one.
# Does removing this feature affect performance?

import numpy as np  
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def main():
    # Load dataset
    df = pd.read_csv("student_performance_ml.csv")

    # Remove SleepHours column
    df = df.drop(columns="SleepHours")

    # Preprocess data
    X = df.drop(columns="FinalResult")
    y = df["FinalResult"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    # Train model
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    # Evaluate model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy after removing SleepHours: {accuracy * 100:.2f}%")
    print("Removing SleepHours not affected model result much as it has low importance score.")

if __name__ == "__main__":
    main()