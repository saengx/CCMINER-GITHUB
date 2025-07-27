import psutil
import os
import cpuinfo

cpu_info_data = cpuinfo.get_cpu_info()
cpu_model_name = cpu_info_data.get('model name')
cpu_brand_name = cpu_info_data.get('brand_raw')

print(f"CPU : {cpu_brand_name}")
cpu_freq = psutil.cpu_freq()
if cpu_freq:
    print(f"CPU Frequency: {cpu_freq.current:.2f} MHz")
    print(f"Min CPU Frequency: {cpu_freq.min:.2f} MHz")
    print(f"Max CPU Frequency: {cpu_freq.max:.2f} MHz")
else:
    print("Could not retrieve CPU frequency information.")