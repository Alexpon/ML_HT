from numpy import *
from random import *
from pylab import *
from csv import *

def read_data(filename):
    csvfile = open(filename)
    data = reader(csvfile, delimiter=';')
    x = []
    y = []
    cnt = 0
    for row in data:
        x.append(row[0:-1])
        y.append(row[-1])
        cnt += 1
    return (array(x)[1:cnt], array(y)[1:cnt], cnt-1)
    # size = cnt-1 扣除第一列


(x_red, y_red, size_red) = read_data("winequality-red.csv")
(x_white, y_white, size_white) = read_data("winequality-white.csv")
(x_mix, y_mix) = (concatenate((x_red,x_white)), concatenate((y_red, y_white)))

