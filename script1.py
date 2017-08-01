#!/usr/bin/env python
import paramiko
import os
import subprocess
import commands

ssh_servidor = '10.50.0.50'
ssh_usuario  = 'plantainterna'
ssh_clave    = '3mt3l#2015'
ssh_puerto   = 36835 
comando      = 'show cable modem summary'
conexion = paramiko.Transport((ssh_servidor, ssh_puerto))
paramiko.util.log_to_file("filename.log")
conexion.connect(username = ssh_usuario, password = ssh_clave)
canal = conexion.open_session()
canal.exec_command(comando)
salida = canal.makefile('rb', -1).readlines()
archivo=open('/mnt/c/Users/Emtel Sa Esp/scripts/datos.txt', 'w')

falla = False

def envio_correo(falla):
	if falla:
		cont = 1
		while cont == 1:
			ejecutar = commands.getoutput("python /mnt/c/Users/Emtel\ Sa\ Esp/scripts/correo2s.py 1> /dev/null 2> /mnt/c/Users/Emtel\ Sa\ Esp/scripts/ficheros/fic.log")
			cont += 2
	else:
		archivo.write("no hay nodos alarmados")

for linea in salida:
	if len(linea) == 104 and linea.startswith(" "):
		interface = linea[0:2]
		datoint = int(interface)
		porcentaje = linea[66:69]
		dato2 = int(porcentaje)
		if dato2 < 30 and datoint < 8:
			archivo.write(linea)
			falla = True
envio_correo(falla)			
archivo.close()
if salida:
	print "ok"
else:
	print canal.makefile_stderr('rb', -1).readlines()


conexion.close()
