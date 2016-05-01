from numpy import *

class Training:
    def __init__(self, u, xy, col):
        self.u = u
        self.xy = xy
        self.col = col
        
    def iterater_optimal(self):
        x = self.xy[:,0:-1]
        y = self.xy[:,-1]
        cost = 1 
        err_cnt = 0.0
        err_list_step = []
        for i in (range(len(x)-1)):
            if(x[i, self.col] != x[i+1, self.col]):
                threshold_step = (float(x[i, self.col]) + float(x[i+1, self.col]))/2
                for j in range(len(x)):
                    if (int(y[j]) != sign(float(x[j, self.col])-threshold_step)):
                        err_cnt = err_cnt + self.u[j]
                        err_list_step.append(j)
                cost_step = err_cnt/sum(self.u)
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
        print (cost)
        return (s, threshold, err_list, cost)
                

    def update_uvalue(self, s, err, err_list):
        # if s = -1  --> err_list is change to correct_list
        if(s == -1):
            err = 1/err

        self.u = self.u / err
        for i in err_list:
            self.u[i] = self.u[i] * err * err
        
        return self.u


    def testing(self, alphas, s_list, thresholds, features, index):
        x = self.xy[:,0:-1]
        y = self.xy[:,-1]
        sum_of_g = 0
        err_count = 0
        for i in range(len(x)):
            for j in range(index):
                sum_of_g += float(alphas[j]) * int(s_list[j]) * sign(float(x[i,int(features[j])])-float(thresholds[j]))
            
            if (int(y[i]) != sign(sum_of_g)):
                err_count += 1
            
            sum_of_g = 0
        return err_count / len(y)

