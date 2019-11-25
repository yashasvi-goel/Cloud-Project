import json
import time
import paramiko
import boto

#This Program takes input from the IT Department about the new machine

print("Enter Details of new Instance:")
print("Enter the Provider,IP,Key File,User")
provider=input("Provider")
IP=input("IP")
key=input("key")
user=input("user")
scaling=input("scaling")
ami=input("AMI")

#We keep track of the details for all machines in this JSON file

with open('machineData.json','r') as filehandle:
    state=json.load(filehandle)


VM={}
VM["ip"]=IP
VM["user"]=user
VM["file"]=key
VM["scaling"]=scaling
VM["ami"]=ami


if provider not in state.keys():
    state[provider]={}
if type(state[provider]) is not list:
    state[provider]=[]
state[provider].append(VM)


#Create a SSH client to plant our Benchmarking Tool into the Virtual Machine

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=IP, port="22", username=user, key_filename=key)
ftp=ssh.open_sftp()

#Transfer the files

ftp.put("proj.sh","proj.sh")
#install the dependencies
ftp.put("setup.sh","setup.sh")
stdin,stdout,stderr=ssh.exec_command("sh setup.sh")

#benchmark

stdin,stdout,stderr=ssh.exec_command("sh proj.sh")

#get the results

ftp.get("ab.txt","u")
ftp.close()
ssh.close()
state=json.dumps(state)

with open('machineData.json','w') as filehandle:
    filehandle.write(state)
    filehandle.close()
