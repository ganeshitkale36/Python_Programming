
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score

def MarvellousHead(Datapath):
    Border = "-"*50
    #--------------------------------------------------------------------------------------
    # Step 1 : Load the Dataset 
    #--------------------------------------------------------------------------------------
    
    print(Border)
    print("Step 1 : Load the Dataset:")
    print(Border)

    df = pd.read_csv("MarvellousHeadBrain.csv")

    print(df.shape)

    print("First few entries of data:",df.head())

    Border = "-"*50
    #--------------------------------------------------------------------------------------
    # Step 2 : Check missing columns 
    #--------------------------------------------------------------------------------------
    
    print(Border)
    print("Step 2 : Check missing columns ")
    print(Border)

    print("Missing values per(Column)\n:",df.isnull().sum())

    Border = "-"*50
    #--------------------------------------------------------------------------------------
    # Step 3 : Display statistical Summary
    #--------------------------------------------------------------------------------------
    
    print(Border)
    print("Step 3 : Display statistical Summary ")
    print(Border)

    print(df.describe())

    #--------------------------------------------------------------------------------------
    # Step 4 : Correlation Between Columns
    #--------------------------------------------------------------------------------------
    
    print(Border)
    print("Step 4 : Correlation Between Columns  ")
    print(Border)

    print(df.corr())

    # End The Analysis Part AND
    # We Start the Model BUild Process

      #--------------------------------------------------------------------------------------
    # Step 5 : Split the dataset into training and testing part
    #--------------------------------------------------------------------------------------
    
    print(Border)
    print("Step  5 : Split the dataset into taining and testing part  ")
    print(Border)

    X = df[["Gender","Age Range","Head Size(cm^3)"]]
    Y = df["Brain Weight(grams)"]

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    print("X_train is:",X_train.shape)
    print("X_test is:",X_test.shape)
    print("Y_train is:",Y_train.shape)
    print("Y_test is:",Y_test.shape)

    #--------------------------------------------------------------------------------------
    # Step 6 : Train the model
    #--------------------------------------------------------------------------------------
    
    print(Border)
    print("Step 6 : Train the model")
    print(Border)

    model = LinearRegression()
    model.fit(X_train,Y_train)

    #--------------------------------------------------------------------------------------
    # Step 7 : Test the model
    #--------------------------------------------------------------------------------------
    
    print(Border)
    print("Step 7 : Test the model")
    print(Border)

    Y_pred = model.predict(X_test)
    print("Predicted Values:",Y_pred)

    #--------------------------------------------------------------------------------------
    # Step  8: Evaluate the model
    #--------------------------------------------------------------------------------------
    
    print(Border)
    print("Step 8 : Evaluate the model")
    print(Border)

    MSE = mean_squared_error(Y_test,Y_pred)
    RMSE = np.sqrt(MSE)
    R2 = r2_score(Y_test,Y_pred)

    print("Mean Sqaured error is:",MSE)
    print("Root mean Squared error is:",RMSE)
    print("R2 values is:",R2)

    #--------------------------------------------------------------------------------------
    # Step 9 : Calculate the  Coefficient 
    #--------------------------------------------------------------------------------------
    
    print(Border)
    print("Step 9 : Calculate the  Coefficient")
    print(Border)
    
    for column,value in zip(X.columns,model.coef_):
        print(f"{column}:{value}")

    print("Intercept:",model.intercept_)

    #--------------------------------------------------------------------------------------
    # Step 10 :  Compare the Actual and predicted Class
    #--------------------------------------------------------------------------------------
    
    print(Border)
    print("Step 10 : Actual and predicted values")
    print(Border)

    Result = pd.DataFrame({
            "Actual Brain_weight" : Y_test.values,
            "Predcited Brain_weight" : Y_pred
    })
    print(Result.head(10))

    #--------------------------------------------------------------------------------------
    # Step 11:  Plot the Actual Brain_weight VS Predcited Brain_weight
    #--------------------------------------------------------------------------------------
    
    print(Border)
    print("Step 11:  Plot the Actual Brain_weight VS Predcited Brain_weight")
    print(Border)

    plt.figure(figsize=(8,5))
    plt.scatter(Y_test,Y_pred)
    plt.title("Actual Brain_weight VS Predcited Brain_weight")
    plt.xlabel("Actual Brain_weight")
    plt.ylabel("Predicted Brain_weight")
    plt.grid(True)
    plt.show()

def main():
    MarvellousHead("MarvellousHeadBrain.csv")



if __name__=="__main__":
    main()


    # test_size = 0.2 the value of r2 is 0.74 Accuracy
     # test_size = 0.1 the value of r2 is 0.80 Accuracy