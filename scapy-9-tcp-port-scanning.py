# TCP port scanning
# Running on ubuntu server
# Pending on LL2.0

from urllib import response
#from async_timeout import timeout
from scapy.all import scapy
from scapy.all import IP
from scapy.all import ICMP
from scapy.all import *
cern = '188.184.21.108'
ip='10.197.225.120'

subnet = '10.197.224.0/23'


response, unans = sr( IP(dst=cern) /TCP(flags="S", dport=(440,443)) )
wrpcap('synScan.pcap', response)

#If the above keeps on going, hitting Ctrl+C will stop the scan and the packets to the pcap file
#Read the pcap file with tcpdump -r filename.pcap


''' Sample Output

sudo python3 scapy-9-tcp-port-scanning.py
Begin emission:
21:17:54.528373 IP 10.105.130.21.20 > 10.197.225.120.440: Flags [S], seq 0, win 8192, length 0
21:17:54.529425 IP 10.105.130.21.20 > 10.197.225.120.441: Flags [S], seq 0, win 8192, length 0
21:17:54.530453 IP 10.105.130.21.20 > 10.197.225.120.442: Flags [S], seq 0, win 8192, length 0
Finished sending 4 packets.
21:17:54.531468 IP 10.105.130.21.20 > 10.197.225.120.443: Flags [S], seq 0, win 8192, length 0
21:17:54.531803 IP 10.197.225.120.443 > 10.105.130.21.20: Flags [S.], seq 3741066228, ack 1, win 29200, options [mss 1460], length 0
21:17:54.531836 IP 10.105.130.21.20 > 10.197.225.120.443: Flags [R], seq 1, win 0, length 0
.*....................................................^C
Received 54 packets, got 1 answers, remaining 3 packets


tcpdump -r synScan.pcap
reading from file synScan.pcap, link-type IPV4 (Raw IPv4)
21:17:54.531456 IP bgl14-1-g06-n7k-2.cisco.com.ftp-data > 10.197.225.120.https: Flags [S], seq 0, win 8192, length 0
21:17:54.531803 IP 10.197.225.120.https > bgl14-1-g06-n7k-2.cisco.com.ftp-data: Flags [S.], seq 3741066228, ack 1, win 29200, options [mss 1460], length 0



'''