#!/usr/bin/env python
import paramiko
import commands
import time
import os

ssh_servidor = '127.1.1.1'
ssh_usuario  = 'usuario'
ssh_clave    = 'contrasena'
ssh_puerto   = 22 
comando      = "telnet 172.16.1.21"
path = os.getcwd()
conexion = paramiko.Transport((ssh_servidor, ssh_puerto))
paramiko.util.log_to_file("filename.log")
conexion.connect(username = ssh_usuario, password = ssh_clave)
canal = conexion.open_session()
#dslam = input("A que dslam desea acceder :")
#tarjeta = input("Numero de tarjeta: ")
#puerto = input("Numero del puerto: ")
canal.exec_command(comando)


salida = canal.makefile('rb', -1).readlines()



if salida:
	for linea in salida:
		print(linea)
else:
	print(canal.makefile_stderr('rb', -1).readlines())

conexion.close()
