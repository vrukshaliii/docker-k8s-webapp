#!/usr/bin/python3

import cgi
import subprocess

print("content-type:text/html\r\n")

f = cgi.FieldStorage()

# Stop Docker Container
os_name = f.getvalue("stop_os_name")

stop = subprocess.getoutput('sudo docker stop  ' + os_name)
print(stop)
print("\n\nContainer {} stopped successfully ...\n".format(os_name))
