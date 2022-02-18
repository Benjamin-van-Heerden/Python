#!/usr/bin/python3

import shutil
import sys

def check_disk_usage(disk, min_abs, min_percent):
    du = shutil.disk_usage(disk)
    percent_free = 100*du.free/du.total
    gigabytes_free = du.free/2**30
    print(f"DEBUG:\nPercent free: {percent_free} \nGigabytes free: {gigabytes_free}")
    if percent_free < min_percent or gigabytes_free < min_abs:
        return False
    return True

if not check_disk_usage("/", 2, 10):
    print("ERROR: Not enough disk space")
    sys.exit(1)

print("Everything ok")
sys.exit(0)