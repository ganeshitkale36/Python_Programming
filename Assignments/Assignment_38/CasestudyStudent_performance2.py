
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


dataset = "student_performance_ml.csv"

df = pd.read_csv(dataset)


print("Total number of students in dataset :",df.shape[0])

passed_students = (df["FinalResult"]==1).sum()
print("Total count of pass student:",passed_students)

failed_students = (df["FinalResult"] ==1).sum()
print("Total count of pass student:",failed_students)


