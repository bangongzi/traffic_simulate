#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import time
import thread
from collections import deque
fancy_loading1 = deque('>--------------------')
fancy_loading2 = deque('*--------------------')

def run_horse( fancy ):
    while True:
        print '\r%s' % ''.join(fancy),
        fancy.rotate(1)
        sys.stdout.flush()
        time.sleep(0.08)

def output_txt( fname , step ):
	file = open(fname,"w")
	i = 0
	for j in range(10):
		i += step
		file.write("\n")
		file.write(str(i))
		time.sleep( 0.1 )
	print "The %s is made" %fname

"""try:
    thread.start_new_thread( run_horse, (fancy_loading1, ) )
    thread.start_new_thread( run_horse, (fancy_loading2, ) )
except:
    print "Error: unable to start thread"
else:
    print "It worked!"""
	
try:
    thread.start_new_thread(output_txt,("1.txt",1))
    thread.start_new_thread(output_txt,("2.txt",2))
except:
    print "Error: unable to start thread"
else:
    print "It worked!"

while 1:
    pass


import thread
import time
import random

alpha = 1.5
for i in range(10):
    print random.paretovariate(alpha)