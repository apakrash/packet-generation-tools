#phase: CL ready 

from scapy.all import *
import ipaddress # good library to work on ipaddresshandling
import time

############ SYN scan on 1 ip ############

ip_address = ipaddress.IPv4Address('1.1.1.1')

print('Starting SYN scan for ip address 1.1.1.1 to 1.1.1.3 for port 443 \n\n')

for i in range(3):
    time.sleep(2)
    print('TCP SYN scap for ip = '+ str(ip_address))
    ip = str(ip_address)
    response= sr1(IP(dst=ip)/TCP(dport=443,flags="S")) # dont use str(ip_address) in this line, it breaks
    response.show()
    ip_address += 1
    print('***********************************************')
    time.sleep(2)
print('\n\n')
