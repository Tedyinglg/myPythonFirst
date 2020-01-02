import numpy as np
def cal_temp():
    E, hr, ypsl, D, cp = 1.98e5, 5.4e5, 0.95, 0.05, 1465
    # activation energy, radiant heat transfer coefficient, y bu si long ?
    # D: diameter of hot plate, m. cp: ??
    L=0.010;densb=641.2;Ta=293;xgm=5.67e-8 # Stefan-B constant.
    R=8.314;k=0.13;dt=0.001;dl=1/100 # 
    AA=13956159753432;Tp=573 # 300 oC AA: pre-exponential factor
    # L: thickness of coal dust layer 1cm?, densb: packing density of dust layer； 
    # Ta = initial temp; xgm: R, k: ; dt: 
    # dt; dl; AA, Tp: temperature of surface
    Ah=k/dl; Ai=dl/dt+2*k/dl;
    # 
    wlgta=E*Ta/(R*Tp*Tp)  # cita(a); 
    wlgtp=E/(R*Tp) # cita()
    c=np.ones(99,1)  #                                                                      
    c=wlgta*c # 将cita * c，c是初始值，乘以c后，再组合成新的c
    c=[wlgtp, c] # cita 
    temp = 100
    f=np.zeros(0,temp)
    for j in range(1,temp):
        for i in range(2,99):   
            b[i,1]=dl*c[i,1]/dt+((E*L*L*AA*Hr*densb*dl)*exp(-pow(E/(R*Tp),2)/c[i,1]))/(R*Tp*Tp)
            # b是矩阵
            i=i+1
        h=4.13*(((c(100,1)*R*Tp*Tp/E-Ta)/(3.14^0.5*D/2))^0.25)
        
        An=dl/dt+ h*L+ k/dl+ L*ypsl*xgm*((R*Tp*Tp/E)^3)*c(100,1)^3   # c(100,1) 有问题
        
        Bn=dl/dt*c(100,1)+h*L*wlgta+L*ypsl*xgm*((R*Tp*Tp/E)^3)*wlgta^4+E*L*L*AA*Hr*densb*dl/R/Tp/Tp*exp(-(E/R/Tp)^2/c(100,1))
        
        B=b # 前面的矩阵；
        B=[B,Bn]
        B[1,1]=wlgtp # 更新B矩阵里面的(1,1)值为wlgtp
        
        preA=ones(100,1)
        
        Adj1=diag(preA) # 主对角阵为1，剩下的不变；
        
        Ascdj1=diag(preA,1) # 改变矩阵上方的第一斜对角线的值
        Ascdj1=Ascdj1[1:100,1:100] # s 上
        
        Axcdj1=diag(preA,-1) # 改变矩阵下方的第一斜对角线的值
        Axcdj1=Axcdj1[1:100,1:100] # x 下
        
        Adj2=Adj1*Ai # 
        
        Ascdj2=Ascdj1 * Ah
        Axcdj2=Axcdj1*Ah
        
        A=Adj2-Ascdj2-Axcdj2
        A[100,100]=An
        A[1,1]=1
        A[1,2]=0
        x=A.l * B
        f[:,j]=x
        c=x
        print(c)
        
if __name__ == "__main__":
    cal_temp()