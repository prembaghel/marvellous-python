# Q6. Plot Histogram of StudyHours.
# Explain what distribution tells you.

import matplotlib.pyplot as plt
import seaborn
import helper

def main():
    df = helper.getStudentData()
    # continuous data
    seaborn.histplot(data = df["StudyHours"])

    plt.show()

if __name__ == "__main__":
    main()
