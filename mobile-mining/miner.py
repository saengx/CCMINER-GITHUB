import os
import json
import time
import pip
import requests
from config import banner
from ipv4 import get_local_ipv4

try:
    with open("setip/ip.json", encoding="utf-8") as set:
        load = set.read()
        loads = json.loads(load)
        user = loads['user']
        file = loads['file']
    if user == "":
       user = "saengx"
    if file == "":
       file = "online"
    with open("setip/set-cpu.json", encoding="utf-8") as set:
        load = set.read()
        loads = json.loads(load)
        cpupriority = loads['cpu-priority']
    if cpupriority == "":
       cpupriority = "1"
    os.system(f"python3 connect.py")

    os.system(f"cd set-miner && mv {file}.json online.json")
    time.sleep(2)
    from progress.bar import ChargingBar
except ImportError:
    pip.main(['install', '--user', 'progress'])
    from progress.bar import ChargingBar

try:
    import requests
except ImportError:
    pip3.main(['install', '--user', 'requests'])
    import requests

localIPv4 = get_local_ipv4()    

def runOffline():
    banner()
    get_local_ipv4()
    try:
        with open("setip/ip.json", encoding="utf-8") as set:
            load = set.read()
            loads = json.loads(load)
            user = loads['user']
            file = loads['file']
        if user == "":
           user = "saengx"
        if file == "":
           file = "online"
        with open("set-miner/online.json", encoding="utf-8") as set:
            load = set.read()
            loads = json.loads(load)
            pool = loads['pool']
            wallet = loads['wallet']
            password = loads['pass']
        if pool == "":
           pool = "stratum+tcp://sg.vipor.net:5040"
        if wallet == "":
           wallet == "RBtTBgmjNCucDyoTBPhNVhMpzzbj8A1kCd"
        if password == "":
           password = "x"
        with open("set-miner/offline.json", encoding="utf-8") as set:
            load = set.read()
            loads = json.loads(load)
            name = loads['name']
            cpu = loads['cpu']
        if name == "":
           name = "Z1"
        if cpu == "":
           cpu = "8"

        print("\033[93mCONNECT USER\033[00m\n")
        print("USER =",user)
        print("file =",file)
        print("\033[1;34;40m")
        print("POOL   =",pool)
        print("WALLET =",wallet)
        print("PASS   =",password)
        print("NAME   =",name)
        print("CPU    =",cpu)
        print("\033[00m\n")

        os.system(f"python3 cpu.py")
        os.system(f"cd ccminer && ./ccminer -a verus -o {pool} -u {wallet}.{name} -p {password} -t {cpu} --cpu-priority {cpupriority} --api-allow={localIPv4}/16 --api-bind=0.0.0.0:4068")
    except:
        #push = {'pool': '','wallet': '','pass': ''}
        #with open("set-miner/online.json", "w") as set:
            #json.dump(push, set, indent=4)
        #push = {'name': '','cpu': ''}
        #with open("set-miner/offline.json", "w") as set:
            #json.dump(push, set, indent=4)
        #push = {'ip': '','file': ''}
        #with open("setip/ip.json", "w") as set:
            #json.dump(push, set, indent=4)
        #push = {'cpu-priority': ''}
        #with open("setip/set-cpu.json", "w") as set:
            #json.dump(push, set, indent=4)

        os.system("@cls||clear")
        print("\n\n\033[1;31;40mการตั้งค่าไม่ถูกต้อง\nกรุณาตั้งค่าใหม่โดยใช้คำสั่ง edit-miner\033[0m\n\n")




while True:   
    os.system("@cls||clear")
    with ChargingBar("\033[35m Starting Your Miner\033[00m") as bar:
        for i in range(100):
            time.sleep(0.02)
            bar.next()

        runOffline()
        break
else:
        os.system("@cls||clear")
        print("\n\n\033[1;31;40mไม่พบการตั้งค่า กรุณาตั้งค่าโดยใช้คำสั่ง edit-miner\033[0m\n\n")