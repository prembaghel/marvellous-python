# case study for Diabetic 
# - load data-> do EDA -> find outlier using hist/ boxplot/ pairplot
# - train model with Logistic regression, KNN, Decision Tree
# - show confusion matrix using matplotlib or seaborn
# - print accuracy_score, precision, recall,CM, f1 score

# Ans:

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.discriminant_analysis import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import ConfusionMatrixDisplay, accuracy_score, classification_report, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier

def DisplayInfo(title):
    print("\n" + "=" * 100)
    print(title)
    print("=" * 100)

def main():
    ###########################################################################
    # Step 1: Load the dataset
    ###########################################################################

    DisplayInfo("Step 1: Load the dataset")
    DatasetPath = "diabetes.csv"
    df = pd.read_csv(DatasetPath)
    print("Initial entries from dataset:")
    print(df.head())

    ###########################################################################
    # Step 2: Clean the dataset
    ###########################################################################

    DisplayInfo("Step 2: Clean the dataset")
    print("Missing values:\n", df.isnull().sum())
    
    # drop rows with NaN value
    df.dropna()

    # Check for zero values in numeric columns
    print("\nZero values per column:")
    print((df == 0).sum())
    
    # Check which columns have zeros (often invalid in medical data)
    zero_columns = (df == 0).sum()
    print("\nColumns with zeros:", zero_columns[zero_columns > 0])
    
    # Replace zeros with NaN in specific columns (medical data often uses 0 as missing)
    # For diabetes dataset: Glucose, BloodPressure, SkinThickness, Insulin, BMI should not be 0
    cols_to_fill = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
    for col in cols_to_fill:
        if col in df.columns:
            df[col] = df[col].replace(0, np.nan)
    
    # Fill NaN values with median (better than mean for skewed data)
    df = df.fillna(df.median())
    
    # print("\nAfter handling zeros and NaN:")
    # print("Missing values:\n", df.isnull().sum())
    # print("Zero values:\n", (df == 0).sum())

    print("Basic Statistic:\n", df.describe())

    ###########################################################################
    # Step 3: Data Visualization 
    ###########################################################################

    # Visualization as histplot
    sns.histplot(df["Outcome"])
    plt.show()

    ###########################################################################
    # Step 4: Apply StandardScaler to normalize features
    ###########################################################################

    DisplayInfo("Step 4: Apply StandardScaler to normalize features")
    
    # Separate features (X) and target (y)
    X = df.drop('Outcome', axis=1)  # All columns except Outcome
    Y = df['Outcome']               # Target column
    
    # Initialize and fit StandardScaler
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Convert back to DataFrame for easier handling
    X_scaled = pd.DataFrame(X_scaled, columns=X.columns)
    
    # print("Original X (first 5 rows):\n", X.head())
    # print("\nScaled X (first 5 rows):\n", X_scaled.head())
    print("\nScaled X statistics:\n", X_scaled.describe())

    ###########################################################################
    # Step 5: create training and testing data
    ###########################################################################

    DisplayInfo("Step 5: Create training and testing data")

    X_train, X_test, Y_train, Y_test = train_test_split(X_scaled, Y, test_size=0.2, random_state=42)

    print("Shape of X_train:", X_train.shape)
    print("Shape of Y_train:", Y_train.shape)
    print("Shape of X_test:", X_test.shape)
    print("Shape of Y_test:", Y_test.shape)

    ###########################################################################
    # Step 6: Create and train LogisticRegression model
    ###########################################################################

    DisplayInfo("Step 6: Create and train LogisticRegression model")
    model_lr = LogisticRegression(max_iter=1000)
    model_lr.fit(X_train, Y_train)
    print("LogisticRegression model created and trained successfully.")

    ###########################################################################
    # Step 7: Create and train KNN model
    ###########################################################################
    
    DisplayInfo("Step 7: Create and train KNN model")
    model_knn = KNeighborsClassifier(n_neighbors=11)
    model_knn.fit(X_train, Y_train)
    print("KNN model created and trained successfully.")

    ###########################################################################
    # Step 8: Test both the model and get prediction
    ###########################################################################

    DisplayInfo("Step 8: Test both the model and get prediction")
    Y_pred_lr= model_lr.predict(X_test)
    Y_pred_knn= model_knn.predict(X_test)
    print("Both the model tested successfuly.")

    ###########################################################################
    # Step 9: Calculate and print accuracy score for both models
    ###########################################################################

    DisplayInfo("Step 9: Calculate and print accuracy score for both models")

    accuracy_lr = accuracy_score(Y_pred_lr, Y_test)
    print("Accuracy of LogisticRegression model:", accuracy_lr * 100)

    accuracy_knn = accuracy_score(Y_pred_knn, Y_test)
    print("Accuracy of KNN model:", accuracy_knn * 100)

    ###########################################################################
    # Step 10: Display confusion matrix and classification report
    ###########################################################################

    DisplayInfo("Step 10: Display confusion matrix and classification report")

    cm_lr  = confusion_matrix(Y_pred_lr, Y_test)
    cm_knn  = confusion_matrix(Y_pred_knn, Y_test)

    print("confusion matrix of LogisticRegression:\n",cm_lr)
    print("confusion matrix of KNN:\n",cm_knn)

    print("Classification report of LogisticRegression: \n",classification_report(Y_test, Y_pred_lr))
    print("Classification report of LogisticRegression: \n",classification_report(Y_test, Y_pred_knn))

    # Display CM graph
    data = ConfusionMatrixDisplay(confusion_matrix=cm_lr, display_labels=model_lr.classes_)
    data.plot()
    plt.title("Confusion matrix of Dibetic dataset")
    plt.show()

    ###########################################################################
    # Step 11: Add predicted values of test data in .csv
    ###########################################################################
   
    DisplayInfo("Step 11: Add predicted values of test data in .csv")
    # to do: insted of scaled values put X_test values before scaling in csv
    data = pd.DataFrame(X_test, columns=X_test.columns)
    data["target"] = Y_pred_lr
    data.to_csv("Diabetes_LR_model_result.csv", index = False)

    print("Predicted values using LogisticRegression model and stored in Diabetes_LR_model_result.csv file.")

if __name__ == "__main__":
    main()