#!/usr/bin/env python3

# Author: Hongjian Zhao
# Author ID: 153103239
# Date Created: 2025/01/23

import sys

if len(sys.argv) > 1: # If there is a command-line argument given
    timer = int(sys.argv[1])
else:
    timer = 3

while timer > 0:
    print(timer)
    timer -= 1
print("blast off!")