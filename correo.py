#!/usr/bin/python

import smtplib
import datetime
import os
import time
from email.MIMEText import MIMEText

remitente = "cmtsalarmas@gmail.com"
destinatario = "magironza@gmail.com"

#print "Hora: " +str(now)

lectura = open('/mnt/c/Users/Emtel Sa Esp/scripts/datos.txt')
palabra= [ ]

for nodo in lectura:
	palabra.append(nodo[65:80])

alarmados = " ".join(palabra)
print alarmados
hora = time.strftime("%H:%M:%S")
fecha = time.strftime("%d/%m/%y")

mensaje = MIMEText("NODO ALARMADO FECHA REPORTE HORA REPORTE " + fecha + " " + hora + " " + alarmados)
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