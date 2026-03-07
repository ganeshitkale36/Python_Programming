import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import(
    confusion_matrix,
    accuracy_score,
    ConfusionMatrixDisplay,
    classification_report
)
##############################################
# Step 1: Load  the dataset
###############################################

print("Step 1 : Load  the dataset")
dataset = "diabeties.csv"

df = pd.read_csv(dataset)
print("Datset are correctly loaded")
print(df)

print("First entreis of dataset:")
print(df.head)

Border = "-"*50
print(Border)

##############################################
# Step 2: Clean  the dataset
###############################################
print(Border)
print("Step 2 : Clean the dataset")
print(Border)

print("The shape of the dataset")
print(df.shape)                                        # (768,9)

print("Missing values (per column)")
print(df.isnull().sum())

print("Statical report of the dataset:")
print(df.describe)

#############################################################
# Step 3: Decide the independnet and dependent variable 
#############################################################
print(Border)
print("Step 3 : Decide the independnet and dependent variable")
print(Border)


# X : Independent Variable / Faeatures
# Y : Dependent Variable / Labels

feature_name = [
    "Pregnancies",
    "Glucose",
    "BloodPressure",
    "SkinThickness",
    "Insulin",
    "BMI",
    "DiabetesPedigreeFunction",
    "Age"
]

X = df[feature_name]
Y = df["Outcome"]

print("Shape of X:",X.shape)   # (768,8)
print("Shape of Y:",Y.shape)   # (768,)

#############################################################
# Step 4: Visualize the data
#############################################################
print(Border)
print("Step 4 : Visualize the data ")
print(Border)

plt.figure(figsize=(7,2))
for sp in df["Outcome"].unique():
    temp = df[df["Outcome"]==sp]
    plt.scatter(temp["BloodPressure"],temp["Glucose"],label = sp)

plt.title("Diabeties: BloodPressure vs Glucose")
plt.xlabel("BloodPressure")
plt.ylabel("Glucose")

plt.legend()
plt.grid(True)
plt.show()

#############################################################
# Step 5: Split the dataset for trainig and testing
#############################################################
print(Border)
print("Step 5 : Split the dataset for trainig and testing ")
print(Border)

X_train,X_test,Y_train,Y_test = train_test_split(
    X,
    Y,
    test_size=0.5,
    random_state=42
)
print("Data spliting is done:")

print("Shape of X:",X.shape)   # (768,8)
print("Shape of Y:",Y.shape)   # (768,)

print("X_trian :",X_train.shape)
print("X_test :",X_test.shape)

print("Y_train :",Y_train.shape)
print("Y_test :",Y_test.shape)

#############################################################
# Step 6: Build the model
#############################################################
print(Border)
print("Step 6 : : Build the model ")
print(Border)

print("We use the Decidion classifier model")

model  = DecisionTreeClassifier(
    criterion="gini",
    max_depth=5,
    random_state=42
)

#############################################################
# Step 7: Train  the  model
#############################################################
print(Border)
print("Step 7 : Train the model ")
print(Border)

model.fit(X_train,Y_train)
print("Model training completed")

#############################################################
# Step 8: Test/ Evaluate  the  model
#############################################################
print(Border)
print("Step 7 : Test the model ")
print(Border)

Y_pred = model.predict(X_test)

print("Evaluate the model:")
print(Y_pred.shape)

print("Predictive Answer")
print(Y_pred)

print("Excepted ANswer:")
print(Y_test)
print("Model testing  completed")

#############################################################
# Step 9: Evaluate the model performance
#############################################################
print(Border)
print("Step 9 : Evaluate the model Performance ")
print(Border)

accuracy = accuracy_score(Y_test,Y_pred)

print("Accuracy of the model",accuracy*100)


cm = confusion_matrix(Y_test,Y_pred)

print("Confusion matrix is")
print(cm)

print("Classfication Report:")
print(classification_report(Y_test,Y_pred))


#############################################################
# Step 10 : Plot confusion Matrix
#############################################################
print(Border)
print("Step 10 : Plot Confusion Matrix ")
print(Border)


data = ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=model.classes_)

data.plot()
plt.title("Confusion Matrix of Iris Dataset")
plt.show()

