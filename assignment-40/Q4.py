# Q4. Create a new DataFrame with details of 5 new students.
# use the  trained model to predict the final result of these 5 students.
# Display the predicted results.

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
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    # Evaluate model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy is: {accuracy * 100:.2f}%")

    # Create new DataFrame for 5 new students
    new_students = pd.DataFrame({
        "StudyHours": [5.0, 3.0, 4.0, 2.0, 6.0],
        "Attendance": [60, 80, 80, 70, 85],
        "PreviousScore": [70, 65, 50, 50, 80],
        "AssignmentsCompleted": [1, 4, 1, 6, 1],
        "SleepHours": [7, 6, 8, 5, 7],
    })

    # Predict results for new students
    predictions = model.predict(new_students)
    print("Predicted results for new students:")
    print(predictions)

if __name__ == "__main__":
    main()
