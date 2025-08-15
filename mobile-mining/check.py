import os, time, json
import requests
def download_file(url, save_path):
    try:
        print("\033[92mกำลังเชื่อมต่อกับ HTTP-SERVER \033[0m")
        print("\033[1;32;40m")
        #os.system("figlet -f digital connect-to-github")
        print("\033[00m\n")
        response = requests.get (url, stream=True)
        response.raise_for_status()

        
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        
        print("\033[93m----------เชื่อมต่อสำเร็จแล้ว-----------\033[0m")
        os.system ("chmod +x start.json && mv start.json start && mv start ../../bin")
        os.system ("start")
    except requests.exceptions.RequestException as e:
        print ("\033[95mไม่พบการเชื่อมต่อ ตรวจสอบอีกครั้งใน 10 วินาที\033[0m")
        time.sleep(10)
        os.system ("python3 check.py")
with open("setip/ipserver.json", encoding="utf-8") as set:
             load = set.read()
             loads = json.loads(load)
             ip = loads['ip']
             IP = f"{ip}"
file_url = f"http://{IP}:8080/start"
#file_url = "https://raw.githubusercontent.com/saengx/miner/main/start"
local_save_path = "start.json"
download_file(file_url,local_save_path) 
