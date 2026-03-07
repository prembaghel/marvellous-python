# Q2. Use the trained model to result for X_test and print the predicted results along with the actual results.

from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from sklearn.model_selection import train_test_split

def main():
    df = pd.read_csv("student_performance_ml.csv")
    
    X = df.drop("FinalResult", axis=1)
    y = df["FinalResult"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
   
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    print("Model trained successfully.")
    y_pred = model.predict(X_test)
    print("Predicted results:", y_pred)
    print("Actual results:", y_test.values)

if __name__ == "__main__":
    main()
