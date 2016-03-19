from numpy import *

def read_data(filename):
    arr = loadtxt(filename)
    x = append(linspace(1,1,len(arr)), arr[:,0:4].T)
    x.shape = (5,len(arr))  # 5*400 array
    y = arr[:,-1]
    return (x, y);

def sign_n(tmp):
    if(tmp==0):
        return -1
    return sign(tmp)

def pla(w, x, y):
    count = 0
    while count < 100000:
        for i in range(len(y)):
            if y[i] != sign_n(dot((w.T), x[:,i])):
                w = w + dot(y[i], x[:,i])
                count = count + 1
                last = i
                break
            elif i == len(y)-1:
                return (w, count, last)
    return (w, count, last)


(x, y) = read_data("hw1_15_train.dat")
w = zeros(5)
(w, count, last) = pla(w,x,y)
print (w)
print (count)
print (last)
