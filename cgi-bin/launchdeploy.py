#!/usr/bin/python3

import cgi
import subprocess

print("content-type:text/html")
print()

f = cgi.FieldStorage()

# Launch Deployment
deployname = f.getvalue("deployname")
imgname = f.getvalue("dimage")

start_deploy = subprocess.getoutput("sudo kubectl create deployment {} --image={}".format(deployname,imgname))
print(start_deploy)
print("\n\n Deployment {} launched successfully ....\n\n".format(deployname))

