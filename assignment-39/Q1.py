# Q1. Import decision tree classifier from sklearn.
# create a model object and train it using fit().

from sklearn.tree import DecisionTreeClassifier
import pandas as pd

def main():
    df = pd.read_csv("student_performance_ml.csv")
    X = df.drop("FinalResult", axis=1)
    y = df["FinalResult"]
    model = DecisionTreeClassifier()
    model.fit(X, y)
    print("Model trained successfully.")

if __name__ == "__main__":
    main()