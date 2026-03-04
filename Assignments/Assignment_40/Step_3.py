import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import(accuracy_score,confusion_matrix)



dataset = "student_performance_ml.csv"

df = pd.read_csv(dataset)



feature_names = [
    "StudyHours",
    "Attendance"
]

X = df[feature_names]
Y = df["FinalResult"]



X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2 ,random_state=41)

print("X is :",X_train.shape)
print("X is :",X_test.shape)
print("Y is :",Y_train.shape)
print("Y is :",Y_test.shape)

model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=3,               
    random_state=42
)

model.fit(X_train,Y_train)

Y_pred = model.predict(X_test)

accuracy = accuracy_score(Y_test,Y_pred)

print("Accuracy of the model is :",accuracy*100)

# Conclusion :-

# THe full Feature model Accuracy  is :100%  And 
# "StudyHours","Attendance" this two features Accuracy also 100% ,
# Does not effect on the Accuracy of the model 
# This model is performing  well