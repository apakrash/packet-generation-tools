#phase: Ubuntu tested, LL test pending


from scapy.all import *


############ Section 1 sr() ############

'''The sr() function is used to send a packet or group of packets when you expect a response back.'''

response_sr = sr(IP(dst="1.1.1.1")/ICMP())
print(response_sr)
#wrpcap("response_sr.pcap", response_sr) # this will throw an error


