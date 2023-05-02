#!/usr/bin/env python
import paramiko
import commands
import time
import os
from paramiko import SSHClient, AutoAddPolicy

cortar = open('pruebacorte.txt', 'r')

ssh_servidor = '127.1.1.1'
ssh_usuario  = 'usuario'
ssh_clave    = 'contrasena'
ssh_puerto   = 22
path = os.getcwd()

paramiko.util.log_to_file("filename.log")
ssh = SSHClient()
ssh.set_missing_host_key_policy(AutoAddPolicy())

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ssh_servidor, username=ssh_usuario, password=ssh_clave)


channel = ssh.invoke_shell()
	
channel.send('mysql -u root -p \n')
time.sleep(2)
pass1 = "3mt3l2015"
channel.send(pass1 + "\n")
time.sleep(2)
out = channel.recv(9999)
#print(out.decode("ascii"))

channel.send('use radius; \n')
time.sleep(2)

#AQUI VA EL CICLO QUE PERMITE HACER EL CORTE

channel.send('update radusergroup set groupname="daloRADIUS-Disabled-Users" where username="corte"; \n')

time.sleep(2)
out = channel.recv(9999)
print(out.decode("ascii"))



ssh.close()