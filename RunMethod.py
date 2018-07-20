import json
import time

from BallDataParse import BallDataParse
from DButil import DButil
from JsonUtil import JsonUtil

def run_task():
    t = time.time()
    sjc = int(round(t * 1000))
    url = 'http://i.sporttery.cn/odds_calculator/get_odds?i_format=json&i_callback=getData&poolcode[]=hhad&poolcode[]=ttg&poolcode[]=crs&poolcode[]=hafu&poolcode[]=had&_=' + str(sjc)
    try:
        data = JsonUtil().http_get(url)
        data=data[8:-2]
        print(data)
        jsonData = json.loads(data)
        list = jsonData['data']
        parse = BallDataParse()
        for value in list.values():
            sql = parse.getMatch(value)
            obs = parse.getObbs(value)
            db = DButil()
            db.run(sql)
            db.run(obs)
    except Exception:
        time.sleep(60)


def timerFun(sched_Timer):
     while True:
         run_task()
         time.sleep(sched_Timer)


if __name__=='__main__':
    sched_Timer=900
    timerFun(sched_Timer)