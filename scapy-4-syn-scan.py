#phase: local test pass | to check on LL2.0

from urllib import response
from scapy.all import scapy
from scapy.all import IP
from scapy.all import ICMP
from scapy.all import *

response= (sr1(IP(dst="10.197.223.121")/TCP(dport=443,flags="S")))
print(dir(response))
#print(response.packetfields())
print(response.summary())
print(response.show())
print(response.show2())


#why would we do this when we know that this can be utilized by iperf, hping or any such tool


response= (sr1(IP(dst=ip)/TCP(dport=443,flags="S")))
print(response.summary())

