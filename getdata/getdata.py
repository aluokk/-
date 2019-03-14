import pymongo
import numpy as np

mongo_uri = 'mongodb://localhost'
mongo_db = 'test'
collection_name = 'ssq_ac'

client = pymongo.MongoClient(mongo_uri)  # 登录mongo
db = client.test  # 指定数据库
collection = db.ssq_ac # 指定集合

try:
    # tmp_date = []
    # results = collection.find()
    results = collection.find().sort('cqssc_date', pymongo.ASCENDING)  # 排序
    data_array = np.array([])
    i=0
    for result in results:
        cur_cqssc_str = result['cqssc_str']
        cur_cqssc_str.reverse()
        i+=1
        print(i)
        for cur_number in cur_cqssc_str:
            tmp_str_array = np.array(cur_number.split('|'))
            tmp_num_array = tmp_str_array.astype(int)
            data_array = np.concatenate((data_array, tmp_num_array), axis=0)
    np.save("filename.npy",data_array)
    # b = np.load("filename.npy")
finally:
    client.close()