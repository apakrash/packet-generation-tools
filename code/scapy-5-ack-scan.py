from urllib import response
from scapy.all import scapy
from scapy.all import IP
from scapy.all import ICMP
from scapy.all import *

#notice the change in flag

print('Starting ACK scan for ip address 1.1.1.1  for port 443 \n\n')

response= (sr1(IP(dst="1.1.1.1")/TCP(dport=443,flags="A")))
response.show()
