###最小二乘法试验###
import numpy as np
from scipy.optimize import leastsq

class Cal_fit(object):
    def __init__(self):
        self.p0=[1, 1] # 参数迭代计算时的初始值，即参数个数；
        
    def func(self,p,x):
        k,b=p
        return k*x+b

    def error(self,p,x,y,s):
        return self.func(p,x)-y #x、y都是列表，故返回值也是个列表

    def interation(self, Xi=0, Yi=0):
        Xi=np.array([8.19,2.72,6.39,8.71,4.7,2.66,3.78])
        Yi=np.array([7.01,2.78,6.47,6.71,4.1,4.23,4.05])
        s="Test the number of iteration" #试验最小二乘法函数leastsq得调用几次error函数才能找到使得均方误差之和最小的k、b
        Para=leastsq(self.error,self.p0,args=(Xi,Yi,s)) #把error函数中除了p以外的参数打包到args中
        k,b=Para[0]
        print("k=",k,'\n',"b=",b)        
        err = np.sum(np.square(Yi-(k * Xi + b)))
        ssr = np.sum(np.square(Yi-np.mean(Yi)))
        r2 = 1-err/ssr
        print("r2 of Excel: ", r2)
        print("r2 of Origin: ", 1-(1-r2)*(np.size(Xi)-1)/(np.size(Xi)-len(self.p0)))

if __name__ == "__main__":
    cal = Cal_fit()
    cal.interation()


"""
###绘图，看拟合效果###
import matplotlib.pyplot as plt

plt.figure(figsize=(8,6))
plt.scatter(Xi,Yi,color="red",label="Sample Point",linewidth=3) #画样本点
x=np.linspace(0,10,1000)
y=k*x+b
plt.plot(x,y,color="orange",label="Fitting Line",linewidth=2) #画拟合直线
plt.legend()
plt.show()
"""



