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
    while count < 100000: 
        for i in orderlist:
            if y[i] != sign_n(dot((w.T), x[:,i])):
                w = w + dot(y[i], x[:,i])
                count = count + 1
                break
            elif i == len(y)-1:
                return (w, count)
    return (w, count)

def calculate_freq(counter):
    freq = [0]*200
    for i in counter:
        freq[counter[i]] = freq[counter[i]]+1
    return freq

(x, y) = read_data("hw1_15_train.dat")
all_count = []
avg_w = zeros(5)

for i in range(2000):
    w = zeros(5)
    (w, count) = pla(w,x,y)
    avg_w = avg_w + w
    all_count.append(count)

avg_w = avg_w / 2000
print (avg_w)
freq = calculate_freq(all_count)
bar(range(200), freq)
show()
