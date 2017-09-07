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
dslam = input("A que dslam desea acceder :")
tarjeta = input("Numero de tarjeta: ")
puerto = input("Numero del puerto: ")
#print type(dslam), dslam, type(tarjeta), tarjeta

channel = ssh.invoke_shell()


def conexion_dslam1(dslam_numero, tarjeta, puerto):
	channel.send('telnet 172.16.1.' + str(dslam_numero) + "\n")
	time.sleep(5)
	user1 = "admemtel"
	pass1 = "3mt3l2016#"
	time.sleep(2)
	channel.send(user1 + "\n")
	channel.send(pass1 + "\n")
	time.sleep(2)
	out = channel.recv(9999)
	print(out.decode("ascii"))
	print "1 - Ver la configuracion \n"
	print "2 - Ver cuanto soporta puerto\n"
	see = input("Escribe 1 o 2: ")
	if see == 1:
		channel.send("show run int adsl_0/" + str(tarjeta)+"/"+str(puerto))
		channel.send("\n")
	else: 
		channel.send("show adsl port-status adsl_0/" + str(tarjeta)+"/"+str(puerto))
		channel.send("\n")

	time.sleep(3)
	out = channel.recv(9999)
	print(out.decode("ascii"))


def conexion_dslam2(dslam_numero, tarjeta, puerto):
	channel.send('telnet 172.16.1.'+ str(dslam_numero))
	channel.send("\n")
	time.sleep(2)
	user2 = "edsl"
	pass2 = "edsl"
	time.sleep(2)
	channel.send(user2 + "\n")
	channel.send(pass2 + "\n")
	time.sleep(2)
	out = channel.recv(9999)
	print(out.decode("ascii"))
	print "1 - Ver la interfaz \n"
	print "2 - Ver la tarjeta \n"
	see = input("Escribe 1 o 2: ")
	if see == 1:
		channel.send("show adsl status interface " + str(tarjeta)+"/"+str(puerto))
		channel.send("\n")
	else: 
		channel.send("show adsl status slot " + str(tarjeta))
		channel.send("\n")
		channel.send("p")
		channel.send("\n")
		channel.send("p")
		channel.send("\n")
	time.sleep(3)
	out = channel.recv(9999)
	print(out.decode("ascii"))
	#print "Deseas resetear el puerto: "
	#reset = input("1- y/ 2- n")
	#if reset == 1:
	#	channel.send("conf interface adsl-mpvc" + str(tarjeta)+"/"+str(puerto))
	#	channel.send("\n")
	#else:
	#	channel.send("log\n")
	#time.sleep(10)
	out = channel.recv(9999)
	print(out.decode("ascii"))

while opcion != 9:
	if dslam == 33 or dslam == 87:
		conexion_dslam2(dslam, tarjeta, puerto)
	else:
		conexion_dslam1(dslam, tarjeta, puerto)

	test = input("Reset?: (1-y/2-n) ")
	opcion = input("Desea salir (s-9)")

def reset_parameters(dslam, tarjeta, puerto):
	if dslam == 87 or dslam == 33:
		channel.send("conf interface adsl-mpvc " + str(tarjeta)+"/"+str(puerto))
		channel.send("\n")
		channel.send("shutdown")
		channel.send("\n")
		time.sleep(2)
		channel.send("no shutdown")
		channel.send("\n")
		time.sleep(2)
		out = channel.recv(9999)
		print(out.decode("ascii"))
		channel.send("end\n")
	else:
		channel.send("conf t")
		channel.send("\n")
		channel.send("interface adsl_0/" + str(tarjeta)+"/"+str(puerto))
		channel.send("\n")
		channel.send("shutdown")
		channel.send("\n")
		time.sleep(2)
		channel.send("no shutdown")
		time.sleep(2)
		out = channel.recv(9999)
		print(out.decode("ascii"))
		channel.send("end\n")

	if test == 1:
		reset_parameters(dslam, tarjeta, puerto)
	else:
		print("Thanks for coming")
		if dslam == 87 or dslam == 33:
			channel.send("conf t\n")
			channel.send("conf interface adsl-mpvc " + str(tarjeta)+"/"+str(puerto))
			channel.send("\n")
			channel.send("no shutdown")
			channel.send("\n")
			channel.send("end\n")
			time.sleep(2)
			channel.send("log\n")
		else:
			channel.send("conf t")
			channel.send("\n")
			channel.send("interface adsl_0/" + str(tarjeta)+"/"+str(puerto))
			channel.send("\n")
			channel.send("shutdown")
			channel.send("\n")
			channel.send("exit\n")
		out = channel.recv(9999)
		print(out.decode("ascii"))
	out = channel.recv(9999)
	print(out.decode("ascii"))
	ssh.close()
