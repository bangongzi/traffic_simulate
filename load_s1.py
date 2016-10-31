#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
import sys

def load_get( bandwdth=10,test_time=15):
    filename = "ifconfig.txt"
    file = open(filename,"r")
    traffic = []
    while 1:
        line = file.readline()
        if not line:
            break
        if line.find("s1-eth101") == -1:
            pass
        else:
            for i in range(5):
                line = file.readline()
            a = line.find("bytes")
            b = line.find("(")
            traffic.append(float(line[a+5:b]))
    ind = len(traffic)
    test_time = test_time + 0.2
    data = (traffic[ind-1]-traffic[ind-2])/1000000000
    rate = (data*8)/test_time
    load = rate/bandwdth
    print "The average speed is %.2fGbit/s,the bandwidth is %.2fGbit/s,the load is %.4f" %( rate,bandwdth,load )

if len(sys.argv) == 1:
    load_get()
elif len(sys.argv) == 3:
    load_get( bandwdth = float(sys.argv[1]),test_time = float(sys.argv[2]) ) 
else:
    print "Invalid number of parameters.\nThe right form is ./load_s1.py 15(s,test_time) 10(Gbit/s,bandwidth)"