import os, time, json
import requests
def autochec(url, filename):
 try:
             print("\n\033[96mตรวจสอบการเชื่อมต่อกับ GITHUB\033[0m\n")
             url = "https://raw.githubusercontent.com/saengx/miner/main/begin-control.json"
             output_filename = "start"
             response = requests.get (url, stream=True)
             response.raise_for_status() 
     with open(filename, 'wb') as f:
         for chunk in response.iter_content(chunk_size=8192):
             f.write(chunk)
             print(f"\n\033[95mเชื่อมต่อสำเร็จแล้ว\033[0m\n

 except requests.exceptions.RequestException as e:
             print ('\n\033[95mไม่พบการเชื่อมต่อ ตรวจสอบอีกครั้งใน 10 วินาที
             time.sleep(1)
             os.system ("python3 check.py")
url_to_download = "https://raw.githubusercontent.com/saengx/miner/main/begin-control.json"
output_filename = "start"
autocheck(url_to_download, output_filename)
os.system ("chmod +x start && mv start ../../bin")
