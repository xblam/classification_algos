import pandas as pd
from sklearn.model_selection import train_test_split

class BensKNN:
    
    def __init__(self, k=3, file_name):
        df = pd.read_csv(file_name)
        self.datasettsX = df.drop('Personality')

    def read_data(self, file_name):
        df = pd.read_csv(file_name)
        print(df.head())

        # now we make the test and train datasets
        self. X = df.drop("Personality", axis=1)
        y = df["Personality"]
        print(X.head())
        print(y.head())


    if __name__ == "__main__":
        read_data("personality_dataset.csv")