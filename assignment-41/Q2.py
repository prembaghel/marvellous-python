# Q2. The value of K plays an important role in the KNN algorithm.
# write a Python program that demonstrates how prediction changes when K changes.
# Dataset: same like Q1
# Tasks: predict class of new point when K=1, K=3, and K=5
# Expect output:
# Prediction results:
# K=1: Predicted class: RED
# K=3: Predicted class: RED
# K=5: Predicted class: BLUE
# explain why the predicted class changes with different K values.

import math

def euclidean_distance(point1, point2):
    return math.sqrt((point1['X'] - point2['X']) ** 2 + (point1['Y'] - point2['Y']) ** 2)

def knn_predict(new_point, dataset, k=3):
    # Compute distances
    distances = []
    for data in dataset:
        dist = euclidean_distance(new_point, data)
        distances.append((data, dist))
    # Sort distances
    distances.sort(key=lambda x: x[1])
    # Select K nearest neighbors
    neighbors = distances[:k]
    # Predict class based on majority vote
    class_votes = {}
    for neighbor in neighbors:
        label = neighbor[0]['label']
        class_votes[label] = class_votes.get(label, 0) + 1
        
    # Return the class with the most votes
    return max(class_votes, key=class_votes.get)

def main():
    # Dataset
    dataset = [
        {'X': 1, 'Y': 2, 'Point': 'A', 'label': 'RED'},
        {'X': 2, 'Y': 3, 'Point': 'B', 'label': 'RED'},
        {'X': 3, 'Y': 1, 'Point': 'C', 'label': 'BLUE'},
        {'X': 6, 'Y': 5, 'Point': 'D', 'label': 'BLUE'},
        {'X': 5, 'Y': 5, 'Point': 'E', 'label': 'BLUE'},
    ]

    # New data point
    new_point = {'X': 2, 'Y': 2}

    # Predict the class for different values of K
    for k in [1, 3, 5]:
        predicted_class = knn_predict(new_point, dataset, k)
        print(f"K={k}: Predicted class: {predicted_class}")

if __name__ == "__main__":
    main()