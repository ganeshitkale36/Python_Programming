
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
##############################################
# Step 1: Load  the dataset
###############################################

dataset = "student_performance_ml.csv"

df = pd.read_csv(dataset)


print("First five entries of dataset")  
print(df.head())

print("Last  five entries of dataset")
print(df.tail())

print(df.shape)

Feature_names = [

    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours",
    "FinalResult"
]

X = df[Feature_names]

Y = df["FinalResult"]

print("List of Column :",Feature_names)

print(df.info(Feature_names))




