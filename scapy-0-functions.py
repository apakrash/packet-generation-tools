

from urllib import response
from scapy.all import scapy
from scapy.all import IP
from scapy.all import ICMP
from scapy.all import *

'''The sr() function is used to send a packet or group of packets when you expect a response back.'''

#response= sr(IP(dst="10.197.223.121")/ICMP())
#print(response.summary())

'''The sr1() function is fire and forget'''


#response= sr1(IP(dst="10.197.223.121")/ICMP())
#print(response.summary())



''''If there is a 'p' at the end, then an L2 packet is being sent''' # this is still in progress

#srp

#response= srp(IP(dst="10.197.223.121")/ICMP())
#print(response.summary())



#srp1

#response= srp1(IP(dst="10.197.223.121")/ICMP())
#print(response.summary())


#srloop() | the name says it

response = srloop(IP(dst="10.197.223.121")/ICMP(), count=2)   #----> this is not working
print(dir(response))
print(response.index())
