#!/usr/bin/python3

import os
import shutil
import sys
import psutil

def check_reboot():
    return os.path.exists("/run/reboot-required")

def check_disk_full(disk, min_gb, min_percent):
    du = shutil.disk_usage(disk)
    percent_free = 100 * du.free / du.total
    gigabytes_free = du.free / 2**30
    if percent_free < min_percent or gigabytes_free < min_gb:
        return True
    return False

def check_battery_percent():
    battery = psutil.sensors_battery()
    plugged = psutil.power_plugged()
    percent = battery.percent
    plugged = "Plugged in" if plugged else "Not plugged in"
    return percent + "% | " + plugged


def main():
    if check_reboot():
        print("Pending reboot")
        sys.exit(1)
    if check_disk_full(disk="/", min_percent=10, min_gb=2):
        print("Disk Full")
        sys.exit(1)
    
    print("Everything okay!")
    sys.exit(0)

main()
    