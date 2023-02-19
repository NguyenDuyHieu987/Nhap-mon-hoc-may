import csv
import random
from sklearn import tree, linear_model
import pandas as pd
import numpy as np

path = "Dataset\\iris.csv"
my_tree = tree.DecisionTreeClassifier()
col_list_data = ["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]


try:
    # with open(path, "r", usecols=col_list) as file:
    #     reader = csv.reader(file)
    #     dataframe = list(reader)
    #     print(dataframe)

    dataframe = pd.read_csv(path, usecols=col_list_data)
    label = pd.read_csv(path, usecols=["Species"])

    sl_train = int(len(dataframe.values) * 0.8)

    dataframe_train = dataframe[:sl_train].values
    label_train = label[:sl_train].values

    dataframe_test = dataframe[sl_train:].values
    label_test = label[sl_train:].values

    # convert to list of list
    result = my_tree.fit(dataframe_train, label_train)
    predict = result.predict(dataframe_test)

    # predict_2d = np.reshape(predict, (-1, 1))
    # print(predict_2d)
    # print(predict_2d == label_test)

    label_test_1d = label_test.flatten()
    # print(label_test_1d)
    print(predict)
    print(predict == label_test_1d)

except FileNotFoundError:
    print("That file wasn't found")
