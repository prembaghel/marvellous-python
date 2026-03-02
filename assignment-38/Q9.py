# Q9. create a plot showing relationship between AssignmentsCompleted and FinalResult. explain your observation.

import matplotlib.pyplot as plt
import seaborn
import helper

def main():
    df = helper.getStudentData()
    seaborn.countplot(x="AssignmentsCompleted", hue="FinalResult", data=df)
    plt.title("Relationship between AssignmentsCompleted and FinalResult")
    plt.show()
    # Observation:
    print("Observation:")
    print(f"From the plot, students who completed more assignments "
          f"have a higher chance of passing (FinalResult = Pass). ")
          

if __name__ == "__main__":
    main()
