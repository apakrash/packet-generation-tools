# Recon [Continued]

![image](https://user-images.githubusercontent.com/17419002/171995543-455fc70f-3e5d-40bb-bf26-5a284863670e.png)

## ACK Scan

In the previous instance, we used the `flags='S'` for sending out TCP syn, now just chaging this parameter, an ack scan can be done for the network using `flags='A'`
`sr1(IP(dst=ip)/TCP(dport=443,flags="S"))` is used to send a syn packet, notice how the tcp flags can be controlled with this. Changing the ip address on each iteration in `dst` lets you scan the entire subnet with this line.

## Run the code

### Terminal 1
On one terminal, run the tcpdump command using:

```
tcpdump -nn -s0  net 1.1.1.0/24
```

or if the above throws an error/permission issue:

```
sudo tcpdump -nn -s0  net 1.1.1.0/24
```

### Terminal 2

On another termninal, run the code:

```
python3 scapy-5-ack-scan.py
```

or if the above throws an error/permission issue:

```
sudo python3 scapy-5-ack-scan.py
```


## Sample Output:


#### [PYTHON]
```
$ sudo python3 scapy-5-ack-scan.py
[sudo] password for ubuntu02:
Begin emission:
Finished sending 1 packets.
.*
Received 2 packets, got 1 answers, remaining 0 packets
(<Results: TCP:1 UDP:0 ICMP:0 Other:0>, <Unanswered: TCP:0 UDP:0 ICMP:0 Other:0>)
```


#### [TCPDUMP]

```$ sudo tcpdump -nn -s0  net 1.1.1.0/24
[sudo] password for ubuntu02:
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on ens192, link-type EN10MB (Ethernet), capture size 262144 bytes

21:00:20.268304 IP 10.105.130.21.20 > 1.1.1.1.443: Flags [.], ack 3215725885, win 8192, length 0
21:00:20.268807 IP 1.1.1.1.443 > 10.105.130.21.20: Flags [R.], seq 3215725885, ack 0, win 8192, length 0
```

## Observation

Notice the `[R.]` flag showing the port is un-filtered.

# Alternative tools

`nmap` is a popular tool being used for achieving the same functionality.

### Terminal 1
On one terminal, run the tcpdump command using:

```
tcpdump -nn -s0  net 1.1.1.0/24
```

or if the above throws an error/permission issue:

```
sudo tcpdump -nn -s0  net 1.1.1.0/24
```

### Terminal 2

On another termninal, run the code:

```
nmap -sA -T4 1.1.1.1
```

or if the above throws an error/permission issue:

```
sudo nmap -sA -T4 1.1.1.1
```

`-sA` denotes ACK scan, similarly `-sS` denotes a syn scan

`-T4` is a timing template | Range is `paranoid (0)`, `sneaky (1)`, `polite (2)`, `normal (3)`, `aggressive (4)`, and `insane (5)` | `aggressive (4)` is good for broadbadn networks.

Refer: [NMAP's man page](https://linux.die.net/man/1/nmap)


## Sample Output:


#### [NMAP]
```
$ sudo nmap -sA -T4 1.1.1.1
Starting Nmap 7.80 ( https://nmap.org ) at 2022-06-02 21:42 IST
Nmap scan report for one.one.one.one (1.1.1.1)
Host is up (0.00052s latency).
Not shown: 998 filtered ports
PORT    STATE      SERVICE
80/tcp  unfiltered http
443/tcp unfiltered https
```


#### [TCPDUMP]

```
$ sudo tcpdump -nn -s0  net 1.1.1.0/24
[sudo] password for ubuntu02:
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on ens192, link-type EN10MB (Ethernet), capture size 262144 bytes

21:00:20.268304 IP 10.105.130.21.20 > 1.1.1.1.443: Flags [.], ack 3215725885, win 8192, length 0
21:00:20.268807 IP 1.1.1.1.443 > 10.105.130.21.20: Flags [R.], seq 3215725885, ack 0, win 8192, length 0
21:42:58.692704 IP 10.105.130.21 > 1.1.1.1: ICMP echo request, id 37287, seq 0, length 8
21:42:58.692744 IP 10.105.130.21.40970 > 1.1.1.1.443: Flags [S], seq 869865408, win 1024, options [mss 1460], length 0
21:42:58.692763 IP 10.105.130.21.40970 > 1.1.1.1.80: Flags [.], ack 869865408, win 1024, length 0
21:42:58.692779 IP 10.105.130.21 > 1.1.1.1: ICMP time stamp query id 52999 seq 0, length 20
21:42:58.693256 IP 1.1.1.1.80 > 10.105.130.21.40970: Flags [R.], seq 1, ack 0, win 1024, length 0
21:42:58.695580 IP 1.1.1.1.443 > 10.105.130.21.40970: Flags [S.], seq 3836754370, ack 869865409, win 65535, options [mss 1380], length 0
21:42:58.695608 IP 10.105.130.21.40970 > 1.1.1.1.443: Flags [R], seq 869865409, win 0, length 0
21:42:58.695705 IP 1.1.1.1 > 10.105.130.21: ICMP echo reply, id 37287, seq 0, length 8
21:42:58.772508 IP 10.105.130.21.41226 > 1.1.1.1.199: Flags [.], ack 2841053849, win 1024, length 0
21:42:58.772570 IP 10.105.130.21.41226 > 1.1.1.1.554: Flags [.], ack 2841053849, win 1024, length 0

[so forth for other ports]
```

# Next
Click Here: [Network Recon | ARP ping](07-Reconn-the-network-3-arp-ping.md)
