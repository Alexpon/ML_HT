from numpy import *
from random import *
from pylab import *
import math

def read_data(filename):
    xy = loadtxt(filename)
    return (xy)

def training(xy_sort0, xy_sort1, u):

    (s_0, threshold_0, err_list_0, cost_0) = step_cost_calculation(array(xy_sort0), 0, u)
    (s_1, threshold_1, err_list_1, cost_1) = step_cost_calculation(array(xy_sort1), 1, u)
    
    if cost_0 < cost_1:
        err = math.sqrt((1-cost_0)/cost_0)
        s = s_0
        u = step_u_calculatioin(s, u, err, err_list_0)
        threshold = threshold_0
        feature = 0
        print("cost = ", cost_0)
    else:
        err = math.sqrt((1-cost_1)/cost_1)
        s = s_1
        u = step_u_calculatioin(s, u, err, err_list_1)
        threshold = threshold_1
        feature = 1
        print("cost = ", cost_1)
    print("thre = ", threshold)
    print("err  = ", err)
    print("row  = ", feature)
    print("s    = ", s)
    print("")
    return (u, log(err), s, threshold, feature)


def step_cost_calculation(xy, col, u):
    x = xy[:,0:-1]
    y = xy[:,-1]
    cost = 1
    err_cnt = 0.0
    err_list_step = []
    for i in (range(len(x)-1)):
        threshold_step = (x[i, col] + x[i+1, col])/2
        for j in range(len(x)):
            if (y[j] != sign(x[j, col]-threshold_step)):
                err_cnt = err_cnt + u[j]
                err_list_step.append(j)
        
        cost_step = err_cnt/sum(u)
        if (cost_step > 0.5):
            s_tmp = -1
            cost_step = 1 - cost_step
        else:
            s_tmp = 1

        if cost > cost_step:
            cost = cost_step
            threshold = threshold_step
            err_list = err_list_step
            s = s_tmp
        err_cnt = 0.0
        err_list_step = []
    return (s, threshold, err_list, cost)
            
def step_u_calculatioin(s, u, err, err_list):
    # if s = -1  --> err_list is change to correct_list
    if(s == -1):
        u = u * err
        for i in err_list:
            u[i] = u[i] / err / err
    else:
        u = u / err
        for i in err_list:
            u[i] = u[i] * err * err
    return u

xy_tr = read_data("hw6_adaboost_train.dat")
xy_te = read_data("hw6_adaboost_test.dat")

# sort input x and output y by row 0
xy_tr_sort0 = sorted(xy_tr, key=lambda tmp: tmp[0])
# sort input x and output y by row 1
xy_tr_sort1 = sorted(xy_tr, key=lambda tmp: tmp[1])
u = 1/len(xy_tr) * ones(len(xy_tr))

iteration = 300
alphas = zeros(iteration)
s_list = zeros(iteration)
thresholds = zeros(iteration)
features = zeros(iteration)
for i in range(iteration):
    print ("Iteration ", i+1)
    (u, alp, s, threshold, feature) = training(xy_tr_sort0, xy_tr_sort1, u)
#    u_input = u
    alphas[i] = alp
    s_list[i] = s
    thresholds[i] = threshold
    features[i] = feature


