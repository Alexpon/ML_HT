from numpy import *
from random import *
from pylab import *

def read_data(filename):
    arr = loadtxt(filename)
    x = arr[:, 0:8]
    y = arr[:, -1]
    return (x, y)

def training(x, y, i):
    threshold = 0
    optimal = 0
    cost = 1
    s = 1
    orderlist = arange(len(y))
    shuffle(orderlist)
    for x_index in orderlist:
        threshold = x_tr[x_index, i]
        (tmp_s, tmp_cost) = calculate_cost(x, y, i, threshold)
        if (cost > tmp_cost):
            (s, cost) = (tmp_s, tmp_cost)
            optimal_threshold = threshold
            optimal_i = i
    return (s, optimal_threshold, cost)

def calculate_cost(x, y, i, threshold):
    err_count = 0
    index = 0
    for x_tr in x[:,i]:
        y_tr = sign(x_tr - threshold)
        if (y_tr != y[index]):
            err_count = err_count + 1
        index = index + 1
    if (err_count/len(y) > 0.5):
        return (-1, (1 - err_count/len(y)))
    else:
        return (1, (err_count / len(y)))

def e_out(x, y, s, i, threshold):
    err_count = 0
    index = 0
    for x_te in x[:, i]:
        if(y[index] != s*sign(x_te - threshold)):
            err_count = err_count + 1
        index += 1
    return err_count / len(y)

(x_tr, y_tr) = read_data("hw2_train.dat")
(x_te, y_te) = read_data("hw2_test.dat")
(s, threshold, cost) = ([], [], [])

for i in range(8):
    (tmp_s, tmp_threshold, tmp_cost) = training(x_tr, y_tr, i)
    threshold.append(tmp_threshold)
    s.append(tmp_s)
    cost.append(tmp_cost)

optimal_index = cost.index(min(cost))

print ("The Decision Stump:")
print ("s = ", s[optimal_index])
print ("threshold = ", threshold[optimal_index])
print ("Ein = ", cost[optimal_index])
print ("Eout = ", e_out(x_te, y_te, s[optimal_index], 
            optimal_index, threshold[optimal_index]))
