from urllib import response
from scapy.all import *

src_ip = '1.1.1.1'
dst_ip = 'www.facebook.com'

ip_layer = IP(
    src = src_ip,
    dst = dst_ip
)

icmp_request = ICMP(id=100)
print(icmp_request.show())
print(ip_layer.show())

packet = ip_layer / icmp_request
send(packet)