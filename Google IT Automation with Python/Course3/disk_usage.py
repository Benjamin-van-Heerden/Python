#!/usr/bin/python3

import shutil

def check_disk_usage(disk, min_abs, min_percent):
    du = shutil.disk_usage(disk)
    percent_free = 100*du.free/du.total
    gigabytes_free = du.free/2**30
    if percent_free < min_percent or gigabytes_free < min_abs:
        return False
    return True

if not check_disk_usage("/", 2*2**30, 10):
    print("ERROR: Not enough disk space")
    return 1

print("Everything ok")
return 0