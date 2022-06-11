#phase: Ubutntu done 

from scapy.all import *
import ipaddress # good library to work on ipaddresshandling
import time

############ Section 1: SYN scan on 1 ip ############

#uncomment to run
'''
response= (sr1(IP(dst="1.1.1.1")/TCP(dport=443,flags="S")))
#print(response.packetfields())
print(response.summary())
print(response.show())
print(response.show2())

wrpcap("syn-scap.pcap", response)

'''


#why would we do this when we know that this can be utilized by iperf, hping or any such tool

# this is not working
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
    
