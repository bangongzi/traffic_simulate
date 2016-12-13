#!/usr/bin/python
# -*- coding: UTF-8 -*-

from __future__ import division
import sys

def pkt_read( filename,snum ):
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
        if line.find("s"+snum+'-') == -1:
            pass
        else:
            j += 1       
            if j == 1: 
                str0 = line[40:59]
                transmit_sum[i] += int(str0)
            else:
                str0 = line[14:28]
                receive_sum[i] += int(str0)
    ReceivePkt = receive_sum[i] - receive_sum[i-1]
    TransminPkt = transmit_sum[i] - transmit_sum[i-1]
    file.close()
    return (ReceivePkt,TransminPkt)

def switch_read( snum='101' ):
    filename = "interfaces.txt" 
    ReceivePkt,TransminPkt = pkt_read( filename,snum )
    rate = (ReceivePkt - TransminPkt) / ReceivePkt
    print "switch s%s receive %d pkts,send %d pkts,so loss rate is: %f" % (snum,ReceivePkt,TransminPkt,rate)

if len(sys.argv) == 1:
    switch_read( '101')
    switch_read( '201')
    switch_read( '301')
    switch_read( '305')
elif len(sys.argv) == 2:
    switch_read( sys.argv[1] )
else:
    print "Invalid number of parameters.\nThe right form is ./measure_loss_rate.py 101(switch number)"
#switch_read( '1' )