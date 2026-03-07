# Q7. Train student model using: 
# random_state= 0, 10, 42
# Compare testing accuracy, does the result change?

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier 

def train_and_evaluate(random_state):
    # Load dataset
    df = pd.read_csv("student_performance_ml.csv")
    X = df.drop(columns=["FinalResult"])
    y = df["FinalResult"]

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=random_state)

    # Train model
    model = RandomForestClassifier(random_state=random_state)
    model.fit(X_train, y_train)

    # Evaluate model
    accuracy = model.score(X_test, y_test)
    print(f"Accuracy with random_state={random_state}: {accuracy * 100:.2f}%")

def main():
    for state in [0, 10, 42]:
        train_and_evaluate(state)
    print("The result changes with different random states due to the randomness in data splitting and model training. Different random states can lead to different subsets of data for training and testing, which can affect the model's performance and thus the accuracy.")

if __name__ == "__main__":
    main()
