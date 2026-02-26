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
Border = "-"*60
##############################################################################
# Step1 : Load the Datset
##############################################################################
print(Border)
print("Step 1 : Load The Data")
print(Border)

dataset = ("student_performance_ml.csv")
print("Load the Data Successfully:")

df = pd.read_csv(dataset)

print("First entries of Data:")
print(df.head())


##############################################################################
# Step 2 : Analysis The Data 
##############################################################################
print(Border)
print("Step 2 : Analysis The Data")
print(Border)

print("Missing values (per column):")
print(df.isnull().sum)

print("Shape of the dataset")
print(df.shape)

print("Stastical report of the dataset:")
print(df.describe())

print(Border)

##############################################################################
# Step 3 : Vusualize the data 
##############################################################################
print(Border)
print("Step 2 : Analysis The Data")
print(Border)

plt.figure(figsize=(7,2))
for sp in df["FinalResult"].unique():
    temp = df[df["FinalResult"]==sp]
    plt.scatter(temp["StudyHours"],temp["Attendance"],label = sp)

plt.title("StudyHours Vs Attendance")
plt.xlabel("StudyHours")
plt.ylabel("Attendance")

plt.legend()
plt.grid(True)
plt.show()

##############################################################################
# Step 4 :  Decide the Independent Variable / depndent Variable
##############################################################################
print(Border)
print("Step 4 : Decide the Independent Variable / depndent Variable")
print(Border)

Feature_names = [

    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours",
    
]

X = df[Feature_names]

Y = df["FinalResult"]

print(Border)

##############################################################################
# Step 5 : Split the dataset in training and testing part
##############################################################################
print(Border)
print("Step 5 : Split the dataset in training and testing part")
print(Border)

X_train,X_test,Y_train,Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)

print("X_train is:",X_train.shape)      # (24,5)
print("X_test is:",X_test.shape)        # (6,5)

print("Y_train is:",Y_train.shape)      # (24,)
print("Y_test is:",Y_test.shape)        # (6,)

##############################################################################
# Step 6 : Build the model
##############################################################################
print(Border)
print("Step 6 : Build the model")
print(Border)
model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=3,
    random_state=42
)

##############################################################################
# Step 7 : Train the model
##############################################################################
print(Border)
print("Step 7 : Train the model")
print(Border)

model.fit(X_train,Y_train)
print("Model train successfully")

##############################################################################
# Step 8 : Test and Evaluate the model
##############################################################################
print(Border)
print("Step 8 : Test and Evaluate model")
print(Border)

print("Test / Evaluate the model")
Y_pred = model.predict(X_test)

print("Predictive Answer:")
print(Y_pred)

print("Excepeted  Answer:")
print(Y_test)

##############################################################################
# Step 9 :    Accuracy Calculation
##############################################################################
print(Border)
print("Step 9 : Accuracy Calculation")
print(Border)

accuracy = accuracy_score(Y_test,Y_pred)
print("Accuracy of the model is :",accuracy*100)


##############################################################################
# Step 10 :  Diplay the Confusion Matrix
##############################################################################
print(Border)
print("Step 10 : Diplay the Confusion Matrix")
print(Border)

confusion = confusion_matrix(Y_test,Y_pred)
print("Confusion Matrix is :",confusion)


data = ConfusionMatrixDisplay(confusion_matrix=confusion,display_labels=model.classes_)

data.plot()
plt.title("Confusion Matrix")
plt.show()








