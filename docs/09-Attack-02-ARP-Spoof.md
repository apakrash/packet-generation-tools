# Attack/Test your network

<p align="left">
<img src="https://user-images.githubusercontent.com/17419002/171995583-fd060cfa-c17a-40f9-8f25-58006e7e06b5.png" width="40%" height="40%" />
</p>


## ARP Spoof

L2 attacks are not un-common in the network. Poisoning the ARP cache of a client for an attacker to be sent all packets to the attacker. With scapy it is incredibly simple to execute this attack.

## Run the code

### Terminal 1
On one terminal, run the tcpdump command using:

```
tcpdump -nn -s0 arp | grep 1.1.1.1
```

or if the above throws an error/permission issue:

```
sudo tcpdump -nn -s0 arp | grep 1.1.1.1
```

### Terminal 2

On another termninal, run the code:

```
python3 scapy-10-arp-cache-poisoning.py
```

or if the above throws an error/permission issue:

```
sudo python3 scapy-10-arp-cache-poisoning.py
```


## Sample Output:


#### [PYTHON]
```
$ sudo python3 scapy-10-arp-cache-poisoning.py

This will show the default packet with source ip and mac of the client.


###[ ARP ]###
  hwtype    = 0x1
  ptype     = IPv4
  hwlen     = None
  plen      = None
  op        = who-has
  hwsrc     = 00:50:56:bd:05:0a
  psrc      = 10.105.130.21
  hwdst     = 00:00:00:00:00:00
  pdst      = 0.0.0.0

-------------------
Notice the change in ARP code, i.e. op from who-has to is-at


###[ ARP ]###
  hwtype    = 0x1
  ptype     = IPv4
  hwlen     = None
  plen      = None
  op        = is-at
  hwsrc     = 00:50:56:bd:05:0a
  psrc      = 10.105.130.21
  hwdst     = 00:00:00:00:00:00
  pdst      = 0.0.0.0

-------------------
Notice the change in other fields of ARP


###[ ARP ]###
  hwtype    = 0x1
  ptype     = IPv4
  hwlen     = None
  plen      = None
  op        = is-at
  hwsrc     = 11:11:11:11:11:11
  psrc      = 1.1.1.1
  hwdst     = 22:22:22:22:22:22
  pdst      = 2.2.2.2

.
Sent 1 packets.
```

#### [TCPDUMP]

It takes a few seconds to show up the packets depending how much arp packets are coming to the box.

```
$ sudo tcpdump -nn -s0 arp | grep 1.1.1.1
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on ens192, link-type EN10MB (Ethernet), capture size 262144 bytes
04:56:29.792206 ARP, Reply 1.1.1.1 is-at 11:11:11:11:11:11, length 28
```

## Observation

This attack needs to be performed with sniffer and will be effective only if the attack packets reach after the original host replies overwriting the actual ip-mac binding on the target computer.

# Next
Click Here: [ARP Spoof Attack](09-Attack-02-ARP-Spoof.md)
