# Q10. Plot SleepHours vs FinalResult.
# does sleeping more gurantees success? explain your observation.

import matplotlib.pyplot as plt
import seaborn
import helper

def main():
    df = helper.getStudentData()
    seaborn.histplot(x="SleepHours", hue="FinalResult", data=df, multiple="stack")
    plt.title("SleepHours vs FinalResult")
    plt.show()
    # Observation:
    print("Observation:")
    print(f"This suggests that getting enough sleep may have a positive impact on a student's performance and their likelihood of passing the course.")

if __name__ == "__main__":
    main()
