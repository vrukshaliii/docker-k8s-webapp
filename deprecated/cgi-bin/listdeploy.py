#!/usr/bin/python3

import cgi
import subprocess

print("content-type:text/html")
print()

print("\n\nList of all deployments .....\n")
list_deploy = subprocess.getoutput("sudo kubectl get deploy")
print(list_deploy)
