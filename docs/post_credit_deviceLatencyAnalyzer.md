# [DIY] Latency introduced by a device

![image](https://user-images.githubusercontent.com/17419002/173512743-0f08e2d6-930f-44aa-bf26-55f9747d7c14.png)

This code takes input the ingress and egress packet captures and computes how much latency is introduced by the device.

## Run the code

```
python3 latencyAnalyzer.py ingress.pcap egress.pcap
```

## Sample Output

```
$ python3 latencyAnalyzer.py slow-in.pcap slow-out.pcap

<truncated>

'0x00003f4e': {'in_time': datetime.datetime(2022, 2, 19, 13, 55, 3, 637235),
                'out_time': datetime.datetime(2022, 2, 19, 13, 55, 3, 637235)},
 '0x00003f4f': {'in_time': datetime.datetime(2022, 2, 19, 13, 55, 3, 639569),
                'out_time': datetime.datetime(2022, 2, 19, 13, 55, 3, 639569)}}

The total delay introduced by the device is 20.36600000000018 x 10^-6 seconds
The average delay introduced by the device is 0.004423544743701169 x 10^-6 seconds
```
