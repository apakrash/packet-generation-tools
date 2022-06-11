#phase: Ubuntu tested, LL test pending


from scapy.all import *


############ Section 1 sr() ############

'''The sr() function is used to send a packet or group of packets when you expect a response back.'''

'''
response_sr = sr(IP(dst="1.1.1.1")/ICMP())
print(response_sr)
#wrpcap("response_sr.pcap", response_sr) # this will throw an error

'''

############ Section 2 sr1() ############

#The sr1() function for getting 1 response packet back'''
'''
response_sr1 = sr1(IP(dst="1.1.1.1")/ICMP())
print(response_sr1.summary())
wrpcap("response_sr1.pcap", response_sr1)

'''
# Notice that the response can be saved in response_sr1.pcap. There is a sample response_sr1-sample.pcap present to check
# To check the file, please use tcdump -r response_sr1.pcap or tcpdump -r response_sr1-sample.pcap  ## use sudo if normal tcpdump is not working



############ Section 3 srloop() ############
'''
response_srloop = srloop(IP(dst="1.1.1.1")/ICMP(), count=2)   
print(response_srloop)

'''

############ Section 4 srp() ############

''''If there is a 'p' at the end, then an L2 packet is being sent''' 

# get the output of interface using the command: ip a s and put it in the variable below
'''
iface = 'ens192'

ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst='1.1.1.1'), timeout=3, iface=iface)
print(ans.summary()) # gateway's ip address
wrpcap("srp_response.pcap", ans)

'''
# Notice that the response is saved in srp_response.pcap. There is a sample srp_response-sample.pcap present to check
# To check the file, please use tcdump -r srp_response.pcap or tcpdump -r srp_response.pcap.pcap  ## use sudo if normal tcpdump is not working
