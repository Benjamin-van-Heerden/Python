import os
import subprocess

my_env = os.environ.copy()
print(my_env["PATH"])
my_env["PATH"] = os.pathsep.join(["/opt/adv_sub/", my_env["PATH"]])

result = subprocess.run(["adv_sub"], env=my_env)