import os, time, json
import socket
from urllib.request import urlopen
def autoconnect():
 try:
     with open("setip/ip.json", encoding="utf-8") as set:
             load = set.read()
             loads = json.loads(load)
             user = loads['user']
             file = loads['file']
             print("\n\033[92mตรวจสอบการเชื่อมต่อค่า config \033[0m\n")
             response = urlopen('http://raw.githubusercontent.com')
             #socket.create_connection(('www.google.com',80))
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