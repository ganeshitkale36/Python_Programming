import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import(accuracy_score,confusion_matrix)



dataset = "student_performance_ml.csv"

df = pd.read_csv(dataset)



feature_names = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
]

X = df[feature_names]
Y = df["FinalResult"]



X = df.drop(["SleepHours"],axis=1)
print(X)


X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2 ,random_state=41)

print("X is :",X_train.shape)
print("X is :",X_test.shape)
print("Y is :",Y_train.shape)
print("Y is :",Y_test.shape)

model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=2,
    random_state=42
)

model.fit(X_train,Y_train)

Y_pred = model.predict(X_test)

accuracy = accuracy_score(Y_test,Y_pred)

print("Accuracy of the model is :",accuracy*100)

# Conclusion :-

# We remove the "SleepHours" Column, Does not any effect on the Accuracy of the model is same as the Previous Accuracy But 
# We change the "test_size" the Accuracy of the model will be change

