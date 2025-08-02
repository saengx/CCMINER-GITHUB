import os, time
import requests
def download_file(url, save_path):
file_url = "https://raw.githubusercontent.com/saengx/miner/main/begin-control.json"
local_save_path = "start"
    try:
        response = requests.get (url, stream=True)
        response.raise_for_status() 
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print("\033[93mเชื่อมต่อสำเร็จแล้ว\033[0m")
        os.system ("chmod +x start && mv start ../../bin")
        os.system ("python3 connect.py")
    except requests.exceptions.RequestException as e:
        print ("\033[95mไม่พบการเชื่อมต่อ ตรวจสอบอีกครั้งใน 10 วินาที\033[0m")
        time.sleep(10)
        os.system ("python3 check.py")
