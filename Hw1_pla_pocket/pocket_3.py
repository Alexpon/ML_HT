from numpy import *
from random import shuffle
from pylab import *

def read_data(filename):
    arr = loadtxt(filename)
    x = append(linspace(1,1,len(arr)), arr[:,0:4].T)
    x.shape = (5,len(arr))
    y = arr[:,-1]
    return (x, y);

def sign_n(tmp):
    if(tmp==0):
        return -1
    return sign(tmp)

def pla(w, x, y):
    count = 0
    orderlist = arange(len(y))
    shuffle(orderlist)
    while count <= 100: 
        for i in orderlist:
            if y[i] != sign_n(dot((w.T), x[:,i])):
                w = w + dot(y[i], x[:,i])
                count = count + 1
                break
            elif i == len(y)-1:
                return (w, count)
    return (w, count)

def test(w, x, y):
    err_count = 0
    for i in range(len(y)):
        if y[i] != sign_n(dot((w.T), x[:,i])):
            err_count = err_count + 1
    return err_count

def calculate_freq(counter):
    freq = [0]*500
    for i in counter:
        freq[i] = freq[i]+1
    return freq

(x_tr, y_tr) = read_data("hw1_18_train.dat")
(x_te, y_te) = read_data("hw1_18_test.dat")

all_err = []
err = 500
pocket = (zeros(5), 500)

for i in range(2000):
    w = zeros(5)
    (w, count) = pla(w, x_tr, y_tr)
    err = test(w, x_te, y_te)
    all_err.append(err)
    if err < pocket[1]:
        pocket = (w, err)

count = calculate_freq(all_err)
x_bar = linspace(0.0,1.0,500)
bar(x_bar, count, width=0.0001, color=(0.2588,0.4433,1.0))
title('Err vs. Freq for 100 updates')
xlabel('Error Rate')
ylabel('Frequency')
show()
