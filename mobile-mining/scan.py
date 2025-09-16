import socket, json, os
import requests
def checknet():
    try:
        print("\033[92mตรวจสอบการเชื่อมต่อ INTERNET \033[0m")
        response = requests.get (url, stream=True)
        response.raise_for_status()
        print("\033[93m----------เชื่อมต่อสำเร็จแล้ว-----------\033[0m")
     
    except requests.exceptions.RequestException as e:
        print ("\033[95mไม่พบการเชื่อมต่อ ตรวจสอบอีกครั้งใน 10 วินาที\033[0m")
        time.sleep(10)
        checknet()
def scan_port(ips, port)
     try:
        sock = socket.create_connection((ips, port), timeout=0.1)
        print(f"พบ HTTP Server ที่ {ips}:{port}")
        ips = f"{ips}"
        IPS = ips
            #sock.close()
        push = {'ip': f"{IPS}"}
        with open("setip/ipserver.json", "w") as set:
             json.dump(push, set, indent=4)
            
    except (socket.timeout, ConnectionRefusedError):
        print(f"{network_ip_prefix}.{i}")
with open("setip/IPprefix.json", encoding="utf-8") as set:
         load = set.read()
         loads = json.loads(load)
         IPprefix = loads['IPprefix']
network_ip_prefix = f"{IPprefix}" # เปลี่ยนเป็น IP prefix ของเครือข่ายคุณ

for i in range(2, 256):
    ip_address = f"{network_ip_prefix}.{i}"
    scan_port(ip_address, 8080)  # ตรวจสอบพอร์ต 8080 (HTTP)
   