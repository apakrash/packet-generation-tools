#this is not working


from urllib import response
from scapy.all import scapy
from scapy.all import IP
from scapy.all import ICMP
from scapy.all import *


ans, unans = sr( IP(dst="192.168.1.0/24")/TCP(dport=80,flags="S") )
ans.summary( lambda s,r : r.sprintf("%IP.src% is alive") )


'''
>>> print(ans.summary(lambda s,r: r.sprintf("%Ether.src% %ARP.psrc%")))

Sample output

6c:41:6a:c7:b8:ff 10.197.224.0
6c:41:6a:c7:b8:ff 10.197.225.0
6c:41:6a:c7:b8:ff 10.197.224.1
6c:41:6a:c7:b8:ff 10.197.225.1
6c:41:6a:c7:b8:ff 10.197.224.2
6c:41:6a:c7:b8:ff 10.197.225.2
6c:41:6a:c7:b8:ff 10.197.224.3
6c:41:6a:c7:b8:ff 10.197.225.3
6c:41:6a:c7:b8:ff 10.197.224.4
6c:41:6a:c7:b8:ff 10.197.225.4
6c:41:6a:c7:b8:ff 10.197.224.5
6c:41:6a:c7:b8:ff 10.197.225.5
6c:41:6a:c7:b8:ff 10.197.224.6
6c:41:6a:c7:b8:ff 10.197.225.6
6c:41:6a:c7:b8:ff 10.197.224.7
6c:41:6a:c7:b8:ff 10.197.225.7
6c:41:6a:c7:b8:ff 10.197.224.8
6c:41:6a:c7:b8:ff 10.197.225.8
6c:41:6a:c7:b8:ff 10.197.224.9
6c:41:6a:c7:b8:ff 10.197.225.9
6c:41:6a:c7:b8:ff 10.197.224.10
6c:41:6a:c7:b8:ff 10.197.225.10
6c:41:6a:c7:b8:ff 10.197.224.11
6c:41:6a:c7:b8:ff 10.197.225.11
6c:41:6a:c7:b8:ff 10.197.224.12
6c:41:6a:c7:b8:ff 10.197.225.12
6c:41:6a:c7:b8:ff 10.197.224.13
6c:41:6a:c7:b8:ff 10.197.225.13
6c:41:6a:c7:b8:ff 10.197.224.14
6c:41:6a:c7:b8:ff 10.197.225.14
6c:41:6a:c7:b8:ff 10.197.224.15
6c:41:6a:c7:b8:ff 10.197.225.15
6c:41:6a:c7:b8:ff 10.197.224.16
6c:41:6a:c7:b8:ff 10.197.225.16
6c:41:6a:c7:b8:ff 10.197.224.17
6c:41:6a:c7:b8:ff 10.197.225.17
6c:41:6a:c7:b8:ff 10.197.224.18
6c:41:6a:c7:b8:ff 10.197.225.18
6c:41:6a:c7:b8:ff 10.197.224.19
6c:41:6a:c7:b8:ff 10.197.225.19
6c:41:6a:c7:b8:ff 10.197.224.20
6c:41:6a:c7:b8:ff 10.197.225.20
6c:41:6a:c7:b8:ff 10.197.224.21
6c:41:6a:c7:b8:ff 10.197.225.21
6c:41:6a:c7:b8:ff 10.197.224.22
6c:41:6a:c7:b8:ff 10.197.225.22
6c:41:6a:c7:b8:ff 10.197.224.23
6c:41:6a:c7:b8:ff 10.197.225.23
6c:41:6a:c7:b8:ff 10.197.224.24
6c:41:6a:c7:b8:ff 10.197.225.24
6c:41:6a:c7:b8:ff 10.197.224.25
6c:41:6a:c7:b8:ff 10.197.225.25
6c:41:6a:c7:b8:ff 10.197.224.26
6c:41:6a:c7:b8:ff 10.197.225.26
6c:41:6a:c7:b8:ff 10.197.224.27
6c:41:6a:c7:b8:ff 10.197.225.27
6c:41:6a:c7:b8:ff 10.197.224.28
6c:41:6a:c7:b8:ff 10.197.225.28
6c:41:6a:c7:b8:ff 10.197.224.29
6c:41:6a:c7:b8:ff 10.197.225.29
6c:41:6a:c7:b8:ff 10.197.225.255



'''

#Internet IP

ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst="1.1.1.1/32"), timeout=2)
print(ans.summary(lambda s,r: r.sprintf("%Ether.src% %ARP.psrc%")))


'''
6c:41:6a:c7:b8:ff 1.1.1.1
'''