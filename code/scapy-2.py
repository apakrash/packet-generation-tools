#phase: Ubuntu tested

#Looking inside the packet prior to sending


from scapy.all import *


# fill in the ip address here, if I haven't figured out a way to find an automated way
src_ip = '10.105.130.21'
dst_ip = '1.1.1.1'

ip_layer = IP(
    src = src_ip,
    dst = dst_ip
)

icmp_request = ICMP(id=200) # Notice how individual attributes can be changed.
print(icmp_request.show())
print(ip_layer.show())

packet = ip_layer / icmp_request
response = send(packet)
print(response)
