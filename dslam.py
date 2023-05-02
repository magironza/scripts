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


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#ssh.connect(host, username=user, password=psw, port=22)
ssh.connect(ssh_servidor, username=ssh_usuario, password=ssh_clave)
dslam = input("A que dslam desea acceder :")
tarjeta = input("Numero de tarjeta: ")
puerto = input("Numero del puerto: ")
#print type(dslam), dslam, type(tarjeta), tarjeta

channel = ssh.invoke_shell()


def conexion_dslam1(dslam_numero):
	
	channel.send('telnet 172.16.1.' + str(dslam_numero) + "\n")
	time.sleep(2)
	user1 = "admemtel"
	pass1 = "3mt3l2016#"
	time.sleep(2)
	channel.send(user1 + "\n")
	channel.send(pass1 + "\n")
	time.sleep(2)
	out = channel.recv(9999)
	print(out.decode("ascii"))

def conexion_dslam2(dslam_numero):
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
	

def verificar_parametros1(tarjeta, puerto):
	print("1 - Ver la configuracion \n")
	print("2 - Ver cuanto soporta puerto\n")
	print("3 - Ver la tarjeta \n")

	see = input("Escribe 1, 2 o 3: ")
	if see == 1:
		channel.send("show run int adsl_0/" + str(tarjeta)+"/"+str(puerto))
		channel.send("\n")
	elif see == 3:
		channel.send("show adsl port-status adsl_0/" + str(tarjeta)+"/1-10")
		channel.send("\n")
	else:
		channel.send("show adsl port-status adsl_0/" + str(tarjeta)+"/"+str(puerto))
		channel.send("\n")

	time.sleep(3)
	out = channel.recv(9999)
	print(out.decode("ascii"))
	return

def verificar_parametros2(tarjeta, puerto):
	print("1 - Ver la interfaz \n")
	print("2 - Ver la tarjeta \n")

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
	time.sleep(10)
	out = channel.recv(9999)
	print(out.decode("ascii"))
	return

if dslam == 33 or dslam == 87:
	conexion_dslam2(dslam)
else:
	conexion_dslam1(dslam)

def reset_parameters1(tarjeta, puerto):
	test = input("Reset?: (1-y/2-n) - 3-cortar ")
	if test == 1:
		channel.send("conf t")
		channel.send("\n")
		channel.send("interface adsl_0/" + str(tarjeta)+"/"+str(puerto))
		channel.send("\n")
		channel.send("shutdown")
		channel.send("\n")
		time.sleep(2)
		channel.send("no shutdown\n")
		time.sleep(2)
		channel.send("end\n")
		out = channel.recv(9999)
		print(out.decode("ascii"))
	elif test == 3:
		channel.send("conf t")
		channel.send("\n")
		channel.send("interface adsl_0/" + str(tarjeta)+"/"+str(puerto))
		channel.send("\n")
		channel.send("shutdown")
		channel.send("\n")
		time.sleep(2)
		channel.send("end\n")
		out = channel.recv(9999)
		print(out.decode("ascii"))
		print("servicio cortado")

	else:
		print("Thanks for coming")
	return
	

def reset_parameters2(tarjeta, puerto):
	test = input("Reset?: (1-y/2-n) - 3-cortar ")
	if test == 1:
		channel.send(" conf interface adsl-mpvc " + str(tarjeta)+"/"+str(puerto))
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
	elif test == 3:
		channel.send(" conf interface adsl-mpvc " + str(tarjeta)+"/"+str(puerto))
		channel.send("\n")
		channel.send("shutdown")
		channel.send("\n")
		time.sleep(2)
		out = channel.recv(9999)
		print(out.decode("ascii"))
		channel.send("end\n")
		print("servicio cortado")

	else:
		print("Thanks for coming")

	return
	

while opcion != 9:
	if dslam == 33 or dslam == 87:
		#conexion_dslam2(dslam, tarjeta, puerto)
		verificar_parametros2(tarjeta, puerto)
		reset_parameters2(tarjeta, puerto)
	else:
		#conexion_dslam1(dslam, tarjeta, puerto)
		verificar_parametros1(tarjeta, puerto)
		reset_parameters1(tarjeta, puerto)

	#print opcion

	opcion = input("Desea salir (s-9):")

if opcion == 9:
	if dslam == 87 or dslam == 33:
		channel.send("end\n")
		channel.send("log\n")
	else:
		channel.send("end\n")
		channel.send("exit\n")
	#print(opcion)
	out = channel.recv(9999)
	print(out.decode("ascii"))
ssh.close()
