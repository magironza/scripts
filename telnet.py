#!/usr/bin/env python
import getpass
import sys
import telnetlib

HOST = "172.16.1.21"
user = "admemtel"
password = "3mt3l2016#"

tn = telnetlib.Telnet(HOST)

tn.read_until("login: ")
tn.write(user + "\n")
tn.read_until("Password: ")
tn.write(password + "\n")

tn.write("show running-config interface adsl_0/2/1 1> /dev/null 2> /mnt/c/Users/Emtel\ Sa\ Esp/scripts/ficheros/ficherotelnet.log")
tn.write("exit\n")

print tn.read_all()