# encoding:utf-8

'''分离学习集，验证集，测试集三组数据'''
import numpy as np

wholedata = np.load("../getdata/filename.npy")
wholedata = wholedata.reshape(-1, 5)
datalen = wholedata.shape[0]
n = round(datalen/2)
learningcollect = wholedata[0:n]
m = round(n/2)
verifycollect = wholedata[n:n+m]
testcollect = wholedata[n+m:]

np.save("./splitdata/learningcollect.npy",learningcollect)
np.save("./splitdata/verifycollect.npy",verifycollect)
np.save("./splitdata/testcollect.npy",testcollect)