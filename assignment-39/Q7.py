# Q7. Use the trained model to predict the result for a student with :
# StudyHours = 6, Attendance = 85, PreviousScore = 66, AssignmentsCompleted = 7, SleepHours = 7.
# will the student pass or fail.

from sklearn.tree import DecisionTreeClassifier
import pandas as pd     

def main():
    df = pd.read_csv("student_performance_ml.csv")
    X = df.drop(columns="FinalResult")
    y = df["FinalResult"]
    model = DecisionTreeClassifier(max_depth=3)
    model.fit(X, y)

    # Predicting for the new student
    new_student = pd.DataFrame({
        "StudyHours": [6],
        "Attendance": [85],
        "PreviousScore": [66],
        "AssignmentsCompleted": [7],
        "SleepHours": [7]
    })

    prediction = model.predict(new_student)
    if prediction[0] == 1:
        print("The student will pass.")
    else:
        print("The student will fail.")

if __name__ == "__main__":
    main()
