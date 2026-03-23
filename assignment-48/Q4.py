# Q4. Write a python program to calculate the Euclidean distance between two points before and after
# applying feature scaling and explain the difference in result.

# Ans:
import numpy as np
from sklearn.preprocessing import StandardScaler
from scipy.spatial.distance import euclidean

# Two data points (e.g., [height in cm, weight in kg])
point1 = np.array([170, 65])
point2 = np.array([180, 80])

# Combine into dataset
data = np.array([point1, point2])

# 1. Euclidean distance BEFORE scaling
distance_before = euclidean(point1, point2)

# 2. Apply Standard Scaling
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

scaled_point1 = scaled_data[0]
scaled_point2 = scaled_data[1]

# 3. Euclidean distance AFTER scaling
distance_after = euclidean(scaled_point1, scaled_point2)

print("Distance before scaling:", distance_before)
print("Distance after scaling:", distance_after)


# Difference is:
# Before scaling: Distance is influenced by feature magnitude (units matter).
# After scaling: Distance reflects true relative differences, not unit size.
