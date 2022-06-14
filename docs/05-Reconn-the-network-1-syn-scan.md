# Recon

![image](https://user-images.githubusercontent.com/17419002/171995537-a7d0aeb8-b0cf-4bc6-89c5-c725e0cb384e.png)
 
 <sub>Credits:Unsplash.com</sub>

## SYN SCAN

One we have seen how to send packets, lets dive into how to use scapy to scan your network in a matter of a few lines:

[For this, we will use the ipaddress module: https://docs.python.org/3/library/ipaddress.html#module-ipaddress]

`sr1(IP(dst=ip)/TCP(dport=443,flags="S"))` is used to send a syn packet, notice how the tcp flags can be controlled with this. Changing the ip address on each iteration in `dst` lets you scan the entire subnet with this line.


## Run the code

### Terminal 1
On one terminal, run the tcpdump command using:

```
sudo tcpdump -nn -s0  net 1.1.1.0/24
```

### Terminal 2

On another termninal, run the code:

```
sudo python3 scapy-4-syn-scan.py
```


## Sample Output:


#### [PYTHON]
```
$ sudo python3 scapy-4-syn-scan.py
[sudo] password for ubuntu02:
1.1.1.1
<class 'str'>
16843009
TCP SYN scap for 1.1.1.1
Begin emission:
Finished sending 1 packets.
....*
Received 5 packets, got 1 answers, remaining 0 packets
###[ IP ]###
  version   = 4
  ihl       = 5
  tos       = 0x0
  len       = 44
  id        = 0
  flags     = DF
  frag      = 0
  ttl       = 47
  proto     = tcp
  chksum    = 0xbd4c
  src       = 1.1.1.1
  dst       = 10.105.130.21
  \options   \
###[ TCP ]###
     sport     = https
     dport     = ftp_data
     seq       = 1079241411
     ack       = 1
     dataofs   = 6
     reserved  = 0
     flags     = SA
     window    = 65535
     chksum    = 0xdcff
     urgptr    = 0
     options   = [('MSS', 1380)]
###[ Padding ]###
        load      = '\x00\x00'

[repeats for 1.1.1.2 and so on]

```


#### [TCPDUMP]

```
$ sudo tcpdump -nn -s0  net 1.1.1.0/24
[sudo] password for ubuntu02:
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on ens192, link-type EN10MB (Ethernet), capture size 262144 bytes
20:34:14.136501 IP 10.105.130.21.20 > 1.1.1.1.443: Flags [S], seq 0, win 8192, length 0
20:34:14.139575 IP 1.1.1.1.443 > 10.105.130.21.20: Flags [S.], seq 1079241411, ack 1, win 65535, options [mss 1380], length 0
20:34:14.139620 IP 10.105.130.21.20 > 1.1.1.1.443: Flags [R], seq 1, win 0, length 0
20:34:14.190055 IP 10.105.130.21.20 > 1.1.1.2.443: Flags [S], seq 0, win 8192, length 0
20:34:14.193960 IP 1.1.1.2.443 > 10.105.130.21.20: Flags [S.], seq 1101331286, ack 1, win 65535, options [mss 1380], length 0
20:34:14.194006 IP 10.105.130.21.20 > 1.1.1.2.443: Flags [R], seq 1, win 0, length 0
20:34:14.245419 IP 10.105.130.21.20 > 1.1.1.3.443: Flags [S], seq 0, win 8192, length 0
20:34:14.248235 IP 1.1.1.3.443 > 10.105.130.21.20: Flags [S.], seq 2059684752, ack 1, win 65535, options [mss 1380], length 0
20:34:14.248271 IP 10.105.130.21.20 > 1.1.1.3.443: Flags [R], seq 1, win 0, length 0
20:34:14.298039 IP 10.105.130.21.20 > 1.1.1.4.443: Flags [S], seq 0, win 8192, length 0
20:34:14.301458 IP 1.1.1.4.443 > 10.105.130.21.20: Flags [S.], seq 4145010479, ack 1, win 65535, options [mss 1380], length 0


20:34:14.301492 IP 10.105.130.21.20 > 1.1.1.4.443: Flags [R], seq 1, win 0, length 0
20:34:14.338512 IP 10.105.130.21.20 > 1.1.1.5.443: Flags [S], seq 0, win 8192, length 0
20:34:14.341698 IP 1.1.1.5.443 > 10.105.130.21.20: Flags [S.], seq 3800543199, ack 1, win 65535, options [mss 1380], length 0
20:34:14.341777 IP 10.105.130.21.20 > 1.1.1.5.443: Flags [R], seq 1, win 0, length 0
```

## Observation

Notice how the `[S.]` i.e. SYN ACK packet shows that the TCP port is open on that ip address.


# Next
Click Here: [Recon | ACK Scan](06-Reconn-the-network-2-ack-scan.md)
