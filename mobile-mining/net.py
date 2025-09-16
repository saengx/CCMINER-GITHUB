import requests, time, os

def check_internet_connection(url='http://www.google.com/', timeout=5):
    """
    ตรวจสอบการเชื่อมต่ออินเทอร์เน็ต โดยลองเข้าถึง URL ที่กำหนด
    """
    try:
        print("\033[92mตรวจสอบการเชื่อมต่อ INTERNET \033[0m")
        requests.get(url, timeout=timeout)
        print("\033[93m----------เชื่อมต่อสำเร็จแล้ว-----------\033[0m")
        print("\033[94mเริ่มต้นสแกนหา HTTP server\033[0m")
        os.system("python3 scan.py")
    except requests.ConnectionError:
        print ("\033[95mไม่พบการเชื่อมต่อ ตรวจสอบอีกครั้งใน 10 วินาที\033[0m")
        time.sleep(10)
        os.system ("python3 net.py")

if __name__ == "__main__":
    check_internet_connection()