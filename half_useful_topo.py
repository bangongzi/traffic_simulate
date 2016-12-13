#!/usr/bin/python
# -*- coding: UTF-8 -*-

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call



def myNetwork():

    net = Mininet( topo=None,
                   build=False,
                   ipBase='10.0.0.0/8')

    core_sw = []
    dist_sw = []
    aces_sw = []
    h = []
    core_num = 1
    dist_num = 2
    aces_num = 10
    fanout_num = 10

    info( '*** Adding controller ***\n' )
    RYU=net.addController(name='RYU',
                      controller=RemoteController,
                      ip='127.0.0.1',
                      protocol='tcp',
                      port=6633)

    info( '*** Adding switches ***\n')
    #Adding core switches
    for i in range(core_num):
        switch_name = 's10' + str( i + 1 )
        sw = net.addSwitch(switch_name, cls=OVSKernelSwitch)
        core_sw.append( sw )
    #Adding distribution switches
    for i in range(dist_num):
        switch_name = 's20' + str( i + 1 )
        sw = net.addSwitch(switch_name, cls=OVSKernelSwitch)
        dist_sw.append( sw )
    #Adding access switches
    for i in range(aces_num):
        if i <= 8:
            switch_name = 's30' + str( i + 1 )
        else:
            switch_name = 's3' + str( i +1 )
        sw = net.addSwitch(switch_name, cls=OVSKernelSwitch)
        aces_sw.append( sw )

    info( '*** Adding hosts ***\n')
    #Adding normal hosts
    for i in xrange(1,191):
        host_name = 'h' + str(i)
        ip_addr = '10.0.' + str((i/100)) + '.' + str((i%100))
        hs = net.addHost(host_name,cls = Host,ip = ip_addr,defaultRoute=None)
        h.append( hs )
    #Adding the special host "h291"
    hs = net.addHost('h191',cls = Host,ip = '10.0.1.91',defaultRoute=None)
    h.append( hs )

    info( '*** Adding links ***\n')
    #Adding the special link between h291 and s101
    net.addLink(core_sw[0],h[190])
    #Adding links between core switches and distribution switches
    for i in range(core_num):
        for j in range(dist_num):
            net.addLink(core_sw[i],dist_sw[j])
    #Adding links between distribution switches and access switches
    for i in range(dist_num):
        for j in range(5):
            net.addLink(dist_sw[i],aces_sw[i*5+ j])
    #Adding links between access switche s301 and 100 normal hosts
    for i in range(100):
        net.addLink(aces_sw[0], h[i])
    #Adding links between other access switches and ohter normal hosts
    for i in xrange(1,aces_num):
        for j in range(fanout_num):
            net.addLink(aces_sw[i], h[(i-1)*fanout_num+j+100])

    

    info( '*** Starting network ***\n')
    net.build()

    info( '*** Starting controllers ***\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches ***\n')
    for i in range(core_num):
        net.get(core_sw[i].name).start([RYU])
    for i in range(dist_num):
        net.get(dist_sw[i].name).start([RYU])
    for i in range(aces_num):
        net.get(aces_sw[i].name).start([RYU])

    info( '*** Post configure switches and hosts ***\n')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()            