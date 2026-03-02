# Q7. Create a scatter plot of : StudyHours vs PreviousScore.
# Use different colors for pass and fail students.

import matplotlib.pyplot as plt
import seaborn
import helper

def main():
    df = helper.getStudentData()
    seaborn.scatterplot(x="StudyHours", y="PreviousScore", hue="FinalResult", data=df)
    plt.title("StudyHours vs PreviousScore")
    plt.show()

if __name__ == "__main__":
    main()
