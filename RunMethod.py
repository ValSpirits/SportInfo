import json
import time
import traceback

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
        jsonData = json.loads(data)
        list = jsonData['data']
        parse = BallDataParse()
        for value in list.values():
            print(value)
            sql = parse.getMatch(value)
            obs = parse.getObbs(value)
            db = DButil()
            db.run(sql)
            db.run(obs)
    except Exception as e:
        traceback.print_exc()
        time.sleep(60)


def timerFun(sched_Timer):
     while True:
         run_task()
         time.sleep(sched_Timer)


if __name__=='__main__':
    sched_Timer=900
    timerFun(sched_Timer)