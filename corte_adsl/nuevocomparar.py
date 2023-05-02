#!/usr/bin/env python
import os
autenticando = open('listado.txt', 'r')
cortar = open('corte.txt', 'r')
path = os.getcwd()

lista1 = []
lista2 = []
final = []

for line in autenticando:
   lista1.append(line[:-1])
   
for line in cortar:
   lista2.append(line[0:7])
   #print lista2
   
for i in lista2:
	for j in lista1:
		ex3 = j.startswith(str(i))
		if ex3 > 0:
			final.append(j)
			#print j
print(path)

open("existe.txt", "w").write("\r\n".join(("".join(item)) for item in final))