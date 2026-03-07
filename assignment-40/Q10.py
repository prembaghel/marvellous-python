# Q10. Train model with :
# max_depth = None
# calculate Training and Testing accuracy.
# if the training accuracy is 100% but testing accuracy is low, what does it indicate about the model? 
# explain why this happens

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier 

def main():
    # Load dataset
    df = pd.read_csv("student_performance_ml.csv")
    X = df.drop(columns=["FinalResult"])
    y = df["FinalResult"]

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Train model with max_depth=None
    model = DecisionTreeClassifier(max_depth=None, random_state=42)
    model.fit(X_train, y_train)

    # Calculate training and testing accuracy
    training_accuracy = model.score(X_train, y_train)
    testing_accuracy = model.score(X_test, y_test)

    print(f"Training Accuracy: {training_accuracy * 100:.2f}%")
    print(f"Testing Accuracy: {testing_accuracy * 100:.2f}%")

    if training_accuracy == 1.0 and testing_accuracy < 1.0:
        print("This indicates that the model is overfitting. Overfitting occurs when a model learns the training data too well, including its noise and outliers, which leads to poor generalization to new, unseen data (testing data). The model performs perfectly on the training set but fails to perform well on the testing set because it has essentially memorized the training data rather than learning the underlying patterns.")

if __name__ == "__main__":
    main()
