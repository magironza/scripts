#!/usr/bin/python

import smtplib
import datetime
import os
import time
from email.MIMEText import MIMEText

remitente = "cmtsalarmas@gmail.com"
destinatario = "magironza@gmail.com"


path = os.getcwd()

def establece_archivo(ruta, permiso):
	archivo = open(ruta, permiso)
	return archivo

def leer_archivo(archivo):
	contenido = archivo.readlines()
	return contenido

arch = establece_archivo(path+"/datos_all.txt", "r+")
contenido_archivo = leer_archivo(arch) 

localidades = [ ]

for dato in contenido_archivo:
	if len(dato) != 104 and not dato.startswith(" "):
		continue

	dato = dato.strip()

	if len(dato.split()) == 10:
		interfaz, dato2, dato3, total_usuario, habiles, dato6, dato7, off_usuarios, porcentaje, nodo = dato.split()

		if int(porcentaje[0:-1]) < 30:
			localidades.append(porcentaje + " " + nodo + " Usuarios desconectados" + off_usuarios)


localidades = " ".join(localidades)

#print "Hora: " +str(now)

#lectura = open('/mnt/c/Users/Emtel Sa Esp/scripts/datos_falla.txt')
#palabra= [ ]

#for nodo in lectura:
#	palabra.append(nodo[65:80])

#alarmados = " ".join(palabra)     
hora = time.strftime("%H:%M:%S")
fecha = time.strftime("%d/%m/%y")

mensaje = MIMEText("NODO ALARMADO O CON BAJO PORCENTAJE DE CONEXION," + localidades + "  FECHA REPORTE "+ fecha +" HORA REPORTE " + hora)
mensaje['From'] = remitente
mensaje['To'] = destinatario
mensaje['Subject'] = "Revisar Nodos " + hora


serverSMTP = smtplib.SMTP('smtp.gmail.com' ,587)
serverSMTP.ehlo()
serverSMTP.starttls()
serverSMTP.ehlo()
serverSMTP.login(remitente, "alertanodo")

serverSMTP.sendmail(remitente,destinatario,mensaje.as_string())

serverSMTP.close()