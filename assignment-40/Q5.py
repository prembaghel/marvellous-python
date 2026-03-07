# Q5. Without using accuracy score, manually calculate accuracy.
# verify your result with accuracy_score function.

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def main():
    # Load dataset
    df = pd.read_csv("student_performance_ml.csv")

    # Select features
    X = df.drop(columns=["FinalResult"])
    y = df["FinalResult"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Train model
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    # Predict results
    y_pred = model.predict(X_test)

    # Manually calculate accuracy
    correct_predictions = sum(y_pred == y_test)
    total_predictions = len(y_test)
    manual_accuracy = correct_predictions / total_predictions
    print(f"Manually Calculated Accuracy: {manual_accuracy * 100:.2f}%")

    # Verify with accuracy_score function
    sklearn_accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy from accuracy_score function: {sklearn_accuracy * 100:.2f}%")

if __name__ == "__main__":
    main()
