from numpy import *
import cv2
import matplotlib.pyplot as plt


def loaddata():
    dataMat = []
    labelMat=[]
    file =open("C:\\Users\\lenovo\\Desktop\\testSet-LR.txt")
    for line in file.readlines():
        lineArr = line.strip().split()
        dataMat.append([float(lineArr[0]),float(lineArr[1])])
        labelMat.append([int(lineArr[2])])
    return dataMat,labelMat


dataMat, labelMat = loaddata()
dataArr = array(dataMat)
n = shape(dataArr)[0]
xcord1 = []
ycord1 = []
xcord2 = []
ycord2 = []
for i in range(n):
    if (int(labelMat[i]) == 1):
        xcord1.append(dataArr[i, 1])
        ycord1.append(dataArr[i, 2])
    else:
        xcord2.append(dataArr[i, 1])
        ycord2.append(dataArr[i, 2])
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')
ax.scatter(xcord2, ycord2, s=30, c='green')

ax.plot(x, y)
plt.xlabel('X1');
plt.ylabel('X2')
plt.show()

