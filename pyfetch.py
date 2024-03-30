import psutil, os, platform, sys, distro, cpuinfo, timeit, os.path

get_processor_name = cpuinfo.get_cpu_info()['brand_raw']
memoryUse = psutil.virtual_memory()[3]/1000000000
memoryTotal = psutil.virtual_memory().total
memoryTotalr = memoryTotal / 1000000000
def get_uptime():
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
    return uptime_seconds

uptimemin = get_uptime() / 60
uptime = uptimemin / 60

print("    .--.       ",os.path.expanduser('~'))
print("   |o_o |       --------------------------------------")
print("   |:_/ |       OS:", distro.name())
print("  //   \ \      Kernel:", platform.release())
print(" (|      |)     Uptime:", round(uptime, 2), "H")
print(" /'\_  _/'\     CPU:", get_processor_name           )
print(" \___)=(___/    RAM:", round(memoryUse, 2),"/", round(memoryTotalr, 2),"GB")
