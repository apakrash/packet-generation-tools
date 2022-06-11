#phase: Ubuntu tested, LL test pending

from scapy.all import *

############ Section 3 srloop() ############

response_srloop = srloop(IP(dst="1.1.1.1")/ICMP(), count=2)   
print(response_srloop)


