# Q5. Calculate - Training accuracy and Testing accuracy.
# shuffle the data and split into train and test set. 
# compare both and comment wether model is overfitting or underfitting.

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score  

def main():
    df = pd.read_csv("student_performance_ml.csv")
    X = df.drop(columns="FinalResult")
    y = df["FinalResult"]
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)  # Shuffle the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)

    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    print("Model trained successfully.")

    y_pred_train = model.predict(X_train)
    y_pred_test = model.predict(X_test)

    train_accuracy = accuracy_score(y_train, y_pred_train)
    test_accuracy = accuracy_score(y_test, y_pred_test)

    print(f"Training Accuracy: {train_accuracy * 100:.2f}%")
    print(f"Testing Accuracy: {test_accuracy * 100:.2f}%")

    if train_accuracy > test_accuracy:
        print("The model is overfitting.")
    elif train_accuracy < test_accuracy:
        print("The model is underfitting.")
    else:
        print("The model is neither overfitting nor underfitting.")

if __name__ == "__main__":
    main()
