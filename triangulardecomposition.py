# 开发人员 ：${桂俊毅}
# 开发时间 ：${2019/11}
# 开发文件 ：triangulardecomposition.py（直接三角分解）
# 开发工具 ：pycharm
import numpy as np
A1=np.array([[1,2,3],
            [2,5,2],
            [3,1,5]])
g= A1.astype(np.float64)       # 转化为float型便于乘除计算

B1 = np.array([[14],
              [18],
              [20]])
h = B1.astype(np.float64)       # 转化为float型便于乘除计算

def sanjiaofenjie(a,b):                         # 将求解过程写在函数内

    U = np.zeros((a.shape[0],a.shape[1]))       # 初始化U

    L = np.zeros((a.shape[0],a.shape[1]))       # 初始化L
    for i in range(a.shape[0]):
        L[i,i] = 1

    for j in range(a.shape[1]):         # 先算出U的第一行元素
        U[0,j]=a[0,j]

    for m in range(a.shape[0]):
        L[m,0] = a[m,0]/U[0,0]          # 再算出L的第一列元素


    for r in range(a.shape[0]):         # 算出剩下的U与L
        for i in range(r,a.shape[1]):
            sum = 0
            sum1 = 0                            # 初始化l*u的累加项的值
            for k in range(r):                  # 循环累加
                sum =sum + L[r, k] * U[k, i]
                sum1 = sum1 + L[i, k] * U[k, r]
            U[r,i] = a[r,i] -sum                    # 计算U中的每个元素
            L[i, r] = (a[i, r] - sum1) / U[r, r]    # 计算L中的每个元素
    print("U=\n",U)
    print("L=\n",L)
"""

    y = np.zeros((a.shape[0],1))        # 定义y
    y[0] = b[0]                         # 算出y1

    for i in range(1,a.shape[0]):       # 算出y2,...,yn
        sum2 = 0
        for k in range(i):              # 求累加项
            sum2 = sum2 + L[i,k]*y[k]
        y[i]=b[i]-sum2
    print("y=",y)

    x=np.zeros((a.shape[0],1))          # 初始化x
    x[a.shape[0]-1] = y[a.shape[0]-1]/U[a.shape[0]-1,a.shape[0]-1]   # 求x[n]

    i = a.shape[0]-2                                                 # 令i=n-1
    for j in range(a.shape[0]-1):   # 求剩余的x中的其它元素，共循环n-1次，分别求x1,..,xn-1
        sum3 = 0
        for k in range(i+1,a.shape[0]):                         # 求累加项
            sum3 = sum3+U[i,k]*x[k]
        x[i] = (y[i]-sum3) /U[i,i]                         # 求出x的每一项
        i = i-1
    return x
print("解向量为x=：\n",sanjiaofenjie(g,h))                # 输出函数的运行结果
"""
print(sanjiaofenjie(g,h))

