# Looking Ahead

![image](https://user-images.githubusercontent.com/17419002/173438124-2156ae02-b083-4a6c-9bf2-1c027cef77e5.png)
<sub>Image Credit: unsplash.com</sub>


## Scapy features: 
* [Sniffing](https://scapy.readthedocs.io/en/latest/usage.html#sniffing) | [Limitations and Mitigation](https://scapy.readthedocs.io/en/latest/usage.html#performance-of-scapy)
* [Replay](https://scapy.readthedocs.io/en/latest/usage.html#sending-packets) | Alternate: tcpreplay
* [OS finger printing/profiling](https://scapy.readthedocs.io/en/latest/usage.html#os-fingerprinting) | Alternate: nmap_fp, p0f | Plethora of Cisco Products |
  
## Attacks
* [VLAN hopping](https://scapy.readthedocs.io/en/latest/usage.html#vlan-hopping)
* [Wireless Frame Injection](https://scapy.readthedocs.io/en/latest/usage.html#wireless-frame-injection)

## Repos to look at:
* [SecDev Attack Repo](https://github.com/secdev/awesome-scapy)
* [Attack Repo](https://github.com/GrigorDimitrov/ScapyAttacks)
* [SSL/TLS support](https://github.com/tintinweb/scapy-ssl_tls)
* [Superset | Repo list](https://github.com/topics/scapy?o=desc&s=stars) 

## Limitations of Scapy

* Handling large number of packets simultaneously | World of Containers | Find your limit
* Partial support for certain complex protocols | Write logic in tcp/udp 

## Running other shell based tools | Python

Run all the commands from inside python | packet/output interpretation

```
import os
os.system('iperf -c 192.168.1.100 -P 4')
```

<h1 align="center">Thank you! and please submit your feedback for the session</h1>

## [Post Credit](post_credit_deviceLatencyAnalyzer.md)


