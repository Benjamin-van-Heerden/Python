#!/usr/bin/env python3

import os
import requests
import json

feedback_list = os.listdir("/data/feedback")
host_dir = "/data/feedback"
url = "http://35.223.35.238/feedback/"

for f in feedback_list:
  file = open(os.path.join(host_dir, f))
  lines = [l.strip() for l in file.readlines()]
  feedback = {"title":lines[0], "name":lines[1], "date":lines[2], "feedback":lines[3]}
  print(feedback)
  print(type(feedback))
  post = requests.post(url, json=feedback)
  print(post.status_code)
  
