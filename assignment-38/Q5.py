
# Q5. Analyze higher study hours increase the chance of passing
# Higher attendance inproves FinalResult.


import helper

df = helper.getStudentData()

print("-" * 50)
print("Average study hours for passed students:\n", df[df["FinalResult"] == 1]["StudyHours"].mean())
print("Average study hours for failed students:\n", df[df["FinalResult"] == 0]["StudyHours"].mean())
print("Student who studied more than equal to 4 hours had higher chance of passing.")
print("-" * 50)
print("Average attendance for passed students:\n", df[df["FinalResult"] == 1]["Attendance"].mean())
print("Average attendance for failed students:\n", df[df["FinalResult"] == 0]["Attendance"].mean())
print("Student who had higher attendance more than 75% had higher chance of passing.")
print("-" * 50)