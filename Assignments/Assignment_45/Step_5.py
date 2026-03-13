import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

def MarvellousWineeCaseStudy(datapath):
    Border = "-"*60

    #---------------------------------------------------------------------
    # Step 1 : Load the Dataset
    #---------------------------------------------------------------------
    print(Border)
    print("Step 1 : Load the Dataset")
    print(Border)

    df = pd.read_csv(datapath)
    print(df.shape)

    print("Few Entries of dataset:")
    print(df.head())

    
    #---------------------------------------------------------------------
    # Step 2 : Missing values from the dataset
    #---------------------------------------------------------------------
    print(Border)
    print("Step 2 : Missing values from the dataset")
    print(Border)

    print("Missing values per(column)")
    print(df.isnull().sum())



    #---------------------------------------------------------------------
    # Step 3 : Statistical report
    #---------------------------------------------------------------------
    print(Border)
    print("Step 3 : Statistical report")
    print(Border)

    print("Statistical report:")
    print(df.describe())


    #---------------------------------------------------------------------
    # Step 4 : Coorelation of dataset 
    #---------------------------------------------------------------------
    print(Border)
    print("Step 4 : Coorelation of dataset ")
    print(Border)

    print(df.corr())

     #---------------------------------------------------------------------
    # Step 5 : Split the dataset Independent variable and Dependent variable
    #---------------------------------------------------------------------
    print(Border)
    print("Step 5 : Split the dataset Independent variable and Dependent variable ")
    print(Border)

    X = df.drop(columns=["Class"])
    Y = df ["Class"]

    print("Independent variable are:",X.shape)
    print("Dependent variable are:",Y.shape)
     #---------------------------------------------------------------------
    # Step 6 : Split the dataset trainig and testing part
    #---------------------------------------------------------------------
    print(Border)
    print("Step  6: Split the dataset trainig and testing part ")
    print(Border)

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    print("X_train is:",X_train.shape)
    print("X_test is :",X_test.shape)
    print("Y_train is :",Y_train.shape)
    print("Y_test is:",Y_test.shape)

    #---------------------------------------------------------------------
    # Step 7 : Train the model
    #---------------------------------------------------------------------
    print(Border)
    print("Step 7 : Train the model ")
    print(Border)

    model = DecisionTreeClassifier(criterion="gini",max_depth=3,random_state=42)

    model.fit(X_train,Y_train)
    
    #---------------------------------------------------------------------
    # Step 8 : Test the model
    #---------------------------------------------------------------------
    print(Border)
    print("Step 8 : Test the model ")
    print(Border)

    Y_pred = model.predict(X_test)
    print("Preective Answer is:",Y_pred)

    #---------------------------------------------------------------------
    # Step 9 : Accuracy of the model
    #---------------------------------------------------------------------
    print(Border)
    print("Step 9 : Accuracy of the model ")
    print(Border)

    accuracy = accuracy_score(Y_test,Y_pred)
    print("Accuracy of the model is:",accuracy*100)

    #---------------------------------------------------------------------
    # Step 10 : Confusion Matrix Display
    #---------------------------------------------------------------------
    print(Border)
    print("Step 10 : Confusion Matrix Display ")
    print(Border)

    cm = confusion_matrix(Y_test,Y_pred)
    print(cm)
    
       #---------------------------------------------------------------------
    # Step 11 : Display Classification Report
    #---------------------------------------------------------------------
    print(Border)
    print("Step 11 : Display Classification Report")
    print(Border)

    Result = classification_report(Y_test,Y_pred)
    print(Result)




def main():

     MarvellousWineeCaseStudy("WinePredictor.csv")


if __name__=="__main__":
    main()