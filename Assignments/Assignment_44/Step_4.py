import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_squared_error

def MarvellousAdvertise(Datpath):
    Border = "-"*40
    #--------------------------------------------------------------------
    # Step 1 : Load the datset
    #----------------------------------------------------------------------
    print(Border)
    print("Step 1 : Load the dataset")
    print(Border)

    df = pd.read_csv("Advertising.csv")
    print(df.shape)

    print("Few Entries of Dataset:")
    print(df.head())

    #--------------------------------------------------------------------
    # Step 2 : Missing values from dataset
    #----------------------------------------------------------------------
    print(Border)
    print("Step  2 : Missing values from dataset")
    print(Border)

    print("Missing values per (column):")
    print(df.isnull().sum())

    #--------------------------------------------------------------------
    # Step 2 : Statisical report of dataset
    #----------------------------------------------------------------------
    print(Border)
    print("Step  2 : Statisical report of dataset")
    print(Border)

    print("Statistical report of dataset:")
    print(df.describe())

    
    #--------------------------------------------------------------------
    # Step 3 : Check the independent and dependent variable
    #----------------------------------------------------------------------
    print(Border)
    print("Step 3 : Check the independent and dependent variable")
    print(Border)

    X = df[["TV","radio","newspaper"]]
    Y = df["sales"]

    print(X.shape)
    print(Y.shape)

     #--------------------------------------------------------------------
    # Step 4 : Find the Correlation
    #----------------------------------------------------------------------
    print(Border)
    print("Step 4 : Find the Correlation")
    print(Border)

    print("Correlation is:",df.corr())

     #--------------------------------------------------------------------
    # Step  5 :Split the dataset training and testing part
    #----------------------------------------------------------------------
    print(Border)
    print("Step  5 :Split the dataset training and testing part")
    print(Border)

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)
    print("X_train is :",X_train.shape)
    print("X_test is :",X_test.shape)
    print("Y_train is:",Y_train.shape)
    print("Y_test is:",Y_test.shape)

    #--------------------------------------------------------------------
    # Step  6: Create & train the model
    #----------------------------------------------------------------------
    print(Border)
    print("Step  6: Build  & train the model")
    print(Border)

    model = LinearRegression()
    model.fit(X_train,Y_train)

      #--------------------------------------------------------------------
    # Step  7 : Test the model
    #----------------------------------------------------------------------
    print(Border)
    print("Step  7 : Test the model")
    print(Border)

    Y_pred = model.predict(X_test)
    print(Y_pred)

    #--------------------------------------------------------------------
    # Step  8 : Evaluate  the model
    #----------------------------------------------------------------------
    print(Border)
    print("Step  8 : Evaluate  the model")
    print(Border)

    MSE = mean_squared_error(Y_test,Y_pred)
    print("Mean Squared Error is :",MSE)

    RMSE = np.sqrt(MSE)
    print("Root mean squared error is :",RMSE)

    R2 = r2_score(Y_test,Y_pred)
    print("R2 value is:",R2*100)

    

def main():

    Border = "-"*50
    print(Border)
    MarvellousAdvertise("Advertising.csv")
    print(Border)

if  __name__=="__main__":
    main()