#this is not working


from urllib import response
from scapy.all import scapy
from scapy.all import IP
from scapy.all import ICMP
from scapy.all import *
ip='10.197.225.120'
subnet = '10.197.224.0/23'

#ans, unans = sr( IP(dst='10.197.225.120/32')/TCP(dport=443,flags="S") )
#ans.summary( lambda s,r : r.sprintf("%IP.src% is alive") )

'''

Sample output

10.197.225.120 is alive

'''

ans, unans = sr( IP(dst='info.cern.ch')/TCP(dport=443,flags="S") )
print(ans.summary(lambda s,r : r.sprintf("%IP.src% is alive")))


'''
Sample Output

188.184.21.108 is alive

'''