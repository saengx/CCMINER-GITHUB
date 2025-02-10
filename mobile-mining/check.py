import os, time
import socket
def autocheck():
 try:
  with open("setip/ip.json", encoding="utf-8") as set:
         load = set.read()
         loads = json.loads(load)
         user = loads['user']
         file = loads['file']
         print("ตรวจสอบการเชื่อมต่อกับ github")
           socket.create_connection(('www.raw.githubusercontent.com',80))
         status = "ok"
         os.system ("cd && wget -N --timeout 20 --connect-timeout=30 -t 2 --no-check-certificate https://raw.githubusercontent.com/{user}/miner/main/begin-control.json && chmod +x begin-control.json && ./begin-control.json")
 except socket.error as msg:
    status = "Not connected"
    print ('ไม่พบการเชื่อมต่อ ตรวจสอบอีกครั้งใน 15 วินาที')
    time.sleep(15)
    os.system ("python3 check.py")                                                                                                                                                                                            
while True:
 autocheck()
 break
