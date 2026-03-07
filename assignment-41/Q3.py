# Q3. Use KNN to predict the result if student is passed or fails based on study hours and attendance.
# Dataset:
# [[study_hours, attendance, result], ...]
# dataset = [
#     [2, 60, 'FAIL'],
#     [5, 80, 'PASS'],
#     [6, 85, 'PASS'],
#     [1, 50, 'FAIL'],
# ]     
# 1. Accept study hours and attendance percentage from user.
# 2. Use KNN to predict whether the student will PASS or FAIL for K=3.

# input:
# Enter study hours: 4
# Enter attendance percentage: 70
# output:
# Predicted result: PASS

import math

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def knn_predict(new_point, dataset, k=3):
    # Compute distances
    distances = []
    for data in dataset:
        dist = euclidean_distance(new_point, data[:2])
        distances.append((data, dist))
    # Sort distances
    distances.sort(key=lambda x: x[1])
    # Select K nearest neighbors
    neighbors = distances[:k]
    # Predict class based on majority vote
    class_votes = {}
    for neighbor in neighbors:
        label = neighbor[0][2]
        class_votes[label] = class_votes.get(label, 0) + 1

    # Return the class with the most votes
    return max(class_votes, key=class_votes.get)

def main():
    # Dataset
    dataset = [
        [2, 60, 'FAIL'],
        [5, 80, 'PASS'],
        [6, 85, 'PASS'],
        [1, 50, 'FAIL'],
    ]

    # Input
    study_hours = float(input("Enter study hours: "))
    attendance = float(input("Enter attendance percentage: "))
    new_point = [study_hours, attendance]

    # Predict the result
    predicted_result = knn_predict(new_point, dataset, k=3)
    print(f"Predicted result: {predicted_result}")

if __name__ == "__main__":
    main()