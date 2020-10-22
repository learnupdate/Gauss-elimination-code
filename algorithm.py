# 开发人员 ：${桂子}
# 开发时间 ：${2020/1}
# 开发文件 ：algorithm.py
# 开发工具 ：pycharm
import numpy as np
# 求逆，求x
flag = True
# flag = False
if flag:
    # a*x=b  输入a,b求x
    a = np.array([[1,0.5,4,3,3],
                [2,1,7,5,5],
                [0.25, 0.14, 1, 0.5, 0.3],
                [0.3, 0.2, 2, 1, 1],
                [0.3, 0.2, 3, 1, 1]])
    b = np.array([[0.2371],
                  [0.4290],
                  [0.1450],
                  [0.0890],
                  [0.0997]])

    def jiejuzhen(gf,gn):             # 解矩阵
        # gf = np.linalg.inv(g)  # 求逆
        M = np.dot(gf, gn)  # 点积
        return M

        print(M)   # 输出x

print("hhhhhhh",jiejuzhen(a,b))

# 插值多项式
# 两点插值
# flag = True
flag = False
if flag:
    y1=2.0
    y0=1.0
    x1=3.0
    x0=1.0
    x = float(input("输入x:"))
    l=float((y1-y0)/(x1-x0))
    m=float(y0+l*(x-x0))
    print("两点插值结果：",m)

# flag = True
flag = False
if flag:
    # 三点插值
    y0=10
    y1=11
    y2=12
    x0=100
    x1=121
    x2=144
    x = float(input("输入x:"))

    X1=float(((x-x1)*(x-x2))/((x0-x1)*(x0-x2)))
    X2=float(((x-x0)*(x-x2))/((x1-x0)*(x1-x2)))
    X3=float(((x-x0)*(x-x1))/((x2-x0)*(x2-x1)))
    m1=float(y0*X1+y1*X2+y2*X3)
    print("三点插值公式的结果为：\n",m1)

# 求w(x)=(x-x0)*(x-x1)*(x-x2)
# flag = True
flag = False
if flag:
    x0 = 100
    x1 = 121
    x2 = 144
    x = float(input("输入x:"))
    w = (x-x0)*(x-x1)*(x-x2)
    print("w(x)=",w)

# flag = True
flag = False

#  输入x1,x2,......,xn
#  分别输入x和xk求相应的Ak
if flag:
    x = float(input("输入x:"))
    xk = float(input("输入xk:"))
    X=[100.0,121.0,144.0]                   #     输入x1,x2,......,xn
    L1=1.0
    L2=1.0
    for i in range(len(X)):
        if (x != X[i]):
            L1 = float(L1 * (x - X[i]))
        if  xk != X[i]:
            L2 = float(L2 * (xk - X[i]))
    Ak=float(L1/L2)
    print("Ak=",Ak)

