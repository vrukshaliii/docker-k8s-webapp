#!/usr/bin/python3

import cgi
import subprocess

print("content-type:text/html")
print()

# List of all services
print("\nList of all services .....\n\n")
list_svc = subprocess.getoutput("sudo kubectl get svc")
print(list_svc)

