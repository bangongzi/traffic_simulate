#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
import sys
import os
import time

#file = open('traffic_rough.txt','a+')
times = 3000
print "The test starts at:",time.strftime('%Y-%m-%d %H:%M:%S')
a = time.time()
for i in range(times):
	os.system("echo NewStart %.5f >> /home/per/log/traffic_rough.txt"%(time.time()))
	os.system("ifconfig |grep -E 'mtu|packet'>> /home/per/log/traffic_rough.txt")
	time.sleep(0.0415)
print "The test ends at:",time.strftime('%Y-%m-%d %H:%M:%S')
b = time.time()
print "The mean time to read data is %.5fs" %((b-a)/times)