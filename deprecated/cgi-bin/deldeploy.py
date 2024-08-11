#!/usr/bin/python3

import cgi
import subprocess

print("content-type:text/html\r\n")

f = cgi.FieldStorage()

# Delete Deployments
del_deploy_name = f.getvalue("del_deployname")

del_deploy =  subprocess.getoutput('sudo kubectl delete deployment  ' + del_deploy_name)
print(del_deploy)
print("\n\nDeployment {} Deleted Successfully ...... \n\n".format(del_deploy_name))

