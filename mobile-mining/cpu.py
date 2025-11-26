import os
print(f"\033[1;32;40mCPU Information\033[00m\n")
print("\033[96m")
os.system("lscpu|grep -i 'model name'")
os.system("lscpu|grep -i 'CPU max MHz'")
os.system("lscpu|grep -i 'On-line CPU(s) list'")
print("\033[00m")

print("**********************************************\n")	
print("\033[92m ccminer CPU High Hashrate  : > 4.0 < \033[00m")
print("Verushash v2.2 based on ccminer\n")
print("**********************************************\n")	
   
