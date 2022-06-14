# Attack/Test your network

<p align="left">
<img src="https://user-images.githubusercontent.com/17419002/171995583-fd060cfa-c17a-40f9-8f25-58006e7e06b5.png" width="40%" height="40%" />
  
<sub>Image Credit: dev.to</sub>
</p>


## Malformed Packet

`IP Null Payload Attack` `LAND Attack` `Smurf Attack` `Nestea/Teardrop Attack`

Check how your network handles malformed packet. For demonstrating we will try to recreate [Nestea/Teardrop](https://community.cisco.com/t5/security-documents/how-to-configure-the-router-to-minimize-a-denial-of-service-dos/ta-p/3117624) attack by sending malformed packets (to a hopefully non-existent host on the network)

`send()` is method of Python's socket class which is used to send data from one socket to another socket. | [send()|Python Docs](https://docs.python.org/3/library/socket.html)

## Run the code

### Terminal 1
On one terminal, run the tcpdump command using:

```
sudo tcpdump -nn -s0 host 192.168.1.100
```

### Terminal 2

On another termninal, run the code:

```
sudo python3 scapy-7-1-malformed-packet.py
```


## Sample Output:


#### [PYTHON]
```
$ sudo python3 scapy-7-1-malformed-packet.py
[sudo] password for ubuntu02:
.
Sent 1 packets.
.
Sent 1 packets.
.
Sent 1 packets.
```

#### [TCPDUMP]

```
$ sudo tcpdump -nn -s0 host 192.168.1.100
[sudo] password for ubuntu02:
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on ens192, link-type EN10MB (Ethernet), capture size 262144 bytes
14:33:14.156265 IP 10.105.130.21.53 > 192.168.1.100.53: domain [length 10 < 12] (invalid)
14:33:14.188779 IP 10.105.130.21 > 192.168.1.100: ip-proto-0
14:33:14.221228 IP 10.105.130.21.53 > 192.168.1.100.53: 22616 updateDA% [b2&3=0x5858] [22616a] [22616q] [22616n] [22616au][|domain]
```

## Observation

Notice the how tcpdump shows that the packet contains invalid/malformed information.

# Next | [ARP Spoof Attack](09-Attack-02-ARP-Spoof.md)
