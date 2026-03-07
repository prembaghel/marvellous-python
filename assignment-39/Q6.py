# Q6. Train three Decision tree models with:
# max_depth = 1, max_depth = 3, max_depth = None
# compare the accuracy_score for all three models and comment on the results.

from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from sklearn.model_selection import train_test_split    
from sklearn.metrics import accuracy_score  

def main():
    df = pd.read_csv("student_performance_ml.csv")
    X = df.drop(columns="FinalResult")
    y = df["FinalResult"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    models = {
        "max_depth=1": DecisionTreeClassifier(max_depth=1),
        "max_depth=3": DecisionTreeClassifier(max_depth=3),
        "max_depth=5": DecisionTreeClassifier(max_depth=5),
        "max_depth=None": DecisionTreeClassifier(max_depth=None)
    }

    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Accuracy for {name}: {accuracy * 100:.2f}%")

    print("\nComparing the results: All are same when I tested.")
    
if __name__ == "__main__":
    main()
