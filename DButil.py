import configparser

import pymysql as pymysql


class DButil:
    @classmethod
    def __initData(self):
        config = configparser.ConfigParser()
        config.read("config.ini")
        db_host = config.get("db", "host")
        db_port = int(config.get("db", "port"))
        db_user = config.get("db", "user")
        db_pass = config.get("db", "password")
        db_db = config.get("db", "db")
        db_charset = config.get("db", "charset")
        db_args={"host":db_host,"port":db_port,"user":db_user,"passwd":db_pass,"db":db_db,"charset":db_charset};
        return db_args;
        # db = pymysql.connect(host=db_host, port=db_port, user=db_user, passwd=db_pass, db=db_db,
        #                      charset=db_charset)
        # return db

    @classmethod
    def run(self,sql):
         try:
             db_args=self.__initData()
             db=pymysql.connect(**db_args)
             db_cursor = db.cursor()
             # 执行sql语句
             db_cursor.execute(sql)
             print(sql)
             # 提交到数据库执行
             db.commit()
         except Exception:  # 方法一：捕获所有异常
             # 如果发生异常，则回滚
             print("发生异常", Exception)
             db.rollback()
         finally:
             # 最终关闭数据库连接
             db.close()
