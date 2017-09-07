#!/usr/bin/python
import os
import commands

path = os.getcwd()

def establece_archivo(ruta, permiso):
	archivo = open(ruta, permiso)
	return archivo

def leer_archivo(archivo):
	contenido = archivo.readlines()
	return contenido

def escribir_archivo(archivo, texto):
	archivo.write('\r\n' + texto)


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
			localidades.append(porcentaje + " " + nodo)


localidades = " ".join(localidades)
print localidades
commands.getoutput("python /mnt/c/Users/Emtel\ Sa\ Esp/scripts/trycorreo.py 1> /dev/null 2> /mnt/c/Users/Emtel\ Sa\ Esp/scripts/ficheros/fic.log")
#print interfaz, total_usuario, habiles, off_usuarios, len(porcentaje), nodo
	


	

