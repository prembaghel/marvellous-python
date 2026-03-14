# Dataset of Weather condition
# Decide whether to play or not
# Design machine learning app which uses Classification technique.
# 1. Load Data
# 2. Clean prepare and maniplulate data (feature weather and temprature replace string with numeric value.)
# 3. Use K nearest neighbour algorithm
# 4. Use K =2 in this KNN algorithm check result and display on screen
# 5. calculate accuracy for different values of K

import pandas as pd
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def main():
    # step 1: Load data
    df = pd.read_csv("PlayPredictor.csv")

    # step 2: clean data
    if "Unnamed: 0" in df.columns:
        df.drop(columns=["Unnamed: 0"], inplace=True)

    # display data
    print("Data:\n",df.head())

    featureData = pd.DataFrame(df[['Whether', 'Temperature']])

    encoders = {}
    for column in featureData:
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column])
        encoders[column] = le
    
    print("encoded data:\n", df.head())

    # Transformed data in required format, Select the features and target
    X = df[['Whether', 'Temperature']]
    y = df['Play']

    print("X shape", X.shape)
    print("Y shape", y.shape)

    # step 3: Train data
    X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print("X_train:", X_train.shape)
    print("X_test:", X_test.shape)
    print("Y_train:", Y_train.shape)
    print("Y_test:", Y_test.shape)

    model = KNeighborsClassifier(n_neighbors=5)

    model.fit(X_train, Y_train)

    # step 4: Test data
    Y_pred = model.predict(X_test)

    # step 4: show accuracy
    accuracy = accuracy_score(Y_test, Y_pred)

    print("Accuracy is :", accuracy * 100)

if __name__ == "__main__":
    main()