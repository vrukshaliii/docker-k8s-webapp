#!/usr/bin/python3

import cgi
import subprocess

print("content-type:text/html\r\n")

f = cgi.FieldStorage()

# Delete Docker Container
os_name = f.getvalue("del_os_name")

delete_c =  subprocess.getoutput('sudo docker rm -f  ' + os_name)
#print(delete_c)
print("\n\n\n\nSuccessfully Deleted Container {} ...... \n\n".format(os_name))
