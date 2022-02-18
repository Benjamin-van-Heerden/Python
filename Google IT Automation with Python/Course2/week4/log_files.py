#!/usr/bin/python3

import sys
import re

pattern = r"\[(\d*)\]"

logfile = sys.argv[1]
usernames = {}
with open(logfile) as f:
    for line in f:
        if "CRON" not in line:
            continue
        else:
            match = re.search(pattern, line)
            if match is None:
                continue
            pid = match[1]
            usernames[pid] = usernames.get(pid, 0) + 1
    f.close()
print(usernames)