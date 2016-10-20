#!/usr/bin/python
# -*- coding: UTF-8 -*-

from __future__ import division
import sys
#from mininet.log import info, error, debug, output, warn

def readtxt( fname,marker ):
	file = open(fname,"r")
	count = []
	while 1:
		line = file.readline()
		if not line:
			break
		if line.find(marker) == -1:
			pass
		else:
			i=line.find(marker)-1
			str0 = line[4:i]
			count.append(int(str0))
	WantedPkt = count[-1] - count[-2]
	file.close()
	return WantedPkt

def data_process(sender=100,receiver=1):
	SendPkt = 0
	ReceivePkt = 0
	for i in xrange(1,sender+1):
		fname ='h' + str(i) +'netstat.txt'
		marker = "segments send out"
		SendPkt += readtxt( fname , marker )
	for i in xrange(sender+1,sender+receiver+1):
		fname ='h' + str(i) +'netstat.txt'
		marker = "segments received\n"
		ReceivePkt = readtxt( fname,marker )
	print "SendPkt,ReceivePkt",SendPkt,ReceivePkt

if len(sys.argv) == 1:
	data_process()
elif len(sys.argv) == 3:
	data_process( int(sys.argv[1]),right = int(sys.argv[2]) )
else:
	print "Invalid number of parameters.\nThe right form is ./data_process 100(sender) 1(receiver)"