# Hello world of Scapy!

<p align="left">
<img src="https://user-images.githubusercontent.com/17419002/171995490-aa393b55-b0c8-4003-a0ea-b1fcbfa49809.png" width="40%" height="40%" />
</p>

### `srloop()`

As the name gives it away, send a packet at layer 3 in loop after each response is received. 

What do you think is the difference between running srloop() and running sr() or sr1() multiple times? 

`srloop` sends the same packet over and over, while `sr`/`sr1` packets can be changed with each loop. 

<p></p>

`srloop(IP(dst="1.1.1.1")/ICMP(), count=2)` is the syntax to send `ICMP` packets, twice to `1.1.1`

## Run the code

### Terminal 1
On one terminal, run the tcpdump command using:

```
sudo tcpdump -nn -s0 host 1.1.1.1
```

### Terminal 2

On another termninal, run the code:

```
sudo python3 scapy-1-3-srloop.py
```


## Sample Output:


#### [PYTHON]
```
$ sudo python3 scapy-1-3-srloop.py
RECV 1: IP / ICMP 1.1.1.1 > 10.105.130.21 echo-reply 0 / Padding
RECV 1: IP / ICMP 1.1.1.1 > 10.105.130.21 echo-reply 0 / Padding

Sent 2 packets, received 2 packets. 100.0% hits.
(<Results: TCP:0 UDP:0 ICMP:2 Other:0>, <PacketList: TCP:0 UDP:0 ICMP:0 Other:0>)

```


#### [TCPDUMP]

```
$ sudo tcpdump -nn -s0 host 1.1.1.1
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on ens192, link-type EN10MB (Ethernet), capture size 262144 bytes
17:22:31.340313 IP 10.105.130.21 > 1.1.1.1: ICMP echo request, id 0, seq 0, length 8
17:22:31.342917 IP 1.1.1.1 > 10.105.130.21: ICMP echo reply, id 0, seq 0, length 8
17:22:32.305151 IP 10.105.130.21 > 1.1.1.1: ICMP echo request, id 0, seq 0, length 8
17:22:32.307671 IP 1.1.1.1 > 10.105.130.21: ICMP echo reply, id 0, seq 0, length 8
```
# Next
Click Here: [Executing Network Reconnaissance](05-Reconn-the-network-1-syn-scan.md)
