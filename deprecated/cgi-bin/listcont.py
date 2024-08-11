#!/usr/bin/python3

import cgi
import subprocess

print("content-type:text/html")
print()

# List of all running containers
print("\n\nList of all running containers .....\n")
list_cont = subprocess.getoutput("sudo docker ps")
print(list_cont)
