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


def main():

    Border = "-"*50
    print(Border)
    MarvellousAdvertise("Advertising.csv")
    print(Border)

if  __name__=="__main__":
    main()