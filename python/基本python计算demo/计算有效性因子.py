import math
def cal():
    ebc = 0.4
    gelta = 0.8
    pos = 3.0 #前三者均是给定的初始值；
    k = 0.0561 # 是kinetic constant,可以根据A和E之间的关系进行计算；取平均值；
    L = (5e-4) / 2 #流化床厚度的一半
    k3 = k/(1-ebc)
    e1 = math.e
    Dini = 1.52e-5 # 扩散系数初始值；与气体的种类有关系；CO2-CO
    # print(Dini* 100000)
    Dco2 = Dini * pow((800+273)/(25+273), 1.75) # 上方的k对整体的影响很小；取1/10也才下降很小一部分；
    # 1073/298 与反应的温度有一定的关系；
    De = Dco2 * ebc * gelta / gelta
    x = L * pow(k3/De, 0.5)
    res1 = pow(e1, x) - pow(e1, -x)
    res2 = pow(e1, x) + pow(e1, -x)
    res = res1 / (res2 * x)
    print(res)
    
if __name__ == "__main__":    
    cal()