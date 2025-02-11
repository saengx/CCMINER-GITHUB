import os, time, json
import socket
def autoconnect():
 try:
     with open("setip/ip.json", encoding="utf-8") as set:
             load = set.read()
             loads = json.loads(load)
             user = loads['user']
             file = loads['file']
             print("\n\033[96mตรวจสอบการเชื่อมต่อกับ GITHUB\033[0m\n")
             socket.create_connection(('www.raw.githubusercontent.com',80))
             status = "ok"
             #os.system(f"cd set-miner && wget -N --timeout 20 --connect-timeout=30 -t 2 --no-check-certificate https://raw.githubusercontent.com/{user}/miner/main/{file}.json")
 except socket.error as msg:
    status = "Not connected"
    print ('\n\033[95mไม่พบการเชื่อมต่อ ตรวจสอบอีกครั้งใน 15 วินาที\033[0m\n')
    time.sleep(15)
    os.system ("python3 connect.py")                                                                                                                                                                                            
while True:
      autoconnect()
      break
