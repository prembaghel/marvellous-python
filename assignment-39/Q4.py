# Q4. Generate confusion matrix using sklearn.
# display it using ConfusionMatrixDisplay.
# Explain clearly True Positives, True Negatives, False Positives, and False Negatives in the context of this problem.


from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv("student_performance_ml.csv")
    X = df.drop(columns="FinalResult")
    y = df["FinalResult"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    print("Model trained successfully.")

    y_pred = model.predict(X_test)
    print("Predicted results:", y_pred)
    print("Actual results:", y_test.values)

    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot()
    plt.show()

    tn, fp, fn, tp = cm.ravel()
    print(f"True Negatives: {tn}")
    print(f"False Positives: {fp}")
    print(f"False Negatives: {fn}")
    print(f"True Positives: {tp}")

if __name__ == "__main__":
    main()
