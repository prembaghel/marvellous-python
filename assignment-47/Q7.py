# Q7. Suppose a dataset have following values: 6,7,8,9,10,11,12
# mean is 9 and Standard Deviation is 2.
# calculate the scaled values for following number
# 6, 9, 12

# Ans:
# Scaled value = (X- mean) / SD

X = [6, 9, 12]
X_scaled = []
for val in X:
    X_scaled.append((val - 9)/2)
print("X_scaled", X_scaled)