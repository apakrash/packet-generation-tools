# Attack/Test your network

![image](https://wwwin-github.cisco.com/storage/user/37778/files/c4565185-cf0b-4108-81dd-b9d24d1bff71)

## Malformed Packet

`IP Null Payload Attack` `LAND Attack` `Smurf Attack` `Nestea/Teardrop Attack`

Check how your network handles malformed packet. For demonstrating we will try to recreate [Nestea/Teardrop](https://community.cisco.com/t5/security-documents/how-to-configure-the-router-to-minimize-a-denial-of-service-dos/ta-p/3117624) attack by sending malformed packets (to a hopefully non-existent host on the network)

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
tcpdump -nni ens192 -s0 host 192.168.1.100
```

or if the above throws an error/permission issue:

```
sudo tcpdump -nni ens192 -s0 host 192.168.1.100
```

### Terminal 2

On another termninal, run the code:

```
python3 scapy-7-1-malformed-packet.py
```

or if the above throws an error/permission issue:

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
$ sudo tcpdump -nni ens192 -s0 host 192.168.1.100
[sudo] password for ubuntu02:
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on ens192, link-type EN10MB (Ethernet), capture size 262144 bytes
14:33:14.156265 IP 10.105.130.21.53 > 192.168.1.100.53: domain [length 10 < 12] (invalid)
14:33:14.188779 IP 10.105.130.21 > 192.168.1.100: ip-proto-0
14:33:14.221228 IP 10.105.130.21.53 > 192.168.1.100.53: 22616 updateDA% [b2&3=0x5858] [22616a] [22616q] [22616n] [22616au][|domain]
```

## Observation

Notice the how tcpdump shows that the packet contains invalid/malformed information.

# Next
Click Here: [ARP Spoof Attack](09-Attack-02-ARP-Spoof.md)
