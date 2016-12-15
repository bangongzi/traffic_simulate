#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
import sys

def load_get( bandwdth=10,test_time=15,snum='101'):
    filename = "ifconfig.txt"
    file = open(filename,"r")
    traffic = []
    while 1:
        line = file.readline()
        if not line:
            break
        if line.find('s'+snum+'-eth1:') == -1:
            pass
        else:
            for i in range(5):
                line = file.readline()
            a = line.find("bytes")
            b = line.find("(")
            traffic.append(float(line[a+5:b]))
    data = (traffic[-1]-traffic[-2])/1000000000
    rate = (data*8)/test_time
    load = rate/bandwdth
    file.close()
    print "The average speed is %.2fGbit/s,the bandwidth is %.2fGbit/s,the load of s%s is %.4f" %( rate,bandwdth,snum,load )

band_array = [ 4.5,2.25,0.45 ]
if len(sys.argv) == 1:
    load_get(bandwdth=band_array[0],snum='101')
    load_get(bandwdth=band_array[1],snum='201')
    load_get(bandwdth=band_array[2],snum='301')
#    load_get(bandwdth=10,snum='1')
elif len(sys.argv) == 2:
    load_get(bandwdth=band_array[0],test_time=float(sys.argv[1]),snum='101')
    load_get(bandwdth=band_array[1],test_time=float(sys.argv[1]),snum='201')
    load_get(bandwdth=band_array[2],test_time=float(sys.argv[1]),snum='301')
    load_get(bandwdth=band_array[2],test_time=float(sys.argv[1]),snum='306')
#    load_get(bandwdth=10,test_time=float(sys.argv[1]),snum='1')
else:
    print "Invalid number of parameters.\nThe right form is ./load_s1.py 15(s,test_time)"