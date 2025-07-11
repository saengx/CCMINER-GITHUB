import os, time, json
import socket
from urllib.request import urlopen
def autocheck():
 try:
     with open("setip/ip.json", encoding="utf-8") as set:
             load = set.read()
             loads = json.loads(load)
             user = loads['user']
             print("\n\033[96mตรวจสอบการเชื่อมต่อกับ GITHUB\033[0m\n")
             response = urlopen('http://raw.githubusercontent.com')
       #socket.create_connection(('www.raw.githubusercontent.com',80))
             status = "ok"
             os.system (f"cd && wget -N --timeout 20 --connect-timeout=30 -t 2 --no-check-certificate https://raw.githubusercontent.com/{user}/miner/main/begin-control.json && chmod +x begin-control.json && ./begin-control.json && run-miner")
 except socket.error as msg:
    status = "Not connected"
    print ('\n\033[95mไม่พบการเชื่อมต่อ ตรวจสอบอีกครั้งใน 15 วินาที\033[0m\n')
    time.sleep(15)
    os.system ("python3 check.py")
    #os.system ("run-miner")                                                                                                                                                                                          
while True:
      autocheck()
      break
else:
      #os.system("@cls||clear")
      print ('\n\033[95mการเชื่อมต่อถูกขัดจังหวะ ตรวจสอบอีกครั้งใน 15 วินาที\033[0m\n')
      time.sleep(15)
      os.system ("auto")