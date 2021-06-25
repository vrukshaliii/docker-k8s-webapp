#!/usr/bin/python3

import cgi
import subprocess

print("content-type:text/html")
print()

f = cgi.FieldStorage()

# Start Docker Container
osname = f.getvalue("osname")
imgname = f.getvalue("osimage")

start_c = subprocess.getoutput("sudo docker run -dit --name {} {}".format(osname,imgname))
print(start_c)
print("Container {} launched successfully ....\n\n".format(osname))
