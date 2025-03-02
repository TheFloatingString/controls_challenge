from sklearn.neural_network import MLPClassifier
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def train_ffnn_simple():
    # read data
    df = pd.read_csv("data/00000.csv")
    # drop NaN rows
    df = df.dropna()
    print(df.head())
    # correctly label X and y data
    X_data = df[["vEgo", "aEgo", "roll", "targetLateralAcceleration"]].values
    y_data = df["steerCommand"].values
    # create classses
    y_data = np.where(np.abs(y_data)>0.2,1,0)
    # train-test split
    X_train, X_test, y_train, y_test = train_test_split(X_data, y_data, test_size=0.2)
    # fit multi-layer perceptron
    clf = MLPClassifier(hidden_layer_sizes=(3,3),max_iter=int(1e5))
    clf.fit(X_train, y_train)
    # print score
    print(clf.score(X_test, y_test))


if __name__ == "__main__":
    train_ffnn_simple()
