# 开发人员 ：${桂俊毅}
# 开发时间 ：${2019/11}
# 开发文件 ：mainelement.py（完全主元素消去法）
# 开发工具 ：pycharm
import numpy as np
A1=np.array([[1,2,-2],
            [1,1,1],
            [2,2,1]])
A = A1.astype(np.float64) # 转化为float便于乘除计算
print("矩阵A为\n",A)

Y1 = np.array([[1],
              [3],
              [5]])
Y = Y1.astype(np.float64)
print("向量Y为：\n",Y)

def maxvalue(b,m,n): # 在一个矩阵b中从第m行和第n列以后的元素中寻找绝对值最大的,返回最大值所处的行列
    index = [0,0]
    max = abs(b[0,0])  # abs()取绝对值
    for i in range(m,b.shape[0]):
        for j in range(n,b.shape[1]-1):  #并入的b向量不计入
            if max<abs(b[i,j]):
                max = b[i,j]
                index[0] = i
                index[1] = j
    return index
# print("第0行列开始，最大的元素为：",maxvalue(2,2,A))

def adjust(c,m,n,m1,n1):    # 将矩阵c中m行元素调到m1行。第n列元素调到第n1列
    tem1 = np.zeros((1,c.shape[1]))  # 存储行
    tem2 = np.zeros((c.shape[0],1))   # 存储列
    for i in range(c.shape[0]):   # 换列
        tem2 = c[i,n1]
        c[i,n1] = c[i,n]
        c[i,n] = tem2
    for j in range(c.shape[1]):   # 换行
        tem1 = c[m1,j]
        c[m1,j] = c[m,j]
        c[m,j] = tem1
    return c    # 返回矩阵

def mainelement(a,y):         # 完全主元素消去法
    test = 0        # test測試最大值是否为零，即方程组是否有解。test=0有解，test=1无解
    a = np.hstack((a,y))  # 将a与y写在一起进行消元
    n = 0

    adjust(a,maxvalue(a,0,0)[0],maxvalue(a,0,0)[1],0,0) # maxvalue[0]和maxvalue[1]分别为最大值的行与列数
    if a[0,0] == 0:                      # 若交换后的最大值为零，说明无解
        test = 1
    for m in range(1,a.shape[0]):      # m为行，n为列，进行循环消元

        for i in range(m,a.shape[0]):    # m行以下的行进行运算
            ax = a[i, n] / a[n, n]
            for l in range(a.shape[1]):
                a[i,l]-=a[n,l] *ax            # 消元运算
        n = n+1                               # 列更新
        if m<a.shape[0]-1:
            if a[maxvalue(a,m,m)[0],maxvalue(a,m,m)[1]]==0:   # 若交换后的最大值为零，说明无解
                test = 1
            adjust(a,maxvalue(a,m,m)[0],maxvalue(a,m,m)[1],m,m) # 每循环一次寻找最大值，调整行与列
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
    if test == 1:    # 若test=1，说明无解,不返回任何值
        return
    else:
        return x  # 输出最终的解
print("解向量X为：\n",mainelement(A,Y))
