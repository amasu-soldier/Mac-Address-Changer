#!/usr/bin/env python


import subprocess
import re

def mac_changer(inputInterface,new_mac):
	print("Changing mac address for {} {} {}".format(inputInterface, "to", new_mac))
	subprocess.call(["sudo","-S","ifconfig",inputInterface,"down"])
	subprocess.call(["sudo","-S","ifconfig",inputInterface,"hw","ether",new_mac])
	subprocess.call(["sudo","-S","ifconfig",inputInterface,"up"])


def new_mac_checker(command,inputInterface):
	ifconfig_result=str(subprocess.check_output([command,inputInterface]))
	mac_address=re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w',ifconfig_result,re.M|re.I)

	if mac_address:
		returnable_mac= mac_address.group(0)
		return returnable_mac
	else:
		print("[-] Could not read Mac Address")


def main():
	inputInterface = input("Enter Interface Name: ")
	inputMac_Address = input("Enter new Mac Address: ")
	old_mac = new_mac_checker("ifconfig", inputInterface)

	mac_changer(inputInterface, inputMac_Address)
	new_mac = new_mac_checker("ifconfig", inputInterface)

	if old_mac == new_mac:
		print("[-] Error mac address are not changed")
	else:
		print("[+] Congo Mac Address are changed :-) ")


if __name__ =="__main__":
	main()








