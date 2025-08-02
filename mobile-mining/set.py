import os, time, json
from config import bannerup
from multiprocessing import cpu_count



def setminer():

   bannerup()
   try:
       print("0-5 \033[93mปกติ 3\033[00m")
       cpupriority = input("[cpu-priority]: ")
       print("\033[35m-----------------------------------------\033[0m")

       print(f"ค่า full-acess ip \033[93mเช่น 192.168.1.0/24\033[00m")
       apiallow = input("[api-allow]: ")
       print("\033[35m-----------------------------------------\033[0m")

       print(f"ค่า bind ip:port \033[93mเช่น 0.0.0.0:4068\033[00m")
       apibind = input("[api-bind]: ")
       print("\033[35m-----------------------------------------\033[0m")
   except:
            os.system("@cls||clear")
            print("เกิดข้อผิดพลาดโปรดตั้งค่าใหม่!")
            time.sleep(3)
            os.system("set")
   push = {
          'cpu-priority': cpupriority,
          'api-allow': apiallow,
          'api-bind' : apibind
          }
   with open("setip/set-cpu.json", "w") as set:
     json.dump(push, set, indent=4)

while True:
  bannerup()
  setminer()
  os.system("run-miner")     
  break
