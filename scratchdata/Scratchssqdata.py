import requests
import time
import pymongo
import logging

logging.basicConfig(filename='logger.log', level=logging.INFO)


mongo_uri = 'mongodb://localhost'
mongo_db = 'test'
collection_name = 'ssq_ac'

client = pymongo.MongoClient(mongo_uri)
db = client[mongo_db]

item = {'cqssc_date':0, 'cqssc_number':0, 'cqssc_str':0}
cookies = {
    'AUM': 'dgX2hdjD5PhTl6GmmdiJVWuXjN5nt-yqlWtWpTno5j7lw',
    'VUID': '41CC80EDE8174C7BB3FC8C6F691CA4B1',
    'Hm_lvt_49024937a7f937de669432245102dac6': '1552098935',
    'UM_distinctid': '1684c72beab64-0b7e7f5549f8328-73216752-100200-1684c72beac103',
    'CNZZDATA3538029': 'cnzz_eid%3D2000804251-1547466073-%26ntime%3D1552096890',
    'routekjgg': 'bce7765295b50ac71f342dfa7d99c0dd',
    'JSESSIONID': '516375110B4EA83F154181D87066F6A5.c73',
    'NAGENTID': '46965',
    'zqPopupOpenStatus': 'opened',
    'Hm_lpvt_49024937a7f937de669432245102dac6': '1552099063',
}
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Referer': 'https://kaijiang.aicai.com/cqssc/',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
}

time_val = 24*3600
begin_time = 1212741426.0
cur_time = begin_time
cur_date = time.strftime('%Y-%m-%d',
                        time.localtime(cur_time))
end_date = '2019-03-11'
end_time = time.mktime(time.strptime(end_date,'%Y-%m-%d'))
s = requests.Session()

while cur_time < end_time:
# for cur_date in ['2008-10-07','2008-10-08','2008-11-13',
#                  '2011-04-25','2018-08-18','2018-08-19']:
    print((cur_time - begin_time) * 100 / (end_time - begin_time),"%")
    cur_time += time_val
    cur_date = time.strftime('%Y-%m-%d',
                             time.localtime(cur_time))
    data = {
      'gameIndex': '301',
      'searchDate': cur_date,
      'gameFrom': ''
    }
    res_str = ''
    try:
        response = s.post('https://kaijiang.aicai.com/open/kcResultByDate.do',
                             headers=headers, cookies=cookies, data=data, timeout=15)
        res_str = response.json()["resultHtml"]
    except Exception as err:
        logging.error(cur_date)
    else:
        logging.info(cur_date)
    if not res_str == '':
        res_list = res_str.split("</td>")
        n = round(len(res_list)/3)
        item['cqssc_number'] = [res_list[i*3].split('>')[-1][9:]
                              for i in range(n)]
        item['cqssc_date'] = [res_list[1+i*3].split('>')[-1]
                                for i in range(n)]
        item['cqssc_str'] = [res_list[2 + i * 3].split('>')[-1]
                              for i in range(n)]
    try:
        db[collection_name].insert(dict(item))
    # time.sleep(random.randint(3, 12))
    except Exception as err:
        logging.info(err)  # 抓取失败时输出日志，补充抓取失败的数据
client.close()
s.close()