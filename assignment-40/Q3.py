# Q3. Train the model using only:
# StudyHours, Attendance
# compare the accuracy score with full feature model.
# is model still performing well?

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def main():
    # Load dataset
    df = pd.read_csv("student_performance_ml.csv")

    # Select features
    X = df[["StudyHours", "Attendance"]]
    y = df["FinalResult"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Train model
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    # Evaluate model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy with only StudyHours and Attendance: {accuracy * 100:.2f}%")
    print("As I observed model still performing well.")

if __name__ == "__main__":
    main()