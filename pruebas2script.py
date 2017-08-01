#!/usr/bin/env python
import paramiko
import commands
import time

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
archivo=open('/mnt/c/Users/Emtel Sa Esp/scripts/datos_falla.txt', 'w')
datos_ssh = open('/mnt/c/Users/Emtel Sa Esp/scripts/datos_all.txt', 'w')
graficos = open('/mnt/c/Users/Emtel Sa Esp/scripts/graficos.txt', 'a')

hora = time.strftime("%H:%M:%S")
fecha = time.strftime("%d/%m/%y")

hora_numero = time.strftime("%H.%M%S")

nodo = [hora_numero]

falla = False

def envio_correo(falla):
	if falla:
		cont = 1
		archivo.write("Falla encontrada")
		while cont == 1:
			ejecutar = commands.getoutput("python /mnt/c/Users/Emtel\ Sa\ Esp/scripts/correo.py 1> /dev/null 2> /mnt/c/Users/Emtel\ Sa\ Esp/scripts/ficheros/fic.log")
			cont += 2
	else:
		archivo.write("no hay nodos alarmados")

def escritura_graficos(alarmados):
	graficos.write("\n")
	graficos.write("HELLO \n")

for linea in salida:

	datos_ssh.write(linea)

	if len(linea) == 104 and linea.startswith(" "):
		interface = linea[0:2]
		datoint = int(interface)
		porcentaje = linea[65:69]
		dato2 = int(porcentaje)
		exepcion = linea.find("FERIA")
		#print exepcion

		nodo.append(porcentaje)

		if dato2 < 30 and datoint < 8 and exepcion == -1:
			print linea
			archivo.write(linea)
			falla = True
nodos_listado = " ".join(nodo)
envio_correo(falla)
escritura_graficos(nodos_listado)
datos_ssh.write('\n')
graficos.close
datos_ssh.close		
archivo.close
if salida:
	print "ok"
else:
	print canal.makefile_stderr('rb', -1).readlines()


conexion.close()
