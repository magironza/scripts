#!/usr/bin/env python
import paramiko
import commands
import time
import os
from paramiko import SSHClient, AutoAddPolicy

ssh_servidor = '127.1.1.1'
ssh_usuario  = 'usuario'
ssh_clave    = 'contrasena'
ssh_puerto   = 22 
opcion = 0
path = os.getcwd()
paramiko.util.log_to_file("filename.log")
ssh = SSHClient()
ssh.set_missing_host_key_policy(AutoAddPolicy())
login = "nada"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#ssh.connect(host, username=user, password=psw, port=22)
ssh.connect(ssh_servidor, username=ssh_usuario, password=ssh_clave)
login = raw_input("Que placa o usuario deseas buscar? : ")

#print type(dslam), dslam, type(tarjeta), tarjeta

channel = ssh.invoke_shell()

channel.send("show users | include " + login)
channel.send("\n")
time.sleep(5)
out = channel.recv(9999)
print(out.decode("ascii"))


ssh.close()
