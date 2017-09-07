#!/usr/bin/env python
import telnetlib

telnet_servidor = '10.50.0.5'
telnet_usuario  = 'plantainterna'
telnet_pass = '3mt3l2016%'
telnet_puerto   = 21
comando      = "show version"


tn = telnetlib.Telnet(telnet_servidor)

tn.write(telnet_usuario + "\r")
tn.write(telnet_pass +"\n")

tn.write("show version\n")
tn.write("exit\n")

out = tn.read_all().decode("ascii")
print out
