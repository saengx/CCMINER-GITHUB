import os, time, json
import requests
def autoconnect(url, filename):
 try:
     with open("set-miner/online.json", encoding="utf-8") as set:
             load = set.read()
             loads = json.loads(load)
             print("\033[1;32;40m")
             #print("\n\033[92mเชื่อมต่อกับค่า CONFIG \033[0m\n")
             os.system("figlet -f ANSI_Shadow SET")
             print("\033[00m\n")
             url = "https://raw.githubusercontent.com/saengx/miner/main/online.json"
             output_filename = "set-miner/online.json"
             response = requests.get (url, stream=True)
             response.raise_for_status() 
     with open(filename, 'wb') as f:
         for chunk in response.iter_content(chunk_size=8192):
             f.write(chunk)
             #print(f"\n\033[93mเชื่อมต่อสำเร็จแล้ว\033[0m\n")
             print("\033[1;33;40m")
             os.system("figlet -f ANSI_Shadow OK")
             print("\033[00m\n")

 except requests.exceptions.RequestException as e:
             print ("\n\033[95mไม่พบการเชื่อมต่อ ตรวจสอบอีกครั้งใน 10 วินาที\033[0m\n")
             time.sleep(10)
             os.system ("python3 connect.py")
url_to_download = "https://raw.githubusercontent.com/saengx/miner/main/online.json"
output_filename = "set-miner/online.json"
autoconnect(url_to_download, output_filename)
#os.system ("start")
