import os, time, json
from config import banneredit
from multiprocessing import cpu_count

cpu_thread = cpu_count()


def OffMiner():

   banneredit()
   try:
       print("ตัวอย่าง: \033[93mค่าที่ใส่ได้คือ 0 ถึง {cpu_thread}\033[00m")
       threads = input("threads: ")
       print("\033[35m-----------------------------------------\033[0m")

       print("ตัวอย่าง: \033[93mRKh6cinBtWFspyBfK6Xsu8JKJsFyfYmUCr\033[00m")
       wallet = input("wallet: ")
       print("\033[35m-----------------------------------------\033[0m")

       if threads == "" or wallet == "":
          raise Exception()
   except:
            os.system("@cls||clear")
            print("เกิดข้อผิดพลาดโปรดตั้งค่าใหม่!")
            time.sleep(3)
            os.system("edit-dero")   
   push = {
         'threads': threads,
         'wallet': wallet,
          }
   with open("set-miner/dero.json", "w") as set:
        json.dump(push, set, indent=4)

while True:
  banneredit()
  OffMiner()
  os.system("run-dero")     
  break