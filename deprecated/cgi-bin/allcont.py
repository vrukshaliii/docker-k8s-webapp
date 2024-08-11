#!/usr/bin/python3

import cgi
import subprocess

print("content-type:text/html")
print()

print("List of all containers launched is listed below ....\n\n")
list_all_cont = subprocess.getoutput("sudo docker ps -a")
print(list_all_cont)
