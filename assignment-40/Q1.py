# Q1. After training decision tree model use:
# model.feature_importances_
# Display important score of each feature
# which feature contribute the most in predicting final result?
# which feature contribute the least?

import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

def main():
    # Load dataset
    df = pd.read_csv("student_performance_ml.csv")

    # Preprocess data
    X = df.drop(columns="FinalResult")
    y = df["FinalResult"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    # Evaluate model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy * 100:.2f}%")

    # Confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    print("Confusion Matrix:")
    print(cm)

    # Feature importances
    importances = model.feature_importances_
    feature_names = X.columns
    feature_importances = pd.DataFrame({"Feature": feature_names, "Importance": importances})
    feature_importances = feature_importances.sort_values(by="Importance", ascending=False)
    print("Feature Importances:")
    print(feature_importances)

    # Most important feature
    most_important = feature_importances.iloc[0]
    print(f"Most Important Feature: {most_important['Feature']} (Importance: {most_important['Importance']})")

    # Least important feature
    least_important = feature_importances.iloc[-1]
    print(f"Least Important Feature: {least_important['Feature']} (Importance: {least_important['Importance']})")

if __name__ == "__main__":
    main()