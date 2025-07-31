import os, time, json
import requests
def autocheck(url, filename):
 try:
     with open("setip/ip.json", encoding="utf-8")>
             load = set.read()
             loads = json.loads(load)
             user = loads['user']
             print("\n\033[96mตรวจสอบการเชื่อมต่อกับ >
             url = "https://raw.githubusercontent>
             output_filename = "start"
             response = requests.get (url, stream>
             response.raise_for_status()  # ยกเลิก>
     with open(filename, 'wb') as f:
         for chunk in response.iter_content(chunk>
             f.write(chunk)
             print(f"\n\033[95mเชื่อมต่อสำเร็จแล้ว\033>

 except requests.exceptions.RequestException as e:
             print ('\n\033[95mไม่พบการเชื่อมต่อ ตรวจ>
             time.sleep(15)
             
             
