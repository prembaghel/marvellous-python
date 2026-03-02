
# Q4 - Analyse using value_counts() and calculate pass and failed percentage
# is dataset balanced justify answer.


import helper

df = helper.getStudentData()

def PrintPercentage():
    print(df["FinalResult"].value_counts())

    pass_percent = (df["FinalResult"] == 1).mean() * 100
    fail_percent = (df["FinalResult"] == 0).mean() * 100

    print("Pass %:", pass_percent)
    print("Fail %:", fail_percent)

PrintPercentage()

print("As data set is distributed in 60-40 percent it looks like balanced.")

