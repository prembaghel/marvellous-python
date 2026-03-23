# Q3. Write a python program using StandardScaler to perform feature scaling on following dataset:
# [[25, 20000], [30, 40000], [35, 80000]]
# print scaled dataset


from sklearn.preprocessing import StandardScaler

data = [[25, 20000], [30, 40000], [35, 80000]]

scaler = StandardScaler()

scaled_data = scaler.fit_transform(data)

print("scaled_data:", scaled_data)