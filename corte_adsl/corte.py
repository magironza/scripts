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
comando      = 'show users'
path = os.getcwd()
conexion = paramiko.Transport((ssh_servidor, ssh_puerto))
paramiko.util.log_to_file("filename.log")
conexion.connect(username = ssh_usuario, password = ssh_clave)
canal = conexion.open_session()
canal.exec_command(comando)
salida = canal.makefile('rb', -1).readlines()
#datos_ssh = open(path+'/listado.txt', 'w')
print path

datos_nodo_alarmado = [ ]

def establece_archivo(ruta, permiso):
	archivo = open(ruta, permiso)
	return archivo

def leer_archivo(archivo):
	contenido = archivo.readlines()
	return contenido

def escribir_archivo(archivo, texto):
	archivo.write('\r\n' + texto)


arch = establece_archivo(path+"/listado.txt", "a")

for linea in salida:

	
	if len(linea.split()) == 5:
			interfaz, user, mode, idle, address = linea.split()
			escribir_archivo(arch, user + '\n')
			
		

if salida:
	print "ok"
else:
	print canal.makefile_stderr('rb', -1).readlines()

arch.seek(0)
conexion.close()
