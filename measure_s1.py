#!/usr/bin/python
# -*- coding: UTF-8 -*-

from __future__ import division
import sys

filename = "interfaces.txt"
file = open(filename,"r")
receive_sum = [];
transmit_sum = [];
i = j = -1
while 1:
    line = file.readline()
    if not line:
	    break
    if line.find("Kernel") == -1:
	    pass
    else:
        receive_sum.append(0)
        transmit_sum.append(0)
        i = i + 1
        j = 0
    if line.find("s1-") == -1:
        pass
    else:
        j += 1
        if j <= 100:
            str0 = line[16:29]
            receive_sum[i] += int(str0)
        else: 
            str0 = line[41:59]
            transmit_sum[i] += int(str0)
ReceivePkt = receive_sum[i] - receive_sum[i-1]
TransminPkt = transmit_sum[i] - transmit_sum[i-1]
rate = (ReceivePkt - TransminPkt) / ReceivePkt
print "receive %d,send %d,so loss rate is: %f" % (ReceivePkt,TransminPkt,rate)
