from sklearn.linear_model import LogisticRegression
import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np


def train_logistic_regression(pkl_filepath=""):
    # read data
    df = pd.read_csv("data/00000.csv")
    # drop NaN rows
    df = df.dropna()
    print(df.head())
    # correctly label X and y data
    X_data = df[["vEgo", "aEgo", "roll", "targetLateralAcceleration"]].values
    y_data = df["steerCommand"].values
    # create classes
    y_data = np.where(np.abs(y_data) > 0.2, 1, 0)
    # train-test split
    X_train, X_test, y_train, y_test = train_test_split(X_data, y_data, test_size=0.2)
    # fit Logisitic regression
    clf = LogisticRegression()
    clf.fit(X_train, y_train)
    # print score
    print(clf.score(X_test, y_test))

    # export to .pkl file


if __name__ == "__main__":
    train_logistic_regression()
