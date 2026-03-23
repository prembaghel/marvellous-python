# Q8. Write a python program that calculate TP, TN, FP, FN for below data:
# Q9: Generate classification report for following data 

# Actual: [1, 1, 1, 1, 0, 0, 0, 0]
# Predicted: [1, 1, 0, 1, 0, 1, 0, 0]

# Ans:
from sklearn.metrics import classification_report, confusion_matrix

Actual = [1, 1, 1, 1, 0, 0, 0, 0]
Predicted = [1, 1, 0, 1, 0, 1, 0, 0]

print("confusion matrix is:\n",confusion_matrix(Actual, Predicted))

print("Classification Report :\n",classification_report(Actual, Predicted))