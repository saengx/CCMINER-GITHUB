import os
import json
import time
import pip
import requests
from config import banner


# check import module
try:
    with open("setip/ip.json", encoding="utf-8") as set:
            load = set.read()
            loads = json.loads(load)
            user = loads['user']
            file = loads['file']
    with open("setip/set-miner.json", encoding="utf-8") as set:
            load = set.read()
            loads = json.loads(load)
            cpupriority = loads['cpu-priority']
            apiallow = loads['api-allow']
            apibind = loads['api-bind']
    #autoconnect()
    #os.system(f"cd set-miner && wget -N --timeout 20 --connect-timeout=30 -t 2 --no-check-certificate https://raw.githubusercontent.com/{user}/miner/main/{file}.json")
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
    
    
zergpool = ["stratum+tcp://verushash.mine.zergpool.com:3300","stratum+tcp://verushash.na.mine.zergpool.com:3300","stratum+tcp://verushash.eu.mine.zergpool.com:3300","stratum+tcp://verushash.asia.mine.zergpool.com:3300"]
    
    
def runOffline():
    banner()
    try:
        with open("setip/ip.json", encoding="utf-8") as set:
            load = set.read()
            loads = json.loads(load)
            user = loads['user']
            file = loads['file']
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
            #print("\n\n\033[1;31;40mไม่พบการตั้งค่า หรือ การตั้งค่าไม่ถูกต้อง\nกรุณาตั้งค่าใหม่โดยใช้คำสั่ง edit-miner\033[0m\n\n")

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
        print("WALLET =",wallet)
        print("NAME   =",name)
        print("POOL   =",pool)
        print("CPU    =",cpu)
        if pool in zergpool:

           print("PASS   =",password +",id="+name)
           print("\033[00m\n")
           
           os.system(f"python3 cpu.py")
           #time.sleep(2)
           #os.system(f"cd ccminer && ./ccminer -a verus -o {pool} -u {wallet}.{name} -p {password},ID={name} -t {cpu} --cpu-priority {cpupriority} --api-allow={apiallow} --api-bind={apibind}")
           os.system(f"cd ccminer && ./ccminer -a verus -o {pool} -u {wallet}.{name} -p {password},ID={name} -t {cpu} --cpu-priority {cpupriority} --api-allow={apiallow} --api-bind={apibind}")
       
        else:
        	
         print("PASS   =",password)
         print("\033[00m\n")
         
         os.system(f"python3 cpu.py")
         #time.sleep(2)
         #os.system(f"cd ccminer && ./ccminer -a verus -o {pool} -u {wallet}.{name} -p {password} -t {cpu}")
         os.system(f"cd ccminer && ./ccminer -a verus -o {pool} -u {wallet}.{name} -p {password} -t {cpu} --cpu-priority {cpupriority} --api-allow={apiallow} --api-bind={apibind}")
    except:
        push = {'pool': '','wallet': '','pass': ''}
        with open("set-miner/{'file'}.json", "w") as set:
            json.dump(push, set, indent=4)
        push = {'name': '','cpu': ''}
        with open("set-miner/offline.json", "w") as set:
            json.dump(push, set, indent=4)
        push = {'ip': '','file': ''}
        with open("setip/ip.json", "w") as set:
            json.dump(push, set, indent=4)
        
        
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

    