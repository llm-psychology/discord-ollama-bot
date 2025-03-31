import logging
import requests
import os
import time

from mod.environment_variables import init
file_path = "./bot.log"#若為相對路徑時，有可能會讓在其他資料夾的module無法執行(會寫undefined)

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(filename)s %(levelname)s %(message)s",
                    datefmt="%a %d %b %Y %H:%M:%S",
                    filename=file_path,
                    filemode="a")

ID,TOKEN,SERVERWEBHOOK,BOTWEBHOOK,MORNING = init()

class addlog:
    def __init__(self):
        struct_time = time.localtime(time.time()) # 轉成時間元組
        self.time_stamp = time.strftime("%Y-%m-%d %H:%M:%S", struct_time)

    def _webhook_(self,url,payload)->int:
        data = {"content": str(payload)}
        response = requests.post(url, json=data)
        return response.status_code

    def _debug_(self,url,msg):
        msg = str(msg)
        msg = self.time_stamp +  " : " + os.getlogin() + " / 🟢[DEBUG]" + msg + "\n"
        print(msg)
        logging.debug(msg)
        self._webhook_(url,msg)

    def _info_(self,url,msg):
        msg = str(msg)
        msg = self.time_stamp +  " : " + os.getlogin() + " / 🟡[INFO]" + msg + "\n"
        print(msg)
        logging.info(msg)
        self._webhook_(url,msg)

    def _warning_(self,url,msg):
        msg = str(msg)
        msg = self.time_stamp +  " : " + os.getlogin() + " / 🟠[WARNING]" + msg + "\n"
        print(msg)
        logging.warning(msg)
        self._webhook_(url,msg)

    def _error_(self,url,msg):
        msg = str(msg)
        msg = self.time_stamp +  " : " + os.getlogin() + " / 🔴[ERROR]" + msg + "\n"
        print(msg)
        logging.error(msg)
        self._webhook_(url,msg)

    class server:
        def debug(msg,url=SERVERWEBHOOK):
            addlog()._debug_(url=url,msg=msg)#需要將所有的addlog實例化 也就是addlog()
        def info(msg,url=SERVERWEBHOOK):
            addlog()._info_(url=url,msg=msg)
        def warning(msg,url=SERVERWEBHOOK):
            addlog()._warning_(url=url,msg=msg)
        def error(msg,url=SERVERWEBHOOK):
            addlog()._error_(url=url,msg=msg)

    class bot:
        def debug(msg,url=BOTWEBHOOK):
            addlog()._debug_(url=url,msg=msg)
        def info(msg,url=BOTWEBHOOK):
            addlog()._info_(url=url,msg=msg)
        def warning(msg,url=BOTWEBHOOK):
            addlog()._warning_(url=url,msg=msg)
        def error(msg,url=BOTWEBHOOK):
            addlog()._error_(url=url,msg=msg)

