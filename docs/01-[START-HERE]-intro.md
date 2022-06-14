# Introduction

Packet generation has been there in networking for a long time and with the advent of cloud computing, Infrastructure as Code, CI/CD pipelines, automating packet generation for network audit and resiliency testing need has increased more than ever.

Although there is off-the-shelf software available for traffic generation, they incorporate a massive technical debt for learning and implementing a custom solution. In comparison open-source tools are very easy to learn, incorporate in your daily automation pipeline, or just plainly generate packets.


So, craft away.

![image](https://user-images.githubusercontent.com/17419002/171995471-e66806d4-5993-4b4a-bae4-9a9d4100a9d9.png)
<sub>Image Credit: Marvel.com</sub>

## Prerequisites

`Scapy`, `Tshark`, `nmap`, `arpspoof`, `arp-sk`, `arping`, `tcpdump`, `wireshark`, `p0f`, `pypacker`, `Zeek`, `iperf`, (never ending list) are a few of tools that are completely free and immensely effective for sniffing/crafting packets.

For the scope of this session we will use `python` and `scapy` to demonstrate the might of packet creation, while using other tools that have similar functionality.
We will install all that is necessary in the next step.

## Experience of the Session
There will be three stages:
         
* Understanding the fundamentals of Scapy | What is it? | How do I run it
* Network Reconnaissance | First Steps to fortify the network!
* Network Attacks | The good stuff :)

Whenever sending a crafted packet, there will be `tcpdump commands`  shared with the code snippets, please run them on another console/cmd session parallelly to experience the packet flow in real time. A corporally to this is whenever possible, the packets are saved and use `tcpdump -r filename.pcap` to check the captured packets.

Wherever possible, there are samples presented of the captures taken in a lab setting for your reference
	
Happy crafting.

# Next
Click Here: [Setup your environment](01.5-environment-setup.md)
