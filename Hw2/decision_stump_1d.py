from numpy import *
from random import *
from pylab import *


def generate_testing_data():
    x = [uniform(-1,1) for i in range(20)]
    y = sign(x)
    return (x, y)

def generate_training_data():
    x = [uniform(-1,1) for i in range(20)]
    y = sign(x)
    for i in range(len(y)):
        if (random() <= 0.2):
            y[i] = -y[i]
    return (x, y)

def training(x, y):
    threshold = 0
    optimal = 0
    cost = 1
    s = 1       # 1: RHS positive, 0: RHS negative
    for x_tr in x:
        threshold = x_tr
        if (cost > calculate_cost(x, y, threshold)[1]):
            (s, cost) = calculate_cost(x, y, threshold)
            optimal = threshold
    return (s, optimal)

def calculate_cost(x, y, threshold):
    err_count = 0
    index = 0
    for x_tr in x:
        y_tr = sign(x_tr - threshold)
        if (y_tr != y[index]):
            err_count = err_count + 1
        index = index + 1
    if (err_count/len(y) > 0.5):
        return (-1, (1 - err_count/len(y)))
    else:
        return (1, (err_count / len(y)))

def e_in_out(x, y, s, threshold):
    err_count = 0
    index = 0
    for x_te in x:
        if(y[index] != s*sign(x_te - threshold)):
            err_count = err_count + 1
        index += 1
    return err_count / len(y)

ein = 0
eout = 0
ein_sum = 0
eout_sum = 0
e_list = []
for i in range(5000):
    (x_tr, y_tr) = generate_training_data()
    (x_te, y_te) = generate_training_data()
    (s, threshold) = training(x_tr, y_tr)
    ein = e_in_out(x_tr, y_tr, s, threshold)
    eout = e_in_out(x_te, y_te, s, threshold)
    e_list.append(ein)
    ein_sum += ein
    eout_sum += eout

eout = eout_sum/5000
ein = ein_sum/5000
print ("Ein: ", ein)
print ("Eout: ", eout)
bar(range(len(e_list)), e_list)
show()
