
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
    )

dataset = ("student_performance_ml.csv")

df = pd.read_csv(dataset)

print(df)

Feature_names = [

    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours",
    
]

X = df[Feature_names]

Y = df["FinalResult"]

X_train,X_test,Y_train,Y_test = train_test_split(
    X,
    Y,
    test_size=0.3,
    random_state=42
)

model = DecisionTreeClassifier()

model.fit(X_train,Y_train)








