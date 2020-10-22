# 开发人员 ：${桂俊毅}
# 开发时间 ：${2019/11}
# 开发文件 ：list_element.py（列主元消去法）
# 开发工具 ：pycharm
import numpy as np

A1=np.array([[4,0,-1],
            [2,1,-2],
            [0,3,2]])
A = A1.astype(np.float64)       # 转化为float型便于乘除计算


Y1 = np.array([[7],
              [-1],
              [4]])
Y = Y1.astype(np.float64)       # 转化为float型便于乘除计算



def maxvalue(b,m,n):       # 在一个矩阵b中从第m行以下从第n列中寻找最大值,返回最大值所处的行数
    index = m
    max = abs(b[m,n])
    for i in range(m,b.shape[0]):
        if max<abs(b[i,n]):
            max = b[i,n]
            index = i
    return index                        # 返回列数
# print("第0行开始在第2列中最大的元素所处的行为：",maxvalue(A,1,1))

def adjust(c,m,m1):    # 将矩阵c中m行元素调到m1行。
    tem1 = np.zeros((1,c.shape[1]))  # 存储行
    for j in range(c.shape[1]):   # 换行
        tem1 = c[m1,j]
        c[m1,j] = c[m,j]
        c[m,j] = tem1
    return c    # 返回矩阵




def mainelement(a,y):         # 完全主元素消去法
    test = 0                                                    # test測試最大值是否为零，即方程组是否有解。test=0有解，test=1无解
    a = np.hstack((a,y))                                        # 将a与y写在一起进行消元
    n = 0

    adjust(a,maxvalue(a,0,0),0)       # maxvalue(a,0,0)返回最大值所处的行，adjust（）将此行与第0行进行交换
    if a[0,0] == 0:                                             # 若交换后的最大值为零，说明无解
        test = 1
    print("第一次换行后的矩阵为：\n",a)
    for m in range(1,a.shape[0]):                                 # m为行，n为列，进行循环消元

        for i in range(m,a.shape[0]):                               # m行以下的行进行运算
            ax = a[i, n] / a[n, n]
            for l in range(a.shape[1]):
                a[i,l]-=a[n,l] *ax            # 消元运算
        print("消元后的矩阵为：\n",a)
        n = n+1                                                     # 列更新
        if m<a.shape[0]-1:
            adjust(a,maxvalue(a,m,n),m)                # 每循环一次寻找最大值所处的行，交换两行
            if a[m,n] == 0:                             # 若交换后的最大值为零，说明无解
                test = 1
            print("换行后的矩阵为：\n",a)

    b = np.split(a,4,axis=1)[3]                 # 将消好的矩阵最后一列分割出来赋值给b
    print("消元之后的矩阵为：\n",a)

    x=np.zeros((A.shape[0],1))                # 定义一个零向量存储解
    N =a.shape[0]-1
    x[N] = b[N]/a[N,N]
    for k in range(1,a.shape[0]):               # 进行回代计算
        sum = 0
        for L in range(N-k+1,a.shape[0]):
            sum =sum + x[L]*a[N-k,L]
        x[N-k] = (b[N-k]-sum)/a[N-k,N-k]
    if test == 1:                                # 若test=1，说明无解,不返回任何值
        return
    else:
        return x                                    # 输出最终的解

print("解向量X为：\n",mainelement(A,Y))

