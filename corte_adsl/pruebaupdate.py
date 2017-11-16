#!/usr/bin/env python
import paramiko
import commands
import time
import os
from paramiko import SSHClient, AutoAddPolicy

cortar = open('pruebacorte.txt', 'r')

ssh_servidor = '190.5.195.18'
ssh_usuario  = 'root'
ssh_clave2   = '3mt3l2017*'
ssh_puerto   = 22 
path = os.getcwd()

paramiko.util.log_to_file("filename.log")
ssh = SSHClient()
ssh.set_missing_host_key_policy(AutoAddPolicy())

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ssh_servidor, username=ssh_usuario, password=ssh_clave2)


channel = ssh.invoke_shell()
	
channel.send('mysql -u root -p \n')
time.sleep(2)
pass2 = "3mt3lir3dm41l"
channel.send(pass2 + "\n")
time.sleep(2)

channel.send('use roundcubemail; \n')
time.sleep(2)
out = channel.recv(9999)
print(out.decode('utf-8'))

primera_parte = "update users set failed_login_counter=2 where user_id="
for login in cortar:
	#print primera_parte + login
	channel.send( primera_parte + login +";\n")
	time.sleep(1)

#channel.send('select * from users; \n')
time.sleep(2)
out = channel.recv(9999)
print(out.decode('utf-8'))
print("se realizo la actualizacion de contador 2")
ssh.close()
