# 开发人员 ：${桂俊毅}
# 开发时间 ：${2019/11}
# 开发文件 ：gauss.py(高斯消去法)
# 开发工具 ：pycharm
import numpy as np
A=np.array([[1,2,3],
            [2,5,2],
            [3,1,5]])
Y = np.array([[14],
              [18],
              [20]])

def gauss(a,y): # 定义消元与回代计算的函数
    a = np.hstack((a,y))  # 将a与y写在一起进行消元
    n = 0
    for m in range(1,a.shape[0]):  # m为行，n为列，进行循环消元
        if (a[m,n] == 0):        # 将剩下要消去的元素中首列元素不为零的调到最上面,方便计算
                for j in range(m,a.shape[0]):
                    if (a[j,n] != 0):
                        a[[m,j],:] = a[[j,m],:]  # 交换矩阵中的两行
                        break
        for i in range(m,a.shape[0]):          # m行以下的行进行运算
            a[i] = a[i] - a[n] * (a[i, n] / a[n, n])   # 消元运算
        n = n+1                                        # 列更新
    b = np.split(a,4,axis=1)[3]      # 将消好的矩阵最后一列分割出来赋值给b
    x=np.zeros((A.shape[0],1))       # 定义一个零向量存储解
    N =a.shape[0]-1
    x[N] = b[N]/a[N,N]
    for k in range(1,a.shape[0]):   # 进行回代计算
        sum = 0                     # 定义累加项
        for L in range(N-k+1,a.shape[0]):
            sum =sum + x[L]*a[N-k,L]     # 进行累加
        x[N-k] = (b[N-k]-sum)/a[N-k,N-k]
    return x                             # 输出最终的解
print("解向量X为：\n",gauss(A,Y))

