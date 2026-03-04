
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import(accuracy_score)
data = {
    "StudyHours" : [2,3,5,6,7],
    "Attendance" : [0,3,2,5,6],
    "PreviousScore" :[50,60,65,78,80],
    "AssignmentsCompleted" :[1,3,5,7,8],
    "SleepHours":[1,3,2,4,6],
    "FinalResult" :[0,1,0,1,1]
}
    
df = pd.DataFrame(data)
print(df)

feature_names = [
    "StudyHours",
    "Attendance",
    "PreviousScore" ,
    "AssignmentsCompleted",
    "SleepHours"
]

X = df[feature_names]
Y = df["FinalResult"]

print(X.shape)
print(Y.shape)

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3,random_state=42)

print("X_train:",X_train.shape)
print("X_test:",X_test.shape)
print("Y_train:",Y_train.shape)
print("Y_test:",Y_test.shape)

model = DecisionTreeClassifier(criterion="gini",max_depth=2,random_state=42)
model.fit(X_train,Y_train)
print("Model Training Successfully Completed:")

Y_pred = model.predict(X_test)
print("Predictive Answer:",Y_pred)

print("Expected Answer:")
print(Y_test !=Y_pred)

accuracy = accuracy_score(Y_test,Y_pred)
print("The Accuracy is:",accuracy*100)
 
# The accuracy of the dataset is 50%