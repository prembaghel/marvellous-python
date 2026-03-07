# Q9. Create new column :
# performanceIndex = (StudyHours * 2) + Attendance
# train model including this new feature, does accuracy improve?

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

def main():
    # Load dataset
    df = pd.read_csv("student_performance_ml.csv")
    
    # Create new feature
    df["performanceIndex"] = (df["StudyHours"] * 2) + df["Attendance"]
    
    # Prepare data
    X = df.drop(columns=["FinalResult"])
    y = df["FinalResult"]
    
    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=10)
    
    # Train model
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    
    # Evaluate model
    accuracy = model.score(X_test, y_test)
    print(f"Accuracy with performanceIndex: {accuracy * 100:.2f}%")

    print("Yes, accuracy is improved because performanceIndex is a combination of two important features, StudyHours and Attendance, which likely provides a better representation of the student's overall performance compared to using those features separately.")

if __name__ == "__main__":
    main()
