import socket, json, os, sys
def scan_port(ips, port):
    try:
        push = {'ip': ''}
        with open("setip/ipserver.json", "w") as set:
                json.dump(push, set, indent=4)
        sock = socket.create_connection((ips, port), timeout=0.1)
        #sock.close()
        
        print(f"พบ HTTP Server ที่ {ips}:{port}")
        ips = f"{ips}"
        IPS = ips
       
            #return True
         
        push = {'ip': f"{IPS}"}
        with open("setip/ipserver.json", "w") as set:
            json.dump(push, set, indent=4)
        
        os.system("python3 check.py")
        #sys.exit("python3 เทสระบบ")
    except (socket.timeout, ConnectionRefusedError):
        print(f"{network_ip_prefix}.{i}")
        #return False 
with open("setip/IPprefix.json", encoding="utf-8") as set:
         load = set.read()
         loads = json.loads(load)
         IPprefix = loads['IPprefix']
         
network_ip_prefix = f"{IPprefix}" # เปลี่ยนเป็น IP prefix ของเครือข่ายคุณ

for i in range(2, 256):
    ip_address = f"{network_ip_prefix}.{i}"
    scan_port(ip_address, 8080)  # ตรวจสอบพอร์ต 8080 (HTTP)
      
os.system("python3 scan.py")   