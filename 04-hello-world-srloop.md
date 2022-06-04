# Hello world of Scapy!

![image](https://user-images.githubusercontent.com/17419002/171995490-aa393b55-b0c8-4003-a0ea-b1fcbfa49809.png)


### `srloop()`

As the name gives it away, send a packet at layer 3 in loop and print the answer each time. What do you think is the difference between running srloop() and running sr() or sr1() multiple times?

Please notice that here ICMP() is the protocol being used, similarly we will see other protocols' usage later in the session.

## Run the code

### Terminal 1
On one terminal, please find the interface being used by your machine/docker image using:
```
ip a s
```
```
1: ens192: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    link/ether 00:50:56:bd:05:0a brd ff:ff:ff:ff:ff:ff
    altname enp11s0
    inet 10.105.130.21/24 brd 10.105.130.255 scope global noprefixroute ens192
       valid_lft forever preferred_lft forever
    inet6 fe80::eaf4:d84d:8cca:dbe6/64 scope link noprefixroute
       valid_lft forever preferred_lft forever
```

Here the interface is `ens192`.

Now run the tcpdump command using:

```
tcpdump -nni ens192 -s0 host 1.1.1.1
```

or if the above throws an error/permission issue:

```
sudo tcpdump -nni ens192 -s0 host 1.1.1.1
```

### Terminal 2

On another termninal, run the code:

```
python3 scapy-1-3-srloop.py
```

or if the above throws an error/permission issue:

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
$ sudo tcpdump -nni ens192 -s0 host 1.1.1.1
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on ens192, link-type EN10MB (Ethernet), capture size 262144 bytes
17:22:31.340313 IP 10.105.130.21 > 1.1.1.1: ICMP echo request, id 0, seq 0, length 8
17:22:31.342917 IP 1.1.1.1 > 10.105.130.21: ICMP echo reply, id 0, seq 0, length 8
17:22:32.305151 IP 10.105.130.21 > 1.1.1.1: ICMP echo request, id 0, seq 0, length 8
17:22:32.307671 IP 1.1.1.1 > 10.105.130.21: ICMP echo reply, id 0, seq 0, length 8
```
# Next
Click Here: [Executing Network Reconnaissance](05-Reconn-the-network-1-syn-scan.md)
