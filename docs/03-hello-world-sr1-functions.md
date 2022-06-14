# Hello world of Scapy!

<p align="left">
<img src="https://user-images.githubusercontent.com/17419002/171995490-aa393b55-b0c8-4003-a0ea-b1fcbfa49809.png" width="40%" height="40%" />
  
  <sub>Credits:Unsplash.com</sub>

</p>

### `sr1()`

The sr1() function returns **1 response packet** back

The syntax remain the same as `sr()`, the name of te function changes to `sr1()`

## Run the code

### Terminal 1
On one terminal, run the tcpdump command using:

```
sudo tcpdump -nn -s0 host 1.1.1.1
```

### Terminal 2

On another termninal, check the code:

```
cat scapy-1-2-sr1.py
```

Thereafter, run the code:

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
$ sudo tcpdump -nn -s0 host 1.1.1.1
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

There is a sample file saved from the lab [in case the code did not run]:

```
tcpdump -r response_sr1-sample.pcap
```

# Next
Click Here: [Scapy Basics | srloop()](04-hello-world-srloop.md)
