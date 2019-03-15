import numpy as np
import random

DATA_DIMENSION = 5
learningcollect = np.load("./splitdata/learningcollect.npy")
LEN_LEARNING = learningcollect.shape[0]
verifycollect = np.load("./splitdata/verifycollect.npy")
LEN_VERIFY = verifycollect.shape[0]
testcollect = np.load("./splitdata/testcollect.npy")
LEN_TEST = testcollect.shape[0]

def genLearningData(batch_size=10, predict=20, samples=50):
    x_train = np.empty((batch_size, samples*DATA_DIMENSION))
    y_train = np.empty((batch_size, predict))
    n = LEN_LEARNING - predict - samples
    for i in range(batch_size):
        begin = random.randint(0, n)
        x_train[i, :] = learningcollect[begin:begin + samples].reshape(-1,samples*DATA_DIMENSION)
        y_train[i, :] = learningcollect[begin + samples:begin + samples + predict].sum(axis=1)
    x_train = x_train.reshape((batch_size, samples*DATA_DIMENSION, 1))
    ytrain = y_train.reshape((batch_size, predict))
    return x_train/10, y_train

def genVerifyOrTestData(collect_type='test', predict=20, samples=50):
    if collect_type == 'test':
        collect_data = testcollect
    elif collect_type == 'verify':
        collect_data = testcollect
    else:
        raise Exception("collect type error!")

    n = LEN_VERIFY - predict - samples
    begin = random.randint(0, n)
    x = collect_data[begin:begin + samples].reshape(samples*DATA_DIMENSION, -1)
    y = collect_data[begin + samples:begin + samples + predict].sum(axis=1).reshape(1,-1)
    return x/10, y

if __name__ == "__main__":

    x,y = genVerifyOrTestData()
    print(x,y)