#!/usr/bin/env python
import paramiko
import commands
import time
import os

ssh_servidor = '127.1.1.1'
ssh_usuario  = 'usuario'
ssh_clave    = 'contrasena'
ssh_puerto   = 36835 
comando      = 'show cable modem summary'
path = os.getcwd()
conexion = paramiko.Transport((ssh_servidor, ssh_puerto))
paramiko.util.log_to_file("filename.log")
conexion.connect(username = ssh_usuario, password = ssh_clave)
canal = conexion.open_session()
canal.exec_command(comando)
salida = canal.makefile('rb', -1).readlines()
doc_falla = open(path+'/datos_falla.txt', 'r+')
datos_ssh = open(path+'/datos_all.txt', 'w')
#graficos = open(path+'/graficos.txt', 'a')

hora = time.strftime("%H:%M:%S")
fecha = time.strftime("%d/%m/%y")

hora_numero = time.strftime("%H.%M")

nodo = [hora_numero]
datos_nodo_alarmado = [ ]

falla = False

def establece_archivo(ruta, permiso):
	archivo = open(ruta, permiso)
	return archivo

def leer_archivo(archivo):
	contenido = archivo.readlines()
	return contenido

def escribir_archivo(archivo, texto):
	archivo.write('\r'+texto+ '\n')

def envio_correo(falla):
	if falla:
		cont = 1
		while cont == 1:
			commands.getoutput("python /mnt/c/Users/Emtel\ Sa\ Esp/scripts/trycorreo.py 1> /dev/null 2> /mnt/c/Users/Emtel\ Sa\ Esp/scripts/ficheros/fic.log")
			cont += 2
	else:
		print("Todo esta ok")

arch = establece_archivo(path+"/datos.txt", "r+")


for linea in salida:

	datos_ssh.write(linea)

	if len(linea) == 104 and linea.startswith(" "):
		linea = linea.strip()

		if len(linea.split()) == 10:
			interfaz, dato2, dato3, total_usuario, habiles, dato6, dato7, off_usuarios, porcentaje, nodo = linea.split()
		#interface = linea[0:2]
		#datoint = int(interface)
		#porcentaje = linea[65:69]
		#dato2 = int(porcentaje)
		#exepcion = linea.find("ANTONIA")
		#print exepcion
			if int(porcentaje[0:-1]) < 30 and int(interfaz[0:1]) < 8 and int(off_usuarios[0:2]) != 0:
				doc_falla.write(linea)
				escribir_archivo(arch, hora + linea + '\r\n')
				datos_nodo_alarmado.append(linea)
				falla = True

#datos_listado = " ".join(datos_nodo_alarmado)
nodos_listado = " ".join(nodo)
envio_correo(falla)
datos_ssh.write('\r\n')
datos_ssh.close()		
doc_falla.close()
if salida:
	print("ok")
else:
	print(canal.makefile_stderr('rb', -1).readlines())

arch.seek(0)
conexion.close()
