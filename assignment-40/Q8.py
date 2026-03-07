# Q8. Decision Tree visualization
# use : from sklearn.tree import plot_tree
# Visualize the trained decision tree,
    # which features appear at the root node?
    # why do you think that feature was selected first?

import pandas as pd
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree

def main():
    # Load dataset
    df = pd.read_csv("student_performance_ml.csv")
    X = df.drop(columns=["FinalResult"])
    y = df["FinalResult"]

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Train model
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Visualize decision tree
    plt.figure(figsize=(12,8))
    plot_tree(model, feature_names=X.columns, class_names=[str(c) for c in model.classes_], filled=True)
    plt.show()

if __name__ == "__main__":
    main()
