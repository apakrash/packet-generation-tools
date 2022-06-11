# Hello world of Scapy!


![image](https://user-images.githubusercontent.com/17419002/171995490-aa393b55-b0c8-4003-a0ea-b1fcbfa49809.png)


### `sr()`

This is the heart of scapy. As the name can be seen as an acronym for send/response, this function is used for  sending packets and receiving the corresponding packets back.

Please notice that here ICMP() is the protocol being used, similarly we will see other protocols' usage later in the session.

## Run the code

### Terminal 1
On one terminal, run the tcpdump command using:

```
tcpdump -nn -s0 host 1.1.1.1
```

or if the above throws an error/permission issue:

```
sudo tcpdump -nn -s0 host 1.1.1.1
```

### Terminal 2

On another termninal, check the code:

```
cat scapy-1-1-sr.py
```

Thereafter, run the code:

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
$ sudo tcpdump -nn -s0 host 1.1.1.1
[sudo] password for ubuntu02:
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on ens192, link-type EN10MB (Ethernet), capture size 262144 bytes


20:54:30.888203 IP 10.105.130.21 > 1.1.1.1: ICMP echo request, id 0, seq 0, length 8
20:54:30.891062 IP 1.1.1.1 > 10.105.130.21: ICMP echo reply, id 0, seq 0, length 8
```

# Next
Click Here: [Scapy Basics | sr1()](03-hello-world-sr1-functions.md)
