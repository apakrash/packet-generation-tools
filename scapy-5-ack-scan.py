from urllib import response
from scapy.all import scapy
from scapy.all import IP
from scapy.all import ICMP
from scapy.all import *

#notice the change in flag

#response= (sr1(IP(dst="10.197.225.120")/TCP(dport=443,flags="A")))

#A noticed anomaly is that sr1 waits for the packet

response= (sr(IP(dst="10.197.225.120")/TCP(dport=443,flags="A")))


print(dir(response))
#print(response.packetfields())
print(response.summary())
print(response.show())
print(response.show2())