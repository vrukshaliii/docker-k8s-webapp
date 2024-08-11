#!/usr/bin/python3

import cgi
import subprocess

print("content-type:text/html")
print()

# List of Docker images
print("\n\nList of all Docker images in your system .....\n\n")
list_img = subprocess.getoutput("sudo docker images")
print(list_img)

