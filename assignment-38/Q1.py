# Q1. write a python program to load the file student_performance_ml.csv using pandas.
# Display the first 5 rows of the dataset.
# last 5 rows of the dataset.
# number of rows and columns in the dataset.
# list of column names in the dataset.
# data types of each column in the dataset.

import helper

df = helper.getStudentData()
# print first 5 line of dataset
print("First 5 line of Dataset:\n",df.head())

# print last 5 line of dataset
print("Last 5 line of Dataset:\n",df.tail())

# print Number of rows and column of Dataset
print("Number of rows and column of Dataset:\n",df.shape)

# print list of column names in dataset
print("List of column names in Dataset:\n",list(df.columns))

# print data type of each column in dataset
print("Datatype of each column in Dataset:\n",df.dtypes)

