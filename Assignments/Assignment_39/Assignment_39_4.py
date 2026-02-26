import matplotlib.pyplot as plt
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
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
    test_size=0.2,
    random_state=42
)

print("X_train is:",X_train)
print("X_test is:",X_test)
print("Y_train is:",Y_train)
print("Y_test is:",Y_test)

model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=1,
    random_state=42
)


model.fit(X_train,Y_train)

Y_pred = model.predict(X_test)

print("Predictive Answer:")
print(Y_pred)

print("Excepeted  Answer:")
print(Y_test,Y_pred)


accuracy = accuracy_score(Y_test,Y_pred)
print("Accuracy of the model is :",accuracy*100)

confusion = confusion_matrix(Y_test,Y_pred)

print("Confusion Matrix is :")
print(confusion)

data = ConfusionMatrixDisplay(confusion_matrix=confusion,display_labels=model.classes_)

data.plot()
plt.title("Confusion Matrix")
plt.show()








