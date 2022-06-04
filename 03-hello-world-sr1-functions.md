![image](https://user-images.githubusercontent.com/17419002/171995490-aa393b55-b0c8-4003-a0ea-b1fcbfa49809.png)


### `sr1()`

The sr1() function for getting 1 response packet back

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
python3 scapy-1-2-sr1.py
```

or if the above throws an error/permission issue:

```
sudo python3 scapy-1-2-sr1.py
```


## Sample Output:


#### [PYTHON]
```
$ sudo python3 scapy-1-2-sr1.py
[sudo] password for ubuntu02:
Begin emission:
Finished sending 1 packets.
..*
Received 3 packets, got 1 answers, remaining 0 packets
IP / ICMP 1.1.1.1 > 10.105.130.21 echo-reply 0 / Padding

```


#### [TCPDUMP]

```
$ sudo tcpdump -nni ens192 -s0 host 1.1.1.1
[sudo] password for ubuntu02:
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on ens192, link-type EN10MB (Ethernet), capture size 262144 bytes

17:18:09.644199 IP 10.105.130.21 > 1.1.1.1: ICMP echo request, id 0, seq 0, length 8
17:18:09.646935 IP 1.1.1.1 > 10.105.130.21: ICMP echo reply, id 0, seq 0, length 8
```

### Saving captures with scapy

```
response_sr1 = sr1(IP(dst="1.1.1.1")/ICMP())
print(response_sr1.summary())
wrpcap("response_sr1.pcap", response_sr1)
```

`wrpcap("response_sr1.pcap", response_sr1)` saves packets recevied. For reference, a sample packet is saved in the repo: `response_sr1.pcap`.
To review the file, use the command:
```
tcpdump -r response_sr1.pcap
```

# Next
Click Here: [Scapy Basics | srloop()](04-hello-world-srloop.md)
