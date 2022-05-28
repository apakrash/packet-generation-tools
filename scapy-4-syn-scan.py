#phase: local test pass | to check on LL2.0

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
for ip_address in range(1,5):
    response= (sr1(IP(dst=str(ip_address))/TCP(dport=443,flags="S")))
    print(response.show())
    ip_address += 1
    time.wait(2)


