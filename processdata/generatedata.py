import numpy as np
import random
import os

module_path = os.path.dirname(__file__)
DATA_DIMENSION = 5
learningcollect = np.load(module_path+"/splitdata/learningcollect.npy")
LEN_LEARNING = learningcollect.shape[0]
verifycollect = np.load(module_path+"/splitdata/verifycollect.npy")
LEN_VERIFY = verifycollect.shape[0]
testcollect = np.load(module_path+"/splitdata/testcollect.npy")
LEN_TEST = testcollect.shape[0]

def genData(collect_type='learning', batch_size=1, predict=20, samples=50):
    if collect_type == 'test':
        collect_data = testcollect
        n = LEN_TEST - predict - samples
    elif collect_type == 'verify':
        collect_data = verifycollect
        n = LEN_VERIFY - predict - samples
    elif collect_type == 'learning':
        collect_data = learningcollect
        n = LEN_LEARNING - predict - samples
    else:
        raise Exception("collect type error!")
    if batch_size > n:
        raise Exception("batch_size exceeds max data length")
    x = np.empty((batch_size, samples*DATA_DIMENSION))
    y = np.empty((batch_size, predict))
    for i in range(batch_size):
        begin = random.randint(0, n)
        x[i, :] = collect_data[begin:begin + samples].reshape(-1,samples*DATA_DIMENSION)
        y[i, :] = collect_data[begin + samples:begin + samples + predict].sum(axis=1)
    x = x.reshape((batch_size, samples*DATA_DIMENSION, 1))
    y = y.reshape((batch_size, predict))
    return x/10, y

# def genVerifyOrTestData(collect_type='test', predict=20, samples=50):
#     if collect_type == 'test':
#         collect_data = testcollect
#     elif collect_type == 'verify':
#         collect_data = verifycollect
#     else:
#         raise Exception("collect type error!")
#
#     n = LEN_VERIFY - predict - samples
#     begin = random.randint(0, n)
#     x = collect_data[begin:begin + samples].reshape(samples*DATA_DIMENSION, -1)
#     y = collect_data[begin + samples:begin + samples + predict].sum(axis=1).reshape(1,-1)
#     return x/10, y

# if __name__ == "__main__":
#
#     x,y = genVerifyOrTestData()
#     print(x,y)