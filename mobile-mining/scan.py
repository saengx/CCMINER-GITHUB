import socket, json, os

def scan_port(ips, port):
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
        #print(f"{network_ip_prefix}.{i}")
network_ip_prefix = "172.16.10" # เปลี่ยนเป็น IP prefix ของเครือข่ายคุณ

for i in range(1, 255):
    ip_address = f"{network_ip_prefix}.{i}"
    scan_port(ip_address, 8080)  # ตรวจสอบพอร์ต 8080 (HTTP)
   