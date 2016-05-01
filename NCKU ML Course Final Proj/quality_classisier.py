from numpy import *
from random import *
from pylab import *
from csv import *
import training

def read_data(filename):
    csvfile = open(filename)
    data = reader(csvfile, delimiter=';')
    xy = []
    flat = False

    for row in data:
        if(flat):
            if (int(row[-1]) > 5):
                row[-1] = 1
            else:
                row[-1] = -1
            xy.append(row)
        flat = True
    shuffle(xy)
    return (xy[0:int(len(xy)/5)], xy[int(len(xy)/5):len(xy)])



(xy_te, xy_tr) = read_data("winequality-red.csv")
#(xy_te, xy_tr) = read_data("winequality-white.csv")

# initialize
u = 1/len(xy_tr) * ones(len(xy_tr))
cost = 1
feature = 0
iteration = 30
alphas = zeros(iteration)
s_list = zeros(iteration)
thresholds = zeros(iteration)
features = zeros(iteration)
#costs = zeros(iteration)
acc = zeros(iteration)

for i in range(iteration):
    cost = 1
    for j in range(10):
        xy_tr_sort = sorted(xy_tr, key=lambda tmp: tmp[j])
        trainer = training.Training(u, array(xy_tr_sort), j)
        (s_tmp, threshold_tmp, err_list_tmp, cost_tmp) = trainer.iterater_optimal()
        if (cost > cost_tmp):
            (s, threshold, err_list, cost) = (s_tmp, threshold_tmp, err_list_tmp, cost_tmp)
            feature = j
    err = sqrt((1-cost)/cost)
    u = trainer.update_uvalue(s, err, err_list)
    print (u)    
    alphas[i] = log(err)
    s_list[i] = s
    thresholds[i] = threshold
    features[i] = feature
    
    #costs[i] = cost
    print ("Iter ", i)
    print ("alpha: ", alphas[i])
    print ("s    : ", s)
    print ("thre : ", threshold)
    print ("row  : ", feature)
    print ("cost : ", cost)

    trainer = training.Training(u, array(xy_tr), 0)
    e_out = trainer.testing(alphas, s_list, thresholds, features, iteration)
    acc[i] = 1-e_out
    print ("Test E out = ", e_out)
    print ("Accurate: ", 1-e_out)
    
"""
trainer = training.Training(u, array(xy_te), 0)
e_out = trainer.testing(alphas, s_list, thresholds, features, iteration)
print ("Test E out = ", e_out)
print ("Accurate: ", 1-e_out)
"""
print ("U:")
print ("\t", features)
bar(range(iteration), acc)
show()
