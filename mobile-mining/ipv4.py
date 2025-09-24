import socket

def get_local_ipv4():
    hostname = socket.gethostname()
    # แทนที่ '127.0.0.1' หรือ 'localhost' ด้วยโฮสต์ที่ใช้งานจริงหากจำเป็น
    # หรือสามารถใช้ '0.0.0.0' เพื่อรับ IP ทั้งหมดที่เชื่อมต่อ
    try:
        # พยายามเชื่อมต่อกับโฮสต์ภายนอกเพื่อหา IP ของเครื่องตัวเอง
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80)) # ใช้ IP ของ Google DNS เป็นตัวอย่าง
        ip_address = s.getsockname()[0]
        s.close()
        return ip_address
    except socket.error:
        # กรณีที่ไม่สามารถเชื่อมต่อได้ เช่น ไม่มีอินเทอร์เน็ต
        return None

local_ipv4 = get_local_ipv4()
if local_ipv4:
    print(f"IPv4 ของเครื่อง: {local_ipv4}")
else:
    print("ไม่สามารถหา IPv4 ของเครื่องได้")