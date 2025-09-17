import os, time, json




def banner():
        os.system("clear")
        print("\033[1;34;40m")
        os.system("figlet -f big VERUS")
        os.system("figlet -f digital http-server")
        print("\033[00m\n")
        print("\033[95mEdit by PICHET SAENGTEWAN\033[0m")
        print("\033[36m\033[0m")

def setip():


    banner()
    try:
        print("ใส่ค่า IPprefix เฉพาะ 3 ชุดแรก ตัวอย่าง \033[93m192.168.1\033[00m")
        IPprefix = input("   IPprefix   ")
        print("\033[35m-----------------------------------------\033[0m")


        if IPprefix == "":
            raise Exception()
    except:
        os.system("@cls||clear")
        print("\033[32mเกิดข้อผิดพลาดโปรดตั้งค่าใหม่\033[00m")
        time.sleep(3)
        os.system("python3 ip.py")

    push = {
           'IPprefix': IPprefix
           }
    with open("setip/IPprefix.json", "w") as set:
        json.dump(push, set, indent=4)


while True:
    banner()
    setip()
    with open("setip/IPprefix.json",encoding="utf-8") as set:
        load = set.read()
        loads = json.loads(load)
        IPprefix = loads['IPprefix']

        print("\033[36m")
        print("IPprefix ที่บันทึก")
        print("IPprefix  =",IPprefix)
        print("\033[0m\n")
        print("\033[31mโปรดตรวจสอบการตั้งค่า ถ้าถูกต้อง ให้ใช้คำสั่ง  run-miner  เพื่อเปิดขุด\033[0m")
        os.system("python3 net.py")
    break
