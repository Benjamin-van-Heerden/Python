#!/usr/bin/python3

import os
import shutil
import sys
import psutil
import socket

def check_reboot():
    return os.path.exists("/run/reboot-required")

def check_disk_full(disk, min_gb, min_percent):
    du = shutil.disk_usage(disk)
    percent_free = 100 * du.free / du.total
    gigabytes_free = du.free / 2**30
    if percent_free < min_percent or gigabytes_free < min_gb:
        return True
    return False

def check_cpu():
    cpu_percent = psutil.cpu_percent(2)
    return cpu_percent

def check_memory():
    mem_percent = psutil.virtual_memory()[2]
    return mem_percent

def check_battery_percent():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = str(battery.percent)
    plugged = "Plugged in" if plugged else "Not plugged in"
    return percent + "% | " + plugged

def check_network():
    try:
        socket.gethostbyname("www.google.com")
        return True
    except:
        return False


def main():
    print("Cpu usage: " + str(check_cpu()) + "%")
    print("Memory usage: " + str(check_memory()) + "%")
    print("Battery usage: " + check_battery_percent())
    print("Connected to network") if check_network() else print("Disconnected from network")

    if check_reboot():
        print("Pending reboot")
        sys.exit(1)
    if check_disk_full(disk="/", min_percent=10, min_gb=2):
        print("Disk Full")
        sys.exit(1)
    
    print("No reboot required and root partition disk usage okay!")
    sys.exit(0)

main()
    