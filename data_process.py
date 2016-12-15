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
    print "The average speed is %.4fGbit/s,the bandwidth is %.4fGbit/s,the load of s%s is %.4f" %( rate,bandwdth,snum,load )
    file1.write( "The average speed is %.4fGbit/s,the bandwidth is %.4fGbit/s,the load of s%s is %.4f \n" %( rate,bandwdth,snum,load ) )

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
    return (ReceivePkt,TransminPkt)

def switch_read( snum='101' ):
    filename = "interfaces.txt" 
    ReceivePkt,TransminPkt = pkt_read( filename,snum )
    rate = (ReceivePkt - TransminPkt) / ReceivePkt
    print "switch s%s receive %d pkts,send %d pkts,so loss rate is: %f" % (snum,ReceivePkt,TransminPkt,rate)
    file1.write( "switch s%s receive %d pkts,send %d pkts,so loss rate is: %f \n" % (snum,ReceivePkt,TransminPkt,rate) )

fname = "data.txt"
file1 = open(fname,"a")
if len(sys.argv) == 5:
    file1.write("The buffer is %s:\n" %sys.argv[4])
    switch_read( sys.argv[1] )
    load_get( snum=sys.argv[1],bandwdth=float(sys.argv[2]),test_time=float(sys.argv[3]) )
else:
    print "Invalid number of parameters.\nThe right form is ./data_process.py 301(switch number) 2.4(Gbit/s,bandwidth) 15(s,test_time) 1ms(the string to give limit info)"
file1.close()