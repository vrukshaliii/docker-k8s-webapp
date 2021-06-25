#!/usr/bin/python3

import cgi
import subprocess

print("content-type:text/html")
print()

# Docker Information
docker_info = subprocess.getoutput("sudo docker info")
print(docker_info)

