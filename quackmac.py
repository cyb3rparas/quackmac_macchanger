#! /usr/bin/python
import subprocess
from termcolor import colored

def change_mac(interface,new_mac):
	subprocess.call(["ifconfig",interface,"down"])
	subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
	subprocess.call(["ifconfig",interface,"up"])

def main():
	print(colored("                       WELCOME TO DR. QUACK MAC!",'cyan',attrs=['bold']))
	print(colored("          Specialist in changing mac address of Linux Patients ;)",'cyan',attrs=['bold']))
	print(colored("                      ****COd3d by 0daymaroon****",'cyan',attrs=['bold']))
	print()
	print()
	interface=str(input(colored("Enter the Target Interface:",'blue')))
	new_mac=input(colored("Enter New Mac address you want:",'blue'))
	before=subprocess.run(["ifconfig "+interface+" | grep ether"], shell=True, stdout=subprocess.PIPE).stdout
	change_mac(interface,new_mac)
	after=subprocess.run(["ifconfig "+interface+" | grep ether"], shell=True, stdout=subprocess.PIPE).stdout
	print()
	if before==after :
		print(colored("Sorry! Failed to change mac address to "+new_mac,'red',attrs=['bold']))
	else:
		print(colored("Yay! Changed mac address to "+new_mac+" successfully",'green',attrs=['bold']))

main()
