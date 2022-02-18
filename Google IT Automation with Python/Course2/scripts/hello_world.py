#!/usr/bin/python3 
import modules.areas as areas
import modules.practical_example as pe

print("hello")
print(areas.circle(1))

print("CPU < 0.75:", end=' ')
print(pe.check_cpu_usage())

print("Disk > 0.2:", end=' ')
print(pe.check_disk_usage("/"))

