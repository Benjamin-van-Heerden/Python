#!/usr/bin/python3

import subprocess
from multiprocessing import Pool
import os

def backup(tup):
  filepath = tup[0]
  dest = tup[1]
  subprocess.call(["rsync", "-arq", filepath, dest])

src = "/home/student-01-62acd246624b/data/prod/"
dest = "/home/student-01-62acd246624b/data/prod_backup/"
filepaths = []

for (root, dirs, files) in os.walk(src, topdown=True):
  for dir in dirs:
    filepaths.append(os.path.join(root, dir))

backup_filepaths = [f.replace(src, dest) for f in filepaths]

tups = list(zip(filepaths, backup_filepaths))

p = Pool(len(tups))
p.map(backup, tups)

