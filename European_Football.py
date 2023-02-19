import csv
import random
from sklearn import tree, linear_model
import pandas as pd
import numpy as np

path = "Dataset/events_premier-league_2022-23.csv"
my_tree = tree.DecisionTreeClassifier()
col_list_data = ["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]


try:
    # with open(path, "r", usecols=col_list) as file:
    #     reader = csv.reader(file)
    #     dataframe = list(reader)
    #     print(dataframe)

    dataframe = pd.read_csv(path)
    label = pd.read_csv(path)
    print(dataframe.values)


except FileNotFoundError:
    print("That file wasn't found")
