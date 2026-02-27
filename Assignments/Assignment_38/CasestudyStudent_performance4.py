
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


dataset = "student_performance_ml.csv"

df = pd.read_csv(dataset)


# value_counts(normalize=True)*100 to find the percnetage

percentage = (df["FinalResult"]==1).value_counts(normalize=True)*100   
print("Percentage of Pass / Fail :",percentage)

# The Dataset is unbalannced 
