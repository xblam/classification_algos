import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


"""
* get the datapoints from kaggle
* split the datapoints into test and training sets (maybe even validation sets?)
* then finish training the knn
"""

# read in the csv file
def read_file(file_name):
    df = pd.read_csv(file_name)
    print(df.head())
    X = df.drop("Personality", axis=1)
    y = df["Personality"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


if __name__ == "__main__":
    read_file('personality_dataset.csv')
    
