#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
import sys

sfname="mmpp_traffic_rough.txt"
ofname="mmpp_traffic_transition.txt"
snum="101"
sfile = open(sfname,"r")
ofile = open(ofname,"w")
time = packet = count = 0
while 1:
    line = sfile.readline()
    if not line:
        break
    if line.find('NewStart') == -1:
        pass
    else:
        ofile.write("%.5f   %d   a%.5f   b%d\n"%(time,packet,time,packet))
        p1=line.find('.')
        if line[(p1+1)]!='0':
            time = count + float('0'+line[p1:])
        else:
            count += 1
            time = count + float('0'+line[p1:])
        packet = 0
    if line.find('s'+snum+'-eth') == -1:
        pass
    else:
        if line.find('s'+snum+'-eth1') == -1:
            line = sfile.readline()
            a = line.find("bytes")
            b = line.find("(")
            packet += int(line[a+5:b])           
        else:
            continue           
sfile.close()
ofile.close()
