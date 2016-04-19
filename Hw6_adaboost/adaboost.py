from numpy import *
from random import *
from pylab import *

def read_data(filename):
    xy = loadtxt(filename)
    return (xy)

def training(xy):
    # sort input x and output y by row 0
    xy_sort = sorted(xy, key=lambda tmp: tmp[0])
    
    # sort input x and output y by row 1
    xy_sort = sorted(xy, key=lambda tmp: tmp[1])
    
def step_cost_calculation(xy):
    x = xy[:, 0:-1]
    y = xy[:, -1]


xy_tr = read_data("hw6_adaboost_train.dat")
xy_te = read_data("hw6_adaboost_test.dat")

training(xy_tr)
