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

def verificar_parametros(tarjeta, puerto):
	print("verificar la velocidad y configuracion")
	print "1 - Ver la configuracion \n"
	print "2 - Ver cuanto soporta puerto\n"
	print "3 - Ver tarjeta\n"

	see = input("Escribe 1, 2 o 3: ")
	if see == 1:
		channel.send("show run int adsl_1/" + str(tarjeta)+"/"+str(puerto))
		channel.send("\n")
	elif see == 3: 
		channel.send("show adsl port-status adsl_1/" + str(tarjeta)+"/1-10 local entire")
		channel.send("\n")
	else:
		channel.send("show adsl port-status adsl_1/" + str(tarjeta)+"/"+str(puerto) +" local entire")
		channel.send("\n")
	time.sleep(3)
	out = channel.recv(9999)
	print(out.decode("ascii"))
	return

def reset(tarjeta, puerto):
	test = input("Reset?: (1-y/2-n) ")
	if test == 1:
		channel.send("conf t")
		channel.send("\n")
		channel.send("interface adsl_1/" + str(tarjeta)+"/"+str(puerto))
		channel.send("\n")
		channel.send("shutdown")
		channel.send("\n")
		time.sleep(2)
		channel.send("no shutdown\n")
		time.sleep(2)
		channel.send("end\n")
		out = channel.recv(9999)
		print(out.decode("ascii"))
	else:
		print("Thanks for coming")
	return

while opcion != 9:
	verificar_parametros(tarjeta, puerto)
	reset(tarjeta, puerto)

	opcion = input("Desea salir? (9-s)")

time.sleep(1)
channel.send("exit\n")
time.sleep(1)
channel.send("exit\n")
time.sleep(1)
out = channel.recv(9999)
print(out.decode("ascii"))
ssh.close()
