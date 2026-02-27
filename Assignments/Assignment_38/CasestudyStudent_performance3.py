
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


dataset = "student_performance_ml.csv"

df = pd.read_csv(dataset)

Avg_study_hours = (df["StudyHours"]).mean()
print("Average of study hours:",Avg_study_hours)

###################################################################
Avg_Attendance = (df["Attendance"]).mean()
print("Average of Attendance :",Avg_Attendance)

###################################################################
max_PreviousScore = (df["PreviousScore"]).max()
print("Maximum of previous Score :",max_PreviousScore)

###################################################################
min_SleepHours = (df["SleepHours"]).min()
print("Minimum of SleepHours :",min_SleepHours)

