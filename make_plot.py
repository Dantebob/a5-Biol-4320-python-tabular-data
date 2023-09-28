#! /bin/python3

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


def make_plot(dataframe, file_name):
    """
    Takes in dataframe and file_name as arguements then creates a plot with a regression line in the form of <file_name>_regress.png

    Parameters
    -------------------
    dataframe : a class object of pandas and a 2D array
        dataframe is used to make points and line of regression on the plot.

    Returns
    ----------
    None

    Creates
    --------------
    a plot in the form of <file_name>_regress.png
    """
    x = dataframe.petal_length_cm
    y = dataframe.sepal_length_cm
    regression = stats.linregress(x, y)
    slope = regression.slope
    intercept = regression.intercept
    plt.scatter(x, y, label = 'Data')
    plt.plot(x, slope * x + intercept, color = "orange", label = 'Fitted line')
    plt.xlabel("Petal length (cm)")
    plt.ylabel("Sepal length (cm)")
    plt.legend()
    file_name = str(file_name).replace(" ", "_") + "_regress.png"
    plt.savefig(file_name)
    #plt.clf is to clear fig after saving it so it is not added to the next plot.
    plt.clf()
    return

if __name__ == '__main__':
    dataframe = pd.read_csv("iris.csv")

    #long_flowers = dataframe[dataframe.petal_length_cm > 5.9]
    setosa = dataframe[dataframe.species == "Iris_setosa"]
    virginica = dataframe[dataframe.species == "Iris_virginica"]
    versicolor = dataframe[dataframe.species == "Iris_versicolor"]
    make_plot(setosa, "Iris setosa")
    make_plot(virginica, "Iris virginica")
    make_plot(versicolor, "Iris versicolor")

