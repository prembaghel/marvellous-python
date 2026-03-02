# Q2. write a program to:
#   Display total number of student in dataset
#   count how many students passed (Final result = 1)
#   count how many students failed (Final result = 0)


import helper

df = helper.getStudentData()

# display total number of student in dataset
print("Total number of students:\n", df.shape[0])

# display how many student passed
passed_count = (df["FinalResult"] == 1).sum()
print("Count of number of passed students:\n",passed_count)


# display how many student failed
failed_count = (df["FinalResult"] == 0).sum()
print("Count of number of failed students:\n",failed_count)
