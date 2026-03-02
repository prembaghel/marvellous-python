# Q8. Draw boxplot for attendance.
# identifier if any outlier are there.

import matplotlib.pyplot as plt
import seaborn
import helper

def main():
    df = helper.getStudentData()
    seaborn.boxplot( x= df["Attendance"])
    plt.title("Boxplot of Attendance")
    plt.show()

if __name__ == "__main__":
    main()
