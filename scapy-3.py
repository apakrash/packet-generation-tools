###### Scraping this ##########

'''
Sending ICMP packets using scapy

'''

from urllib import response
from scapy.all import scapy
from scapy.all import IP
from scapy.all import ICMP
from scapy.all import sr

src_ip = '10.65.49.110'
# to check how to find this in learning LL 2.0, worst case worst, have to maunally edit this.

dst_ip = 'www.facebook.com' #using hostname also works

ip_layer = IP(
    src = src_ip,
    dst = dst_ip
)

icmp_request = ICMP(id=100)
print(icmp_request.show())
print(ip_layer.show())

packet = ip_layer / icmp_request
#for i in range(5):
    
responsePacket = sr(packet, iface='Ethernet 5')
if responsePacket:
   print(responsePacket.index)