__author__ = "Nikhil Alampalli Ramu", "Abhishek Pakrashi", "Raghunath Kulkarni"
__email__ = "nalampal@cisco.com", "apakrash@cisco.com", "raghukul@cisco.com"
__status__ = "beta testing"


import sys
import os
import json
import datetime
import re
from pprint import pprint
from subprocess import *

def export_to_txt(f_name, txt_f_name):
    cmd = """tshark -T json -r %s > %s""" % (f_name, txt_f_name)
    check_call(cmd, shell=True)
    #os.system(cmd)

def time_delay(in_j,out_j):
    print('PacketIndex,IP_ID, IngressTime,EgressTime,FirewallProcessingTime,CumulativeDelayByFirewall')
    packets={}
    for i in in_j:
        a=datetime.datetime.strptime(re.findall(r"\w{3}\s+\d{1,2}, \d{4} \d{2}:\d{2}:\d{2}.\d{6}",i["_source"]["layers"]["frame"]["frame.time"])[0], "%b %d, %Y %H:%M:%S.%f")
        packets[i["_source"]["layers"]["ip"]['ip.id']]={}
        packets[i["_source"]["layers"]["ip"]['ip.id']]['in_time']=a
        
    for i in out_j:
        a=datetime.datetime.strptime(re.findall(r"\w{3}\s+\d{1,2}, \d{4} \d{2}:\d{2}:\d{2}.\d{6}",i["_source"]["layers"]["frame"]["frame.time"])[0], "%b %d, %Y %H:%M:%S.%f")
        if i["_source"]["layers"]["ip"]['ip.id']  in packets:
            packets[i["_source"]["layers"]["ip"]['ip.id']]['out_time']=a
        else:
            packets[i["_source"]["layers"]["ip"]['ip.id']]={}
            packets[i["_source"]["layers"]["ip"]['ip.id']]['out_time']=a
    time_delta=[]
    b=[]
    index = 1 #starts at 1 to match the index of the pcap files
    
    #pprint(packets)
    for i in packets:
        if 'in_time' in packets[i] and 'out_time' in packets[i]:
            a=(packets[i]['out_time']-packets[i]['in_time']).total_seconds()*1000
            if a < 0:
                a = a * -1
            b.append(a)
            if(a>=0.0):
                time_delta.append(a)
#         print(str(index) + ',' + str(i) + ',' + str(packets[i]['in_time'])  + ',' + str(packets[i]['out_time']) + ',' + str(a) + ',' + str(sum(b)))
        index += 1
    #print(b)
    pprint(packets)
    print('\nThe total delay introduced by the device is ' + str(sum(b)) + ' x 10^-6 seconds\n\n')
    #print(time_delta)
    avg_delay  = sum(time_delta)/len(time_delta)
    print('The average delay introduced by the device is ' + str(avg_delay) + ' x 10^-6 seconds\n\n\n')


if __name__ == '__main__':
    ingress = sys.argv[1]
    egress = sys.argv[2]
    export_to_txt(ingress,"ingress.txt")
    export_to_txt(egress,"egress.txt")
    f = open("ingress.txt", "r")
    in_json=json.loads(f.read())
    f = open("egress.txt", "r")
    out_json=json.loads(f.read())
    time_delay(in_json,out_json)
#     time_delay(out_json,in_json)
    os.remove("ingress.txt")
    os.remove("egress.txt")
    
    #return '\nPlease scroll to the bottom for the total latency output'
