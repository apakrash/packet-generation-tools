#phase: Ubuntu tested, LL test pending


from scapy.all import *

############ Section 2 sr1() ############

#The sr1() function for getting 1 response packet back'''

response_sr1 = sr1(IP(dst="1.1.1.1")/ICMP())
print(response_sr1.summary())
wrpcap("response_sr1.pcap", response_sr1)


# Notice that the response can be saved in response_sr1.pcap. There is a sample response_sr1-sample.pcap present to check
# To check the file, please use tcdump -r response_sr1.pcap or tcpdump -r response_sr1-sample.pcap  ## use sudo if normal tcpdump is not working

