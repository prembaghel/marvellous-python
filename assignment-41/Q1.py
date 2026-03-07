# Q1. Write a python program that classifies a new data point using K-Nearest Neighbors (KNN) algorithm.
# The algorithm should be implemented manually without using any machine learning libraries.
# The program should
    # Calculate Euclidean distance 
    # sort distances
    # Select K nearest neighbors
    # Predict the class based on majority vote
# Dataset:
# [
    # {X:1, Y:2, Point: 'A', label: 'RED'}, 
    # {X:2, Y:3, Point: 'B', label: 'RED'},
    # {X:3, Y:1, Point: 'C', label: 'BLUE'},
    # {X:6, Y:5, Point: 'D', label: 'BLUE'},
# ]

# Tasks:
# 1. accept a new data point (X, Y) from the user
# 2. compute Euclidean distance from the new data point to all existing points in the dataset
# 3. sort the distances 
# 4. select the K nearest neighbors (K=3)
# 5. predict the class of label

# Input Format:
# Enter x coordinate: 2
# Enter y coordinate: 2

# Output :
# Nearest neighbors:
# A - Distace = 1.0
# B - Distace = 1.0
# C - Distace = 1.41
# Predicted class: RED

import math

def euclidean_distance(point1, point2):
    return math.sqrt((point1['X'] - point2['X']) ** 2 + (point1['Y'] - point2['Y']) ** 2)

def knn_predict(new_point, dataset, k=3):
    # Compute distances
    distances = []
    for data in dataset:
        dist = euclidean_distance(new_point, data)
        distances.append((data, dist))
    # Print distances
    for data, dist in distances:
        print(f"Distance from {data['Point']} to new point: {dist:.2f}")
        
    # Sort distances
    distances.sort(key=lambda x: x[1])
    
    # Select K nearest neighbors
    neighbors = distances[:k]
    
    # Predict class based on majority vote
    class_votes = {}
    for neighbor in neighbors:
        label = neighbor[0]['label']
        class_votes[label] = class_votes.get(label, 0) + 1
        print(f"{neighbor[0]['Point']} - Distance = {neighbor[1]:.2f}")
    
    # Return the class with the most votes
    return max(class_votes, key=class_votes.get)

def main():
    # Dataset
    dataset = [
        {'X': 1, 'Y': 2, 'Point': 'A', 'label': 'RED'}, 
        {'X': 2, 'Y': 3, 'Point': 'B', 'label': 'RED'},
        {'X': 3, 'Y': 1, 'Point': 'C', 'label': 'BLUE'},
        {'X': 6, 'Y': 5, 'Point': 'D', 'label': 'BLUE'},
    ]

    # Accept new data point from user
    x = float(input("Enter x coordinate: "))
    y = float(input("Enter y coordinate: "))
    new_point = {'X': x, 'Y': y}    

    # Predict the class of the new data point
    predicted_class = knn_predict(new_point, dataset)
    print(f"Predicted class: {predicted_class}")    

if __name__ == "__main__":
    main()