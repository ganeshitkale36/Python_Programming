
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


dataset = "student_performance_ml.csv"

df = pd.read_csv(dataset)


# Draw a Histogram for StudyHours

plt.figure(figsize=(7,2))
sns.histplot(df["StudyHours"])
plt.title("Study vs Hours")
plt.show()

