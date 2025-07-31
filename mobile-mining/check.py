import os, time, json
import requests
def autocheck():
 try:
     with open("setip/ip.json", encoding="utf-8") as set:
             load = set.read()
             loads = json.loads(load)
             user = loads['user']
             print("\n\033[96mตรวจสอบการเชื่อมต่อกับ GITHUB\033[0m\n")
             url = "https://raw.githubusercontent.com/{user}/miner/main/begin-control.json"
             output_filename = "start"
             response = requests.get (url, stream=True)
             response.raise_for_status()  # ยกเลิกหากเกิดข้อผิดพลาดในการดาวน์โหลด
 except requests.exceptions.RequestException as e:
        print ('\n\033[95mไม่พบการเชื่อมต่อ ตรวจสอบอีกครั้งใน 15 วินาที\033[0m\n')
        time.sleep(15)
        os.system ("python3 check.py")      
 while True:
      autocheck()
      os.system ("start")
      break    
             
             
