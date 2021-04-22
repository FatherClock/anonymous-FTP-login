#!/usr/bin/python

import ftplib

def anonLogin(hostname):
	try:
		ftp = ftplib.FTP(hostname)
		ftp.login('anonymous','anonymous')
#		print("[+] Logged In Successfully to")
		print("[+] " + hostname + " FTP Anonymous Login Succeeded.")
		ftp.quit()
		return True
	except Exception, e:
		print ("[-] " + hostname + "FTP Anonymous Login Failed.")

host = raw_input("Enter IP of FTP Host: ")
anonLogin(host)



