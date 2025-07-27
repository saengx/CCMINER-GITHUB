import psutil
import os
import cpuinfo
import platform

cpu_info = platform.processor()
cpu_count = psutil.cpu_count(logical=False)
logical_cpu_count = psutil.cpu_count(logical=True)
system_info = platform.uname()

print(f"\033[1;32;40mCPU Information\033[00m\n")
print(f"Processor: {cpu_info}")
print(f"Threads: {cpu_count}")
print("System Information:")
print(f"System: {system_info.system}")
print(f"Node Name: {system_info.node}")
print(f"Processor: {system_info.processor}")