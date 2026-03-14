# Wine Dataset classifier
# Use Classification technigue.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

def main():
    # Load Data
    df = pd.read_csv("WinePredictor.csv")

    # Clean data
    df.dropna(inplace = True)

    X = df.drop(columns=["Class"])
    y = df["Class"]

    X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    print("Information of training and testing data:\n")
    print("X_train:", X_train.shape)
    print("Y_train:", Y_train.shape)
    print("X_test:", X_test.shape)
    print("Y_test:", Y_test.shape)

    scaler = StandardScaler()
    #Independent variable scaling:
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.fit_transform(X_test)

    model = KNeighborsClassifier(n_neighbors=9)
    model.fit(X_train_scaled, Y_train)

    Y_pred = model.predict(X_test_scaled)

    accuracy = accuracy_score(Y_test, Y_pred)

    print("Accuracy is :", accuracy * 100)

if __name__ == "__main__":
    main()