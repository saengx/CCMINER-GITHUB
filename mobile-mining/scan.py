import socket

def scan_port(ip, port):
    try:
        sock = socket.create_connection((ip, port), timeout=1)
        print(f"พบ HTTP Server ที่ {ip}:{port}")
        sock.close()
        return True
    except (socket.timeout, ConnectionRefusedError):
        return False

# ตัวอย่างการสแกน IP ในเครือข่าย (ต้องระบุช่วง IP ที่ถูกต้อง)
network_ip_prefix = "172.16.10." # เปลี่ยนเป็น IP prefix ของเครือข่ายคุณ

for i in range(1, 255):
    ip_address = f"{network_ip_prefix}{i}"
    scan_port(ip_address, 8080)  # ตรวจสอบพอร์ต 80 (HTTP)
   