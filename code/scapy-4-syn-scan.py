#phase: CL ready 

from scapy.all import *
import ipaddress # good library to work on ipaddresshandling
import time

############ SYN scan on 1 ip ############

ip_address = ipaddress.IPv4Address('1.1.1.1')
print(ip_address)
print(type(str(ip_address)))
print(int(ip_address))
for i in range(5):
    #time.wait(2)
    print('TCP SYN scap for '+ str(ip_address))
    ip = str(ip_address)
    response= sr1(IP(dst=ip)/TCP(dport=443,flags="S")) # dont use str(ip_address) in this line, it breaks
    print(response.show())
    ip_address += 1
    
