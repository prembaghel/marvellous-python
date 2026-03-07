# Q8. Write a single structured python program that perform:
# DataLoading, Data analysis, visualization, train_test_split, model training, prediction, accuracy_score, confusion matrix generation, Final conclusion.

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay  

def main():
    # Data Loading
    df = pd.read_csv("student_performance_ml.csv")
    
    # Data Analysis
    print("Data Analysis:")
    print(df.describe())
    
    # Visualization
    df['FinalResult'].value_counts().plot(kind='bar', color=['blue', 'orange'])
    plt.title('Distribution of Final Results')
    plt.xlabel('Final Result')
    plt.ylabel('Count')
    plt.legend()
    plt.show()
    
    # Train-test split
    X = df.drop(columns="FinalResult")
    y = df["FinalResult"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Model training
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    
    # Prediction
    y_pred = model.predict(X_test)
    
    # Accuracy score
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy * 100:.2f}%")
    
    # Confusion matrix generation
    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot()
    plt.show()
    
    # Final conclusion
    tn, fp, fn, tp = cm.ravel()
    print(f"True Negatives: {tn}")
    print(f"False Positives: {fp}")
    print(f"False Negatives: {fn}")
    print(f"True Positives: {tp}")
    print("\nConclusion: The model has an accuracy of {:.2f}%. The confusion matrix shows the distribution of true positives, true negatives, false positives, and false negatives. Based on these metrics, we can evaluate the performance of the model and identify areas for improvement.".format(accuracy * 100))       
    
if __name__ == "__main__":
    main()