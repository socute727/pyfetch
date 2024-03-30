import psutil, os, platform, sys, distro, cpuinfo, timeit, os.path

get_processor_name = cpuinfo.get_cpu_info()['brand_raw']
cpuusg = psutil.cpu_percent(4)
memoryUse = psutil.virtual_memory()[3]/1000000000
memoryTotal = psutil.virtual_memory().total
memoryTotalr = memoryTotal / 1000000000
f = print
distr = distro.name()
system = platform.uname()
obj_Disk = psutil.disk_usage('/')
def get_uptime():
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
    return uptime_seconds
uptimemin = get_uptime() / 60
uptime = uptimemin / 60

#if distr == "Arch Linux":
#    f("⣿⣧⣿⣿⣿⣿⡟⢸⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣏⣿⣿ ",os.path.expanduser('~'))
#    f("⣿⢸⣿⡏⣿⣿⣹⢸⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿  --------------------------------------")
#    f("⣿⢼⡟⣤⣿⣧⣿⣸⣿⣿⣿⣿⣿⣿⣿⢻⣸⣿⢿⣿⣿⣿⣿⣿⣿⡇  OS:", platform.system())
#    f("⣿⢸⢧⣽⡼⣟⣛⣃⣿⠿⣿⣿⣿⣿⣿⢸⣏⣿⡘⣿⣿⣿⣿⡿⣿⢳  Distro:", distro.name())
#    f("⣿⡜⣸⡿⠷⠿⢿⣿⡼⡟⣼⡿⣿⣿⡿⡼⣿⣞⣆⡄⢭⢟⣻⡇⡿⣾  Kernel:", platform.release())
#    f("⡜⣷⢻⣤⣿⡒⠄⠄⠉⣺⣿⣿⣾⣽⣇⣥⡯⠿⠾⣞⣮⣃⢻⣧⣇⣿  Uptime:", round(uptime, 2), "H")
#    f("⣿⣮⡞⣷⣯⣗⣙⣿⣧⣣⣿⣿⣿⣿⣿⣿⣇⠟⡂⣀⣀⠉⡫⢸⣸⣿  CPU:", get_processor_name           )
#    f("⢿⣿⣿⣮⡻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣷⣬⣍⣎⣿⣿  CPU usage:", cpuusg, "%")
#    f("⣦⣭⣟⡿⣿⣿⣝⢿⣿⣿⣿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣜⣼⣿⣿  RAM:", round(memoryUse, 2),"/", round(memoryTotalr, 2),"GiB")
#    f("⠋⠄⠄⠄⠄⠉⠻⢷⣝⡿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⣼⣿⣿⣿  Disc used:", round(obj_Disk.used / 1000000000, 2), "GiB")
#    f("⠄⠄⠄⠄⠄⠄⠄⠄⢙⢿⣮⡻⣿⣷⣿⣿⠿⣟⡯⢡⣾⣠⣿⣿⣿⣿  Architecture:", platform.machine())
#    f("")
if distr == "Arch Linux":
    f("    _             _ ")
    f("   / \\   _ __ ___| |__     ",os.path.expanduser('~'))
    f("  / _ \\ | '__/ __| '_ \\     --------------------------------------")
    f(" / ___ \\| | | (__| | | |    OS:", distro.name())
    f("/_/   \\_\\_|  \\___|_| |_|    Kernel:", platform.release())
    f("| |   (_)_ __  _   ___  __  Uptime:", round(uptime, 2), "H")
    f("| |   | | '_ \\| | | \\ \\/ /  CPU:", get_processor_name           )
    f("| |___| | | | | |_| |>  <   CPU usage:", cpuusg, "%")
    f("|_____|_|_| |_|\\__,_/_/\\_\\  RAM:", round(memoryUse, 2),"/", round(memoryTotalr, 2),"GB")
    f("")

elif distr == "Fedora Linux":
    f(" _____        _                 ")
    f("|  ___|__  __| | ___  _ __ __ _  ",os.path.expanduser('~'))
    f("| |_ / _ \\/ _` |/ _ \\| '__/ _` |  --------------------------------------")
    f("|  _|  __/ (_| | (_) | | | (_| |  OS:", distro.name())
    f("|_|  \\___|\\__,_|\\___/|_|  \\__,_|  Kernel:", platform.release())
    f("| |   (_)_ __  _   ___  __        Uptime:", round(uptime, 2), "H")
    f("| |   | | '_ \\| | | \\ \\/ /        CPU:", get_processor_name)
    f("| |___| | | | | |_| |>  <         CPU usage:", cpuusg, "%")
    f("|_____|_|_| |_|\\__,_/_/\\_\\        RAM:", round(memoryUse, 2),"/", round(memoryTotalr, 2),"GB")
    f("")

elif distr == "Ubuntu":
    f("  ____                        _           _ ")
    f(" / ___|__ _ _ __   ___  _ __ (_) ___ __ _| |",os.path.expanduser('~'))
    f("| |   / _` | '_ \\ / _ \\| '_ \\| |/ __/ _` | | --------------------------------------")
    f("| |__| (_| | | | | (_) | | | | | (_| (_| | | OS:", distro.name())
    f(" \\____\\__,_|_| |_|\\___/|_| |_|_|\\___\\__,_|_| Kernel:", platform.release())
    f("| | | | |__  _   _ _ __ | |_ _   _           Uptime:", round(uptime, 2), "H")
    f("| | | | '_ \\| | | | '_ \\| __| | | |          CPU:", get_processor_name)
    f("| |_| | |_) | |_| | | | | |_| |_| |          CPU usage:", cpuusg, "%")
    f(" \\___/|_.__/ \\__,_|_| |_|\\__|\\__,_|          RAM:", round(memoryUse, 2),"/", round(memoryTotalr, 2),"GB")
    f("")

elif distr == "Debian GNU/Linux":
    f("  ____       _     _              ")               
    f(" |  _ \\  ___| |__ (_) __ _ _ __                  ",os.path.expanduser('~'))       
    f(" | | | |/ _ \\ '_ \\| |/ _` | '_ \\                  --------------------------------------")
    f(" | |_| |  __/ |_) | | (_| | | | |                 OS:", distro.name())
    f(" |____/ \\___|_.__/|_|\\__,_|_| |_|                 Kernel:", platform.release())
    f("  ____                ___     _                   Uptime:", round(uptime, 2), "H")          
    f(" / ___|_ __  _   _   / / |   (_)_ __  _   ___  __ CPU:", get_processor_name)
    f("| |  _| '_ \\| | | | / /| |   | | '_ \\| | | \\ \\/ / CPU usage:", cpuusg, "%")
    f("| |_| | | | | |_| |/ / | |___| | | | | |_| |>  <  RAM:", round(memoryUse, 2),"/", round(memoryTotalr, 2),"GB")
    f(" \\____|_| |_|\\__,_/_/  |_____|_|_| |_|\\__,_/_/\\_\\ ")
    f("")

else:
    f("    .--.       ",os.path.expanduser('~'))
    f("   |o_o |       --------------------------------------")
    f("   |:_/ |       OS:", distro.name())
    f("  //    \\\\      Kernel:", platform.release())
    f(" (|      |)     Uptime:", round(uptime, 2), "H")
    f(" /'\\_  _/'\\     CPU:", get_processor_name           )
    f(" \\___)=(___/    CPU usage:", cpuusg, "%")
    f("                RAM:", round(memoryUse, 2),"/", round(memoryTotalr, 2),"GB")
    f("")
