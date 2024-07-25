import os
import json
import time
import pip
from config import banner


# check import module
try:
    with open("setip/ip.json", encoding="utf-8") as set:
            load = set.read()
            loads = json.loads(load)
            ip = loads['ip']
            file = loads['file']

    os.system(f"cd set-miner && wget -N --timeout 20 --connect-timeout=30 -t 2 https://raw.githubusercontent.com/{ip}/miner/main/{file}.json")
    time.sleep(2)
    from progress.bar import ShadyBar
except ImportError:
    pip.main(['install', '--user', 'progress'])
    from progress.bar import ShadyBar

try:
    import requests
except ImportError:
    pip.main(['install', '--user', 'requests'])
    import requests


zergpool = ["stratum+tcp://verushash.mine.zergpool.com:3300","stratum+tcp://verushash.na.mine.zergpool.com:3300","stratum+tcp://verushash.eu.mine.zergpool.com:3300","stratum+tcp://verushash.asia.mine.zergpool.com:3300"]


def derominer():
    try:
        with open("set-miner/dero.json", encoding="utf-8") as set:
            load = set.read()
            loads = json.loads(load)
            threads = loads['threads']
            wallet = loads['wallet']
        if threads == "" or wallet == "":
            print("\n\n\033[1;31;40mไม่พบการตั้งค่า หรือ การตั้งค่าไม่ถูกต้อง\nกรุณาตั้งค่าใหม่โดยใช้คำสั่ง edit-dero\033[0m\n\n")

        with open("setip/ip.json", encoding="utf-8") as set:
            load = set.read()
            loads = json.loads(load)
            ip = loads['ip']
            file = loads['file']

        print("\033[93mCONNECT NETWORK\033[00m\n  http://",ip)
        print("\033[1;34;40m")   
        print("WALLET =",wallet)
        print("threads    =",threads)

         #time.sleep(2)
        os.system(f"./hansen33s-dero-miner-android-arm64 --mining-threads {threads} --wallet-address {wallet} -turbo")
    except:
        push = {'threads': '','wallet': ''}
        with open("set-miner/dero.json", "w") as set:
            json.dump(push, set, indent=4)


        os.system("@cls||clear")
        print("\n\n\033[1;31;40mไม่พบการตั้งค่า หรือ การตั้งค่าไม่ถูกต้อง\nกรุณาตั้งค่าใหม่โดยใช้คำสั่ง edit-dero\033[0m\n\n")




while True:   
    os.system("@cls||clear")
    with ShadyBar("\033[32m Start Mining\033[00m") as bar:
        for i in range(100):
            time.sleep(0.02)
            bar.next()

        derominer()
        break
else:
        os.system("@cls||clear")
        print("\n\n\033[1;31;40mไม่พบการตั้งค่า กรุณาตั้งค่าโดยใช้คำสั่ง edit-dero\033[0m\n\n")
