#!/usr/bin/env python
import paramiko
import commands
import time
import os
from paramiko import SSHClient, AutoAddPolicy

ssh_servidor = '190.5.200.10'
ssh_usuario  = 'plantainterna'
ssh_clave    = '3mt3l#2015'
ssh_puerto   = 22 
opcion = 0
#comando      = "telnet  "  + telnet_servidor
path = os.getcwd()
#conexion = paramiko.Transport((ssh_servidor, ssh_puerto))
paramiko.util.log_to_file("filename.log")
#conexion.connect(username = ssh_usuario, password = ssh_clave)
#canal = conexion.open_session()
#dslam = input("A que dslam desea acceder :")
#tarjeta = input("Numero de tarjeta: ")
#puerto = input("Numero del puerto: ")
ssh = SSHClient()
ssh.set_missing_host_key_policy(AutoAddPolicy())


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#ssh.connect(host, username=user, password=psw, port=22)
ssh.connect(ssh_servidor, username=ssh_usuario, password=ssh_clave)
tarjeta = input("Numero de tarjeta: ")
puerto = input("Numero del puerto: ")
#print type(dslam), dslam, type(tarjeta), tarjeta

channel = ssh.invoke_shell()


channel.send('telnet 10.50.0.5\n')
channel.send("\n")
time.sleep(3)
user1 = "plantainterna"
pass1 = "3mt3l2016%"
channel.send(user1 + "\n")
channel.send(pass1 + "\n")
time.sleep(2)
channel.send('telnet 192.168.30.11\n')
channel.send("\n")
time.sleep(3)
user2 = "zte"
pass2 = "zte"
channel.send(user2 + "\n")
channel.send(pass2 + "\n")
time.sleep(2)
out = channel.recv(9999)
print(out.decode("ascii"))

while opcion != 9:
	print "1 - Ver la configuracion \n"
	print "2 - Ver cuanto soporta puerto\n"
	see = input("Escribe 1 o 2: ")
	if see == 1:
		channel.send("show run int adsl_1/" + str(tarjeta)+"/"+str(puerto))
		channel.send("\n")
	else: 
		channel.send("show adsl port-status adsl_1/" + str(tarjeta)+"/"+str(puerto) +" local entire")
		channel.send("\n")
	time.sleep(3)
	out = channel.recv(9999)
	print(out.decode("ascii"))
	opcion = input("Desea salir? (9-s)")

time.sleep(1)
channel.send("exit\n")
time.sleep(1)
channel.send("exit\n")
time.sleep(1)
out = channel.recv(9999)
print(out.decode("ascii"))
ssh.close()
