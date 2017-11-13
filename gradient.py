import matplotlib.pyplot as plt

#Training datasets
x = [1,2,3,4,5,6]
y = [13,14,20,21,25,30]


#设置允许误差值和初始化参数
epsilon = 1
alpha = 0.01
diff = [0,0]
max_itor = 20
error1 = 0
error0 =0
cnt = 0
m = len(x)
theta0 = 0.001
theta1 = 0.001


#循环训练
while 1:
    cnt=cnt+1
    diff = [0,0]
    for i in range(m):
        #计算成本函数的导数
        diff[0]+=theta0+ theta1 * x[i]-y[i]
        diff[1]+=(theta0+theta1*x[i]-y[i])*x[i]
    theta0=theta0-alpha/m*diff[0]
    theta1=theta1-alpha/m*diff[1]
    error1=0
    for i in range(m):
        error1+=(theta0+theta1*x[i]-y[i])**2
    if abs(error1-error0)< epsilon:
        break
    print('theta0 :%f,theta1 :%f,error:%f'%(theta0,theta1,error1))
    if cnt>200:
        print('cnt>200')
        break
print('theta0 :%f,theta1 :%f,error:%f'%(theta0,theta1,error1))

#把x的值输入到预测的曲线中，用数组获取最后的预测值
y1 = []
for i in x:
     h=theta0 + theta1 * i
     y1.append(h)
print(y1)
plt.plot(x,y,'bo')
plt.plot(x,y1,'g')
plt.show()











