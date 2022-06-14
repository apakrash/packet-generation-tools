# Recon [Continued]

![image](https://user-images.githubusercontent.com/17419002/171995552-c169c00b-54b4-4cbc-8894-f6804cc5bdce.png)

<sub>Image Credit: cyberhoot.com/</sub>



## ARP Ping

Doing L2 Scans are possible with scapy. `srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst="1.1.1.1/32"), timeout=2)` is used to check for the MAC address for which packet destined to `1.1.1.1` should be sent.


## Run the code

### Terminal 1
On one terminal, run tcpdump:

```
sudo tcpdump -nn -s0 arp
```

### Terminal 2

On another termninal, run the code:

```
sudo python3 scapy-6-ARP-ping.py
```

## Sample Output:


#### [PYTHON]
```
$ sudo python3 scapy-6-ARP-ping.py
[sudo] password for ubuntu02:
Begin emission:
Finished sending 1 packets.
*
Received 1 packets, got 1 answers, remaining 0 packets
6c:41:6a:c7:b8:ff 1.1.1.1
```

#### [TCPDUMP]

```
$ sudo tcpdump -nn -s0 arp 
[sudo] password for ubuntu02:
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on ens192, link-type EN10MB (Ethernet), capture size 262144 bytes
11:38:34.620773 ARP, Request who-has 1.1.1.1 tell 10.105.130.21, length 28
11:38:34.621472 ARP, Reply 1.1.1.1 is-at 6c:41:6a:c7:b8:ff, length 46
```

## Observation

Use any ip address in the local network/broadcast domain to get a valid answer. To verify the arp table on the device, use `arp -a`
Also notice that scapy is not intuitive to arp for the default gateway if the ip address is not in the same subnet.

### Sample Output
```
$ arp -a
_gateway (10.105.130.1) at 6c:41:6a:c7:b8:ff [ether] on ens192
```

# Alternative tools | 1

`nping`/`nmap` is a popular tool being used for achieving the same functionality.

### Terminal 1
On one terminal, run tcpdump:

```
sudo tcpdump -nn -s0  net 1.1.1.0/24
```

### Terminal 2

On another termninal, run the code:

```
sudo nping --arp-type ARP 1.1.1.1
```

## Sample Output:


#### [NMAP]
```
$ sudo nping --arp-type ARP 1.1.1.1
[sudo] password for ubuntu02:

Starting Nping 0.7.80 ( https://nmap.org/nping ) at 2022-06-04 12:25 IST
SENT (0.0240s) ARP who has 1.1.1.1? Tell 10.105.130.21
RCVD (0.0248s) ARP reply 1.1.1.1 is at 6C:41:6A:C7:B8:FF
RCVD (0.4803s) ARP reply 10.105.130.23 is at 00:50:56:BD:05:0A
SENT (1.0243s) ARP who has 1.1.1.1? Tell 10.105.130.21
RCVD (1.0278s) ARP reply 1.1.1.1 is at 6C:41:6A:C7:B8:FF
RCVD (1.7245s) ARP reply 10.105.130.22 is at 00:50:56:BD:05:0A
SENT (2.0245s) ARP who has 1.1.1.1? Tell 10.105.130.21
RCVD (2.0253s) ARP reply 1.1.1.1 is at 6C:41:6A:C7:B8:FF
RCVD (2.5407s) ARP reply 10.105.130.22 is at 00:50:56:BD:05:0A
SENT (3.0246s) ARP who has 1.1.1.1? Tell 10.105.130.21
RCVD (3.0274s) ARP reply 1.1.1.1 is at 6C:41:6A:C7:B8:FF
RCVD (3.7847s) ARP reply 10.105.130.23 is at 00:50:56:BD:05:0A
SENT (4.0251s) ARP who has 1.1.1.1? Tell 10.105.130.21
RCVD (4.0260s) ARP reply 1.1.1.1 is at 6C:41:6A:C7:B8:FF

Max rtt: N/A | Min rtt: N/A | Avg rtt: N/A
Raw packets sent: 5 (210B) | Rcvd: 9 (342B) | Lost: 0 (0.00%)
Nping done: 1 IP address pinged in 4.06 seconds
```


#### [TCPDUMP]

```
$ sudo tcpdump -nn -s0 arp 
[sudo] password for ubuntu02:
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on ens192, link-type EN10MB (Ethernet), capture size 262144 bytes
12:25:40.776216 ARP, Request who-has 1.1.1.1 tell 10.105.130.21, length 28
12:25:40.776816 ARP, Reply 1.1.1.1 is-at 6c:41:6a:c7:b8:ff, length 46
12:25:41.776418 ARP, Request who-has 1.1.1.1 tell 10.105.130.21, length 28
12:25:41.779853 ARP, Reply 1.1.1.1 is-at 6c:41:6a:c7:b8:ff, length 46
12:25:42.776561 ARP, Request who-has 1.1.1.1 tell 10.105.130.21, length 28
12:25:42.777270 ARP, Reply 1.1.1.1 is-at 6c:41:6a:c7:b8:ff, length 46
12:25:43.776752 ARP, Request who-has 1.1.1.1 tell 10.105.130.21, length 28
12:25:43.779434 ARP, Reply 1.1.1.1 is-at 6c:41:6a:c7:b8:ff, length 46
12:25:44.777223 ARP, Request who-has 1.1.1.1 tell 10.105.130.21, length 28
12:25:44.777982 ARP, Reply 1.1.1.1 is-at 6c:41:6a:c7:b8:ff, length 46
12:30:51.101219 ARP, Request who-has 10.105.130.23 tell 10.105.130.21, length 28
```

# Alternative tools | 2

`arping` is a popular tool being used for achieving the same functionality.

### Terminal 1
On one terminal, run tcpdump:

```
sudo tcpdump -nn -s0 arp 
```

### Terminal 2

On another termninal, run the code:

```
arping 1.1.1.1 -c1 -I $(route | grep '^default' | grep -o '[^ ]*$')
```

## Sample Output:


#### [ARPING]
```
$ arping 1.1.1.1 -c1 -I $(route | grep '^default' | grep -o '[^ ]*$')
arping: lookup dev: No matching interface found using getifaddrs().
arping: Unable to automatically find interface to use. Is it on the local LAN?
arping: Use -i to manually specify interface. Guessing interface ens192.
ARPING 1.1.1.1
60 bytes from 6c:41:6a:c7:b8:ff (1.1.1.1): index=0 time=573.971 usec
```

#### [TCPDUMP]

```
$ sudo tcpdump -nn -s0 arp
[sudo] password for ubuntu02:
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on ens192, link-type EN10MB (Ethernet), capture size 262144 bytes
12:54:43.212818 ARP, Request who-has 1.1.1.1 tell 10.105.130.21, length 44
12:54:43.213416 ARP, Reply 1.1.1.1 is-at 6c:41:6a:c7:b8:ff, length 46
```

# Next | [Executing Network Attacks](08-Attack-01-malformed-packet.md)
