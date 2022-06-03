from scapy.all import *

#Internet IP

ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst="1.1.1.1/32"), timeout=2)
print(ans.summary(lambda s,r: r.sprintf("%Ether.src% %ARP.psrc%")))


'''
6c:41:6a:c7:b8:ff 1.1.1.1

guess whose mac address address is this?
'''
