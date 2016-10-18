#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
import sys

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
data = (traffic[ind-1]-traffic[ind-2])/1000000000
print "The average spped is %.2fGbit/s,the bandwidth is 10Gbit/s,the load is %.4f" %( ((data*8)/15),( ( (data*8) /15 ) /10) )