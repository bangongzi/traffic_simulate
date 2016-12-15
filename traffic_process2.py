#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
import sys

def line_process(line):
    p1=line.find('a')
    p2=line.find('b')
    time=float(line[(p1+1):p2])
    packet=int(line[(p2+1):])
    return (time,packet)

sfname="mmpp_traffic_transition.txt"
ofname="mmpp_traffic_final.txt"
sfile = open(sfname,"r")
ofile = open(ofname,"w")
line=sfile.readline()
t1=p1=0
t2,p2=line_process(line)
while 1:
    line = sfile.readline()
    if not line:
        break
    t1=t2
    p1=p2
    t2,p2=line_process(line)
    ofile.write("%.5f   %d   %f\n"%(t1,p1,( ((p2-p1)*8) / (t2-t1) ) ) )      
sfile.close()
ofile.close()
