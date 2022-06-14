from scapy.all import *

#Internet IP

ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst="1.1.1.1/32"), timeout=2)
print(ans.summary(lambda s,r: r.sprintf("%Ether.src% %ARP.psrc%")))

