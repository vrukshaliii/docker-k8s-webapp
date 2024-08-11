#!/usr/bin/python3

import cgi
import subprocess

print("content-type:text/html")
print()

f = cgi.FieldStorage()

# Launch Pod
podname = f.getvalue("podname")
imgname = f.getvalue("pimage")

start_pod = subprocess.getoutput("sudo kubectl run {} --image={}".format(podname,imgname))
print(start_pod)
print("\n\nPod {} launched successfully ....\n\n".format(podname))
