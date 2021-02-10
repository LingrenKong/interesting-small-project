# _*_coding:utf-8_*_
"""
Author: Lingren Kong
Created Time: 2020/10/30 12:50
探究利用感知机和线性规划解线性可分问题的特点
"""

from sklearn import datasets
import numpy as np
import scipy
import matplotlib.pyplot as plt

data, target = datasets.make_classification(n_samples=100, #样本量
                                            n_features=2,#特征数
                                            n_informative=2, #有效特征数
                                            n_redundant=0,#冗余特征数
                                            n_repeated=0,#重复特征数
                                            n_classes=2,#数据类别数
                                            n_clusters_per_class=1,#每类团簇个数
                                            class_sep=2.0,#类间距离
                                            random_state=1)#随机数种子
plt.scatter(data[:, 0], data[:, 1], c=target)
plt.show()

def getData(n,rand=1):
    data, target = datasets.make_classification(n_samples=n,  # 样本量
                                                n_features=2,  # 特征数
                                                n_informative=2,  # 有效特征数
                                                n_redundant=0,  # 冗余特征数
                                                n_repeated=0,  # 重复特征数
                                                n_classes=2,  # 数据类别数
                                                n_clusters_per_class=1,  # 每类团簇个数
                                                class_sep=2.0,  # 类间距离
                                                random_state=rand)  # 随机数种子
    return data,target
#LP solution


n = 2
data,target = getData(n)
y = target
y[y==0] = -1
A= data*y.reshape(n,1)
u = -np.ones(2)#cT*x
v = np.ones(n)
w = np.zeros(n)#x
result = scipy.optimize.linprog(u,-A,-v)#,method='simplex')
print(result)
plt.scatter(data[:, 0], data[:, 1], c=target)
plt.show()
