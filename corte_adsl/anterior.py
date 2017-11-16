#!/usr/bin/env python
import os
autenticando = open('anteriorcorte.txt', 'r')
cortar = open('corte.txt', 'r')
path = os.getcwd()
 
lista1 = []
lista2 = []
final = []
 
for line in autenticando:
    lista1.append(line[:-1])
     
for line in cortar:
    lista2.append(line[0:7])
     
#for i in lista2:
#	if i in lista1:
#		final.append(i)

for i in lista2:
	for j in lista1:
		ex3 = j.startswith(str(i))
		if ex3 > 0:
			final.append(j)
			#print j
print path + "----> Ok la comparacion"

   
open("iguales.txt", "a").write("\r\n".join(("".join(item)) for item in final))



  