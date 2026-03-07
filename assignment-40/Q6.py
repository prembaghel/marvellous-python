# Q6. Identify students where:
# y_test != y_pred
# Display those rows.
# How many students were misclassified?
# what common pattern do you observe?

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
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    # Train model
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    # Predict results
    y_pred = model.predict(X_test)

    # Identify misclassified students
    misclassified = df.loc[y_test.index[y_test != y_pred]]
    print("Misclassified Students:")
    print(misclassified)

    # Count misclassified students
    misclassified_count = misclassified.shape[0]
    print(f"Number of Misclassified Students: {misclassified_count}")

    # Observe common patterns
    common_patterns = misclassified.describe(include='all')
    print("Common Patterns in Misclassified Students:")
    print(common_patterns)

if __name__ == "__main__":
    main()
