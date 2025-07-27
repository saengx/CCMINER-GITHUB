import psutil
import os
import cpuinfo
import platform

cpu_info = platform.processor()
cpu_count = psutil.cpu_count(logical=False)
logical_cpu_count = psutil.cpu_count(logical=True)
system_info = platform.uname()

print("\033[1;32;40mCPU Information")
print(f"Processor: {cpu_info}")
print(f"Physical Cores: {cpu_count}")
print(f"Logical Cores: {logical_cpu_count}")
print("System Information:")
print(f"System: {system_info.system}")
print(f"Node Name: {system_info.node}")
print(f"Release: {system_info.release}")
print(f"Version: {system_info.version}")
print(f"Machine: {system_info.machine}")
print(f"Processor: {system_info.processor}")