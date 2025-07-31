import os, time, json
import requests
def autoconect(url, filename):
 try:
     with open("setip/ip.json", encoding="utf-8") as set:
             load = set.read()
             loads = json.loads(load)
             user = loads['user']        
             print("\n\033[96mตรวจสอบการเชื่อมต่อค่า config\033[0m\n")
             url = "https://raw.githubusercontent.com/{user}/miner/main/online.json"
             output_filename = "online.json"
             response = requests.get (url, stream=True)
             response.raise_for_status() 
     with open(filename, 'wb') as f:
         for chunk in response.iter_content(chunk_size=8192):
             f.write(chunk)
             print(f"\n\033[95mเชื่อมต่อสำเร็จแล้ว\033[0m\n")

 except requests.exceptions.RequestException as e:
             print ("\n\033[95mไม่พบการเชื่อมต่อ ตรวจสอบอีกครั้งใน 10 วินาที\033[0m\n")
             time.sleep(1)
             os.system ("python3 check.py")
url_to_download = "https://raw.githubusercontent.com/saengx/miner/main/begin-control.json"
output_filename = "setminer/online.json"
autocheck(url_to_download, output_filename)

import requests

def download_file(url, filename):
    """ดาวน์โหลดไฟล์จาก URL และบันทึกในชื่อที่กำหนด"""
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # ยกเลิกหากเกิดข้อผิดพลาดในการดาวน์โหลด

        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"ดาวน์โหลดไฟล์ '{filename}' สำเร็จแล้ว")

    except requests.exceptions.RequestException as e:
        print(f"เกิดข้อผิดพลาดในการดาวน์โหลด: {e}")

# ตัวอย่างการใช้งาน
url_to_download = "https://www.easygifanimator.net/images/samples/video-to-gif-sample.gif"
output_filename = "sample.gif"
download_file(url_to_download, output_filename)
