#!/usr/bin/python3

import subprocess

print(subprocess.run(["date"]))
subprocess.run(["sleep", "0.5"])
print("done sleeping")
print(subprocess.run("ls"))

result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print(result.returncode)
print(result.stdout)
print(result.stdout.decode().split())

result = subprocess.run(["rm", "dne"], capture_output=True)
print(result.stdout)
print(result.stderr)

subprocess.run(["echo BvH970730 | sudo -S chmod +x hello.py"])

subprocess.run(["./hello.py"])
