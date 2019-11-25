import time
import paramiko
import mysql.connector
import json
import boto3
import sys

#This is a program to keep a check on all the machines in a timed fashion and do the needful

def predict(VM,temp):
#    with open("temp","r") as file:
 #       data = file.read().replace('\n','')
        
    return False

def scaleUP(VM):

    client=boto3.client('ec2')
    ec2=boto3.resource('ec2')
    health=boto3.client('health')

    instances=ec2.create_instances(
            ImageId=VM["ami"],
            MinCount=1,
            InstanceType='t2.micro'
            keyName=VM["file"]
            )

#Fetch the details of all the machines

with open('machineData.json','r') as filehandle:
    state=json.load(filehandle)

#Iterating over all the machines
for prov in state.keys():
    for VM in prov.keys():
        VM=prov[VM]
        ip=VM["ip"]
        user=VM["user"]
        key=VM["file"]
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=ip, port="22", username=user, key_filename=key)
        #Running the check on the virtual machine
        stdin,stdout,stderr=ssh.exec_command("sh proj.sh")
        ftp=ssh.open_sftp()
        ftp.get("ab.txt","temp")
        #predict the Overflow
        if predict(VM,temp)==True:
            scaleUP(VM)
        print stdout.readlines()
        ssh.close()
