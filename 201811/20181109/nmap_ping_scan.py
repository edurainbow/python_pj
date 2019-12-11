#__author:"Peter"
#date:2019/2/3

#!/usr/bin/python3
# -*- coding=utf-8 -*-

#import nmap
#import sys
def nmap_ping_scan(network_prefix):
    nm = nmap.PortScanner()
    ping_scan_raw_result = nm.scan(hosts=network_prefix, arguments='-v -n -sn')
    host_list = []
    for Result in ping_scan_raw_result['scan'].values():
        if Result['status']['stats'] == 'up':
            host_list.append(Result['addresses']['ipv4'])
    return host_list
if __name__ == '__main__':
   for host in nmap_ping_scan(sys.argv[1]):
       print('%-20s %5s' % (host,'is UP'))