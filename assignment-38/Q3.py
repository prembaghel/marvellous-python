
import helper

df = helper.getStudentData()


# Display average study hours
average_study_hours = df["StudyHours"].mean()
print("Average Study Hours:\n", average_study_hours)


# Display average Attendance
average_attendance = df["Attendance"].mean()
print("Average Attendance:\n", average_attendance)


# Display Maximum previous score
maximum_previous_score = df["PreviousScore"].max()
print("Maximum previous score:\n", maximum_previous_score)


# Display Minimum sleep hours
minimum_sleep_hours = df["SleepHours"].min()
print("Minimum sleep hours:\n", minimum_sleep_hours)