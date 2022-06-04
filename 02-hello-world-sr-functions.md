# Hello world of Scapy!

<p align="center">
<img src="https://wwwin-github.cisco.com/storage/user/37778/files/12a5f0a1-2764-45e7-85cc-fbf2e26e2821" width="40%" height="40%">
</p>

### `sr()`

This is the heart of scapy. As the name can be seen as an acronym for send/response, this function is used for  sending packets and receiving the corresponding packets back.

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
python3 scapy-1-1-sr.py
```

or if the above throws an error/permission issue:

```
sudo python3 scapy-1-1-sr.py
```


## Sample Output:


#### [PYTHON]
```
$ sudo python3 scapy-1-1-sr.py
[sudo] password for ubuntu02:

Begin emission:
Finished sending 1 packets.
.*
Received 2 packets, got 1 answers, remaining 0 packets
(<Results: TCP:0 UDP:0 ICMP:1 Other:0>, <Unanswered: TCP:0 UDP:0 ICMP:0 Other:0>)
```


#### [TCPDUMP]

```
$ sudo tcpdump -nni ens192 -s0 host 1.1.1.1
[sudo] password for ubuntu02:
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on ens192, link-type EN10MB (Ethernet), capture size 262144 bytes


20:54:30.888203 IP 10.105.130.21 > 1.1.1.1: ICMP echo request, id 0, seq 0, length 8
20:54:30.891062 IP 1.1.1.1 > 10.105.130.21: ICMP echo reply, id 0, seq 0, length 8
```

# Next
Click Here: [Scapy Basics | sr1()](03-hello-world-sr1-functions.md)
