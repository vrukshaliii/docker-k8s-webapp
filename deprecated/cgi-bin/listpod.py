#!/usr/bin/python3

import cgi
import subprocess

print("content-type:text/html")
print()

# List Pods
print("\n\nList of all pods .....\n")
list_pod = subprocess.getoutput("sudo kubectl get po")
print(list_pod)

