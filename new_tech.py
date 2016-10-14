#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import time
import thread
import random
from collections import deque

def pareto( alpha = 1.5 ):
    suma = 0
    for i in range(1000):
        t = random.paretovariate(alpha) * 25
        suma += t
        print t
    print "The expectation is %f" %(suma/1000)

pareto(1.5)

"""try:
    thread.start_new_thread( run_horse, (fancy_loading1, ) )
    thread.start_new_thread( run_horse, (fancy_loading2, ) )
except:
    print "Error: unable to start thread"
else:
    print "It worked!"""

